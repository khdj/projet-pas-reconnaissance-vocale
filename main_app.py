import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

from dl_audio_subs_from_yt import *
from api import *
from compare_api import *
from main import *


AUDIO_PATH = './Audio_files/'
MEDIA_FORMAT = 'mp3'
LANGUAGE = 'en-US'
CSV_FILE_NAME = 'api_comparison.csv'

@st.cache
def load_data(file_name):
	df = pd.read_csv(file_name, index_col=0)

	return df

def main():
	st.title('Projet PAS, reconnaissance vocale')
	st.write("### Comparateur d'API")
	st.write('Khadidiatou BADJI, Raphaël LAURENT')

	st.write("""## Entrez un lien Youtube : """)

	yt_link = st.text_input("URL Youtube :", 'https://youtu.be/g0Q5YeZ4YOA')


	if st.button('Valider'):

		#Pour appeler toutes API en mm tps (+ mets les resultats dans le csv)
		#run(yt_link)

		st.write('#### Résultats pour ce run :')
		df = load_data(CSV_FILE_NAME)

		table_execution_time = df[['api', 'execution_time']]
		st.write(table_execution_time.iloc[-3:])
		chart = alt.Chart(df.iloc[-3:]).mark_bar().encode(
	    alt.X("execution_time"),
	    alt.Y('api'),
	    color = "api",
		)
		st.altair_chart(chart)

		table_word_error_rate = df[['api','word_error_rate',]]
		st.write(table_word_error_rate.iloc[-3:])
		chart = alt.Chart(df.iloc[-3:]).mark_bar().encode(
	    alt.X("word_error_rate"),
	    alt.Y('api'),
	    color = "api",
		)
		st.altair_chart(chart)


		table_grammatical_score_percentage = df[['api','grammatical_score_percentage']]
		st.write(table_grammatical_score_percentage.iloc[-3:])
		chart = alt.Chart(df.iloc[-3:]).mark_bar().encode(
		    alt.X("grammatical_score_percentage"),
		    alt.Y('api'),
		    color = "api",
		)
		st.altair_chart(chart)
		
		st.write(df)


main()