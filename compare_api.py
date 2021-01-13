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

# install webvett-py

#from jiwer import wer

#install asr-evaluation
# import asr_evaluation


import webvtt
import requests

"""
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
"""

def get_grammatical_score(text):  # returns (grammatical errors nb, grammatical errors percentage)
    url = "https://virtualwritingtutor.com/api/checkgrammar.php"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"appKey": "deb81f80-2fca-11eb-b604-ff319903c933",
            "text": text}
    r = requests.post(url, headers=headers, data=data)
    if r.status_code == 200:
        content = r.json()
        errors_nb = content['error_grammar_count_total']
        error_percent = content['error_grammar_percent']
        # print(f"Input text :\n{text}\n\n"
        #      f"Grammatical errors nb : {errors_nb}\n"
        #      f"Grammatical errors percent : {error_percent}")
        return int(errors_nb), float(error_percent[:-1])
    else:
        print(f"Problem with request ! {r.status_code} error")
        return -1, -1

"""
def get_error_rate(real_text, transcript):
    return wer(real_text, transcript)


def find_all_wer(real_text, watson_text, google_text, amazon_text):
    error_watson = wer(real_text, watson_text)
    error_google = wer(real_text, google_text)
    error_amazon = wer(real_text, amazon_text)
    return {"watson": watson_text, "google": google_text, "amazon": amazon_text}, {"watson": error_watson,
                                                                                   "google": error_google,
                                                                                   "amazon": error_amazon}
"""

"""def run(yt_url, lang_model):
    lang = lang_model[:2]
    download(yt_url, lang=lang)

    watson = WatsonApi()
    google = GoogleApi()
    amazon = AwsApi()
    all_text, all_wer = find_all_wer(real_text, watson_text, google_text, amazon_text)"""
