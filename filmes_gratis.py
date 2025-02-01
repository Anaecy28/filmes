import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

key_dict = json.loads(st.secrets["textkey"])
st.write(key_dict)
#key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project=key_dict["project_id"])
st.error("Conexión a Firestore exitosa")

def read_from_firestore():
    try:
        movies_ref = db.collection("movies")
        docs = movies_ref.stream()

        movies_list = []
        for doc in docs:
            movies_list.append(doc.to_dict())

        if not movies_list:
            st.write("No se encontraron películas en Firestore.")

        return pd.DataFrame(movies_list)

    except Exception as e:
        st.write(f"Error al leer desde Firestore: {e}")

df_movies = read_from_firestore()
if not df_movies.empty:
    st.write(df_movies.head()) 
