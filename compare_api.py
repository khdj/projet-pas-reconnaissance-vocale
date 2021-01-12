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


def run(yt_url, lang_model):
    lang = lang_model[:2]
    download(yt_url, lang=lang)

    watson = WatsonApi()
    google = GoogleApi()
    amazon = AwsApi()


