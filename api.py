# install ibm_watson
# install google-cloud-speech
# install boto3

import io
import json
import ntpath
import urllib
from abc import abstractmethod

import boto3
from google.cloud import speech
from google.oauth2 import service_account
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1
import urllib.parse
# import requests
# import speech_recognition as sr
# from google.oauth2 import service_account


class API:

    @abstractmethod
    def transcribe(self, audio_file_path, audio_type, lang_model):
        raise NotImplementedError()


class WatsonApi(API):
    def __init__(self):
        apikey = "_I97e0HrO3bRZoQ-R5whIAIElGbgC6lM3VLvhuxvLMzx"
        url = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/0539da85-8f81-4a06-a3ed-837ed5039c1d"

        authenticator = IAMAuthenticator(apikey=apikey)
        self.stt = SpeechToTextV1(authenticator=authenticator)
        self.stt.set_service_url(url)

    def transcribe(self, audio_file_path, audio_type, lang_model):
        text = ""
        with open(audio_file_path, 'rb') as audio_file:
            res = self.stt.recognize(audio=audio_file, content_type=audio_type, model=lang_model,
                                     continuous=True).get_result()
        all_res = res['results']
        for res in all_res:
            text = f"{text}{res['alternatives'][0]['transcript']}"  # ajouter un saut de ligne à la fin ?
        return text


class AwsApi(API):
    def __init__(self):
        AWS_ACCESS_KEY_ID = 'AKIAJOHGFZ7IIA7755LA'
        AWS_SECRET_ACCESS_KEY = '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'

        self.job_name = 'test'
        self.path = 'https://s3.amazonaws.com/bucketpas/'
        self.service = boto3.client('transcribe', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='eu-west-3')

    def check_job_name(self, job_name):
        # all the transcriptions
        existed_jobs = self.service.list_transcription_jobs()
        for job in existed_jobs['TranscriptionJobSummaries']:
            if job_name == job['TranscriptionJobName']:
                self.service.delete_transcription_job(TranscriptionJobName=job_name)
                break

    def transcribe(self, audio_file_path, audio_type, lang_model):
        self.check_job_name(self.job_name)
        file_name = ntpath.basename(audio_file_path)
        job_uri = f"{self.path}{urllib.parse.quote(file_name)}" 
        self.service.start_transcription_job(TranscriptionJobName=self.job_name, Media={'MediaFileUri': job_uri},
                                             MediaFormat=audio_type, LanguageCode=lang_model)

        while True:
            res = self.service.get_transcription_job(TranscriptionJobName=self.job_name)
            if res['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break
            # print("Not ready yet...")
            # time.sleep(2)
        # print(status)
        if res['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
            with urllib.request.urlopen((res['TranscriptionJob']['Transcript']['TranscriptFileUri'])) as url:
                s = url.read()
                # print(s)
                data = json.loads(s)
                text = data['results']['transcripts'][0]['transcript']
                print(text)
        return text

#real google api
class GoogleApi(API):
    def __init__(self):
        # Instantiates a client
        API_CREDENTIALS = "projet-pas-text-to-speech-api-f2a45acc63a5.json"
        my_credentials = service_account.Credentials.from_service_account_file(API_CREDENTIALS)
        self.client = speech.SpeechClient(credentials=my_credentials)

    # need to convert to wav
    def transcribe(self, audio_file_path, audio_type, lang_model):
        # Loads the audio file into memory
        with io.open(audio_file_path, "rb") as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            audio_channel_count=2,
            language_code=lang_model,  # en-US
        )

        # Sends the request to google to transcribe the audio
        response = self.client.recognize(request={"config": config, "audio": audio})

        # Reads the response
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))

        return result.alternatives[0].transcript


## other google api (speechrecognition module)