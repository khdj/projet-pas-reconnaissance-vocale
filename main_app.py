import streamlit as st
import pandas as pd

from dl_audio_subs_from_yt import *
from api import *


AUDIO_PATH = '/Audios_files/'
MEDIA_FORMAT = 'mp3'
LANGUAGE = 'en-US'


def main():
	st.title('Projet PAS, reconnaissance vocale')

	st.write("""## Entrez un lien Youtube : """)

	yt_link = st.text_input("URL Youtube :", 'https://youtu.be/g0Q5YeZ4YOA')


	if st.button('Valider'):

		audio_file_name, subs_file_name = download(yt_link)
		st.write("""Téléchargement de la vidéo :""" + audio_file_name + """ et de ses sous-titres terminé. """)
		file_path = str(AUDIO_PATH + audio_file_name)
		st.write("""appelle des API : """)

		#test
		AwsAPI = AwsApi()

		text = AwsAPI.transcribe(file_path, MEDIA_FORMAT, LANGUAGE)
		st.write(text)

main()