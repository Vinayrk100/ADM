import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re
import sklearn.metrics.pairwise as pw
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances


def similar_items(title):
    cos_sim = title_based_recom(title)
    cos_sim = cos_sim[cos_sim['ratings_count'] > 1000]
    a = cos_sim.sort_values(by='ratings_count')
    cos_sim = cos_sim.drop(['user_id', 'rating'], axis=1)
    cos_sim = cos_sim.drop_duplicates()

    return cos_sim


def title_based_recom(input_book_name):
    books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/final_book_details.csv')
    # books_details_df = books_details_df.drop(columns=['invoice_date', 'Quantity'])
    pivot_item_based = pd.pivot_table(books_details_df,
                                      index='book_title',
                                      columns=['user_id'], values='rating')
    sparse_pivot = sparse.csr_matrix(pivot_item_based.fillna(pivot_item_based.mean(axis=0)))
    recommender = pw.cosine_similarity(sparse_pivot)

    recommender_df = pd.DataFrame(recommender,
                                  columns=pivot_item_based.index,
                                  index=pivot_item_based.index)

    ## Item Rating Based Cosine Similarity
    cosine_df = pd.DataFrame(recommender_df[input_book_name].sort_values(ascending=False))
    cosine_df.reset_index(level=0, inplace=True)
    cosine_df.columns = ['title', 'cosine_sim']
    df_count = pd.merge(cosine_df, books_details_df, on='title')
    return df_count


title_recommendation = title_based_recom("How to Win Friends and Influence People")

title_recommendation.to_csv("C:/Users/Nikhita/Desktop/Dataset/Final/Output/title_recommendation.csv")
