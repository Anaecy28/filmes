import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

st.title('NETFLIX APP')
st.title("Todos los filmes")
st.header("Todos las peliculas")

#df_movies = read_from_firestore()
df_movies = None
st.sidebar.header("Buscar Películas")
search_query = st.sidebar.text_input("Ingrese el título de la película")
search_button = st.sidebar.button("Buscar")

if st.sidebar.checkbox("Mostrar todas las películas"):
    st.dataframe(df_movies)

if search_button:
    filtered_df = df_movies[df_movies["name"].str.contains(search_query, case=False, na=False)]
    st.dataframe(filtered_df)


st.write(st.secrets["textkey"])  

key_dict = st.secrets["textkey"]["credentials"]
key_dict["private_key"] = key_dict["private_key"].replace("\n", "")
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project=key_dict["project_id"])
st.write("Conexión a Firestore exitosa")
