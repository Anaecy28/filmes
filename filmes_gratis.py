import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

st.write(st.secrets["textkey"])  

key_string = st.secrets["textkey"]
if isinstance(key_string, str):
    key_dict = json.loads(key_string)
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project=key_dict["project_id"])
    st.write("Conexión a Firestore exitosa")
else:
    st.error("El valor de 'textkey' no es un string.")
