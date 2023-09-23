import sys
import importlib
import contextlib
import subprocess
from io import StringIO
# Movie Recommendation dependencies
# import numpy as np
# import pandas as pd
# import difflib
# from sklearn.feature_extraction.text import TfidfVectorizer #to convert text data into numerical data
# from sklearn.metrics.pairwise import cosine_similarity


# Whatsapp Chatbot Part
@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old



def execute_python(code):
    with stdoutIO() as c:
        try:

            # Trying start
            import numpy as np
            import pandas as pd
            import difflib
            from sklearn.feature_extraction.text import TfidfVectorizer  # to convert text data into numerical data
            from sklearn.metrics.pairwise import cosine_similarity
            # Trying end
            # Movie Recommendation Part

            movies_data = pd.read_csv('movies (1).csv', encoding='utf-8')
            movies_data.head()
            movies_data.shape
            features = ['genres', 'keywords', 'tagline', 'cast', 'director']

            # Replacing null values with null strings
            for i in features:
                movies_data[i] = movies_data[i].fillna('')
            # combining all the selected features

            combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data[
                'tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
            combined_features
            vectorizer = TfidfVectorizer()
            feature_vectors = vectorizer.fit_transform(combined_features)
            similarity = cosine_similarity(feature_vectors)
            movie_name = code
            # creating a list containing the movie name in the dataset
            movie_titles = movies_data['title'].tolist()
            movie_titles
            # finding close match for the user input movie name

            close_match = difflib.get_close_matches(movie_name, movie_titles)
            index_of_the_movie = movies_data[movies_data.title == close_match[0]]['index'].values[0]
            index_of_the_movie
            similarity_score = list(enumerate(similarity[index_of_the_movie]))
            similarity_score
            # Filter the movies that have higher similarity score value

            sorted_similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
            sorted_similarity_score
            print("Movies Suggested for you : \n")
            i = 1
            for j in sorted_similarity_score:
                index = j[0]
                title_from_index = movies_data[movies_data.index == index]['title'].values[0]
                if (i <= 15):
                    print(i, '-', title_from_index)
                    i += 1

            # Movie Recommendation part end

        except:
          print("Something went wrong")
    return c.getvalue()
