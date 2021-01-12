import streamlit as st
import pandas as pd

from dl_audio_subs_from_yt import *

st.title('Projet PAS, reconnaissance vocale')

st.write("""## Entrez un lien Youtube : """)

yt_link = st.text_input("URL Youtube :", 'https://youtu.be/g0Q5YeZ4YOA')

if st.button('Valider'):

	titre = download(yt_link)
	st.write("""Téléchargement de la vidéo et de ses sous-titre terminé. """)



