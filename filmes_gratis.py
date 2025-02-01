import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project=key_dict["project_id"])
st.write("Conexión a Firestore exitosa")

def read_from_firestore():
    movies_ref = db.collection("movies")
    docs = movies_ref.stream()

    movies_list = []
    for doc in docs:
        movies_list.append(doc.to_dict())

    return pd.DataFrame(movies_list)

df_movies = read_from_firestore()
print(df_movies.head())

df_movies = read_from_firestore()
st.sidebar.header("Buscar Películas")
search_query = st.sidebar.text_input("Ingrese el título de la película")
search_button = st.sidebar.button("Buscar")

if st.sidebar.checkbox("Mostrar todas las películas"):
    st.dataframe(df_movies)

if search_button:
    filtered_df = df_movies[df_movies["name"].str.contains(search_query, case=False, na=False)]
    st.dataframe(filtered_df)
def read_from_firestore():
    movies_ref = db.collection("movies")
    docs = movies_ref.stream()

    movies_list = []
    for doc in docs:
        movies_list.append(doc.to_dict())

    return pd.DataFrame(movies_list)
