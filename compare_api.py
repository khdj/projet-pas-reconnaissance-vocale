"""
here: (other script to get all data ?)
    - dl file from yt
        - (add sending the file to bucket for aws
          + sending it to the cloud for google already ok)
    - call each constructor API
    - call transcribe method and get result
    - upload everything to csv/excel file
    - compare : (add all scores to csv) -> comparison on api
        - error rate
        - grammatical errors
        - execution time
        - ponctuation ?

"""

from dl_audio_subs_from_yt import *
from api import *
from jiwer import wer
import webvtt


def vtt_to_string(vtt_file_name):
    vtt = webvtt.read(vtt_file_name)
    transcript = ""

    lines = []
    for line in vtt:
        lines.extend(line.text.strip().splitlines())

    previous = None
    for line in lines:
        if line == previous:
            continue
        transcript += " " + line
        previous = line
    return transcript


def find_all_wer(real_text, watson_text, google_text, amazon_text):
    error_watson = wer(real_text, watson_text)
    error_google = wer(real_text, google_text) 
    error_amazon = wer(real_text, amazon_text)
    return {"watson" : watson_text, "google" : google_text, "amazon" : amazon_text}, {"watson" : error_watson, "google" : error_google, "amazon" : error_amazon}

"""def run(yt_url, lang_model):
    lang = lang_model[:2]
    download(yt_url, lang=lang)

    watson = WatsonApi()
    google = GoogleApi()
    amazon = AwsApi()
    all_text, all_wer = find_all_wer(real_text, watson_text, google_text, amazon_text)"""

