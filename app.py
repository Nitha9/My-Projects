import streamlit as st

import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests. get('https://api.themoviedb.org/3/movie/ {}?api_key=415b84137b7e905b52ca9101e35b6139&language=en-US'.format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    fullpath = "https://image.tmdb.org/t/p/w500" + poster_path
    return fullpath

def recommend(movie: object) -> object:
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie =[]
    recommendedmovies_poster =[]
    
    for i in movie_list[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommendedmovies_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommendedmovies_poster


movies_list = pickle.load(open('movies.pk1','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
movie_list = movies['title'].values
option = st.selectbox('Select the movie', movies['title'].values)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    #with col5:
     #   st.text(recommended_movie_names[4])
      #  st.image(recommended_movie_posters[4])