import streamlit as st
import pandas as pd

from dl_audio_subs_from_yt import *
from api import *
from compare_api import *


AUDIO_PATH = './Audios_files/'
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

		text_AWS = AwsAPI.transcribe(file_path, MEDIA_FORMAT, LANGUAGE)

		#text_watson = 

		#text_google = 
		st.write('text_AWS:')
		st.write(text_AWS)

		vtt_file_path = str(AUDIO_PATH + subs_file_name)
		subtitles = vtt_to_string(vtt_file_path)

		st.write('subtitles:')
		st.write(subtitles)


		dict_text = {}
		dict_wer = {}
		#dict_text, dict_wer = find_all_wer(subtitles, text_watson, text_google, text_AWS)
		#test :
		error_aws = wer(subtitles, text_AWS)

		st.write('error_aws:')
		st.write(error_aws)





main()