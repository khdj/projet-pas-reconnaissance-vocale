import streamlit as st
import pandas as pd

from dl_audio_subs_from_yt import *
from api import *


AUDIO_PATH = '/Audios_files/'

st.title('Projet PAS, reconnaissance vocale')

st.write("""## Entrez un lien Youtube : """)

yt_link = st.text_input("URL Youtube :", 'https://youtu.be/g0Q5YeZ4YOA')

if st.button('Valider'):

	audio_file_name, subs_file_name = download(yt_link)
	st.write("""Téléchargement de la vidéo :""" + audio_file_name + """et de ses sous-titres terminé. """)

if st.button('Appeler les API'):
	WatsonApi.transcribe(AUDIO_PATH + audio_file_name)


