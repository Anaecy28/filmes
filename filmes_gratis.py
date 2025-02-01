import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

st.title('NETFLIX APP')
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

data = {
    'title': ['Film 1', 'Film 2', 'Film 3', 'Film 4'],
    'director': ['Director A', 'Director B', 'Director A', 'Director C']
}
df = pd.DataFrame(data)

director_selected = st.sidebar.selectbox(
    "Seleccione un director",
    options=df['director'].unique(),
    index=0  
)

def filter_films_by_director(director):
    filtered_df = df[df['director'] == director]
    return filtered_df

if st.sidebar.button("Buscar Filmes"):
    filtered_films = filter_films_by_director(director_selected)
    
    st.write(f"Filmes encontrados de {director_selected}:")
    st.dataframe(filtered_films) 
    st.write(f"Total de filmes encontrados: {len(filtered_films)}")



key_dict = st.secrets["textkey"]
st.write(key_dict)  
key_dict["private_key"] = key_dict["private_key"].replace("\\n", "\n")
#creds = service_account.Credentials.from_service_account_info(key_dict)
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project=key_dict["project_id"])
st.write("Conexión a Firestore exitosa")
