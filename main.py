# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from api import *
from dl_audio_subs_from_yt import *
from vtt_to_string import vtt_to_text
import streamlit as st

AUDIO_PATH = "./Audio_files/"
MEDIA_FORMAT = 'mp3'
LANG_MODEL = 'en-US'


def add_to_csv(api, api_name, audio, subs_formatted):
    print(f"Start decoding for {api_name}...")
    start_time = time.time()
    transcript = api.transcribe(f"{AUDIO_PATH}{audio}")
    elapsed_time = time.time() - start_time
    print(f"Decoding successful in {elapsed_time} s")

    # print(text_watson)
    g_errors_nb, g_error_score = get_grammatical_score(transcript)
    error_rate = get_error_rate(subs_formatted, transcript)
    data = {
        "api": api_name,
        "audio": audio,
        "execution_time": elapsed_time,
        "word_error_rate": error_rate,
        "grammatical_errors": g_errors_nb,
        "grammatical_score_percentage": g_error_score,
        "transcription": transcript,
    }
    # print(transcript)
    df = pd.DataFrame([data])
    df.to_csv("api_comparison.csv", mode='a', header=False)
    print(df.head())


def run(yt_url):
    lang = LANG_MODEL[:2]

    #ici j'ai commenté et j'ai écrit les fichiers en dur pcq je voulais pas qu'il me les reletecharge a chq fois pour gagner du tps
    audio, subs = download(yt_url, lang=lang)
    #audio = "20201013 Why is the world warming up _ Kristen Bell + Giant Ant.mp3"
    #subs = "20201013 Why is the world warming up _ Kristen Bell + Giant Ant.en.vtt"

    st.write("Téléchargement de la vidéo :" + audio + " et de ses sous-titres terminé." )
    st.write("appelle des API : ... ")

    subs_formatted = vtt_to_text(f"{AUDIO_PATH}{subs}")

    watson = WatsonApi()
    google = GoogleApi()
    amazon = AwsApi()

    st.write("Appelle Google... ")
    add_to_csv(google, "google", audio, subs_formatted)
    st.write("Google terminé ")
    st.write("Appelle Watson ... ")
    add_to_csv(watson, "watson", audio, subs_formatted)
    st.write("Watson terminé ")
    st.write("Appelle Amazon ... ")
    add_to_csv(amazon, "amazon", audio, subs_formatted)
    st.write("Amazon terminé ")


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    url = "https://www.youtube.com/watch?v=-UV3xm9pZ0g"
#    run(yt_url=url)
