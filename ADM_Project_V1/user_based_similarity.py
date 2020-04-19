import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re
import sklearn.metrics.pairwise as pw
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances

books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/half_users_books_ratings_v1.csv')


def user_based_recom(input_dataframe, input_user_id):
    pivot_user_based = pd.pivot_table(input_dataframe, index='user_id', columns=['title'], values='rating')
    print(pivot_user_based)
    sparse_pivot_ub = sparse.csr_matrix(pivot_user_based.fillna(pivot_user_based.mean(axis=0)))
    # print(sparse_pivot_ub)
    user_recomm = pw.cosine_similarity(sparse_pivot_ub)
    print("user rec")
    print(user_recomm)
    user_recomm_df = pd.DataFrame(user_recomm, columns=pivot_user_based.index.values,
                                  index=pivot_user_based.index.values)
    print("user rec df")

    print(user_recomm_df)
    ## Item Rating Based Cosine Similarity
    usr_cosine_df = pd.DataFrame(user_recomm_df[input_user_id].sort_values(ascending=False))
    usr_cosine_df.reset_index(level=0, inplace=True)
    usr_cosine_df.columns = ['user_id', 'cosine_sim']
    print(usr_cosine_df)

    similar_usr = usr_cosine_df['user_id'][1:5]
    l = []
    for i in similar_usr:
        l.append(input_dataframe[input_dataframe['user_id'] == i])
    print(l)

    print(similar_usr)
    return similar_usr


a = user_based_recom(books_details_df, 9)

print(a)
