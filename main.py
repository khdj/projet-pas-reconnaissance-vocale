# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from dl_audio_subs_from_yt import *
from api import *
from vtt_to_string import vtt_to_text
import time
from compare_api import *
import pandas as pd


def run(yt_url, lang_model="en-US"):
    AUDIO_PATH = "./Audio_files/"
    lang = lang_model[:2]
    audio, subs = download(yt_url, lang=lang)

    # with open(f"{AUDIO_PATH}{subs}", 'r') as f:
    #    subs_content = f.read()
    subs_formatted = vtt_to_text(f"{AUDIO_PATH}{subs}")
    #print(audio)
    #print(subs)

    watson = WatsonApi()
    google = GoogleApi()
    amazon = AwsApi()

    """
    print("Start decoding for watson...")
    start_time = time.time()
    text_watson = watson.transcribe(f"{AUDIO_PATH}{audio}")
    elapsed_time = time.time() - start_time
    print(f"Decoding successful in {elapsed_time} s")

    # print(text_watson)
    g_errors_nb, g_error_score = get_grammatical_score(text_watson)
    error_rate = get_error_rate(subs_formatted, text_watson)
    watson_data = {
        "api": "watson",
        "audio": audio,
        "execution_time": elapsed_time,
        "word_error_rate": error_rate,
        "grammatical_errors": g_errors_nb,
        "grammatical_score_percentage": g_error_score,
        "transcription": text_watson,
    }
    # print(text_watson)
    df = pd.DataFrame([watson_data])
    df.to_csv("api_comparison.csv")
    """

    amazon.add_to_csv(audio, f"{AUDIO_PATH}{audio}", subs_formatted, "amazon")
    #=> error - upload_to_aws : AttributeError: 'TranscribeService' object has no attribute 'upload_file'
    #watson.add_to_csv(audio, f"{AUDIO_PATH}{audio}", subs_formatted, "watson")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=-UV3xm9pZ0g"
    run(yt_url=url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
