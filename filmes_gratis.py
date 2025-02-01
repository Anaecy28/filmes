import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

db = firestore.Client.from_service_account_json("firebase.json")
dbNames = db.collection("names")

def loadByName(name):
  names_ref = dbNames.where(u'name', u'==',name)
  currentName =  None
  for myname in names_ref.stream():
    currentName =  myname
  return currentName

#BTN BUSCAR
st.sidebar.subheader("Buscar nombre")
nameSearch= st.sidebar.text_input("nombre")
btnFiltrar= st.sidebar.button("Buscar")

if btnFiltrar:
  doc = loadByName(nameSearch)
  if doc is None:
    st.sidebar.write("Nombre no existe")
  else:
    st.sidebar.write(doc.to_dict())

# BTN ELIMINAR

st.sidebar.subheader("Eliminar registro")
nameSearch= st.sidebar.text_input("nombre a eliminar")
btnEliminar= st.sidebar.button("Eliminar")

if btnEliminar:
  deleteName = loadByName(nameSearch)
  if deleteName is None:
    st.sidebar.write(f"{nameSearch} no existe")
  else:
    dbNames.document(deleteName.id).delete()
    st.sidebar.write(f"{nameSearch} eliminado")

# BTN ACTUALIZAR

st.sidebar.subheader("Actualizar registro")
nameNew= st.sidebar.text_input("nombre a actualizar")
btnActualizar= st.sidebar.button("Actualizar")

if btnActualizar:
  actualizarName = loadByName(nameSearch)
  if actualizarName is None:
    st.sidebar.write(f"{nameSearch} no existe")
  else:
    miActualizarName = dbNames.document(actualizarName.id)
    miActualizarName.update(
        {
            "name": nameNew
        }
    )
