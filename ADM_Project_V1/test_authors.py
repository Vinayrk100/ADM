import pandas as pd
import numpy as np

books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/users_books_ratings.csv')


def item_and_author_based_recom(books_details, authors):
    ## Item Rating and Gender Based Cosine Similarity
    # top_cos_genre = pd.merge(cosine_df, books_details_df, on='title')
    return books_details[['title']]


author_sim = item_and_author_based_recom(books_details_df, books_details_df.authors)

print(author_sim)
