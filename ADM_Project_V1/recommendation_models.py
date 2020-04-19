import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/half_users_books_ratings_v1.csv')
# user_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/user_details.csv')

final = books_details_df.pivot_table(values='rating',index='user_id',columns='book_id')
print(final.head())

book_similarity = final.copy().fillna(final.mean(axis=0))
print(book_similarity.head())

user_similarity = final.apply(lambda row: row.fillna(row.mean()), axis=1)
print(user_similarity.head())

b = cosine_similarity(user_similarity)
np.fill_diagonal(b, 0)
similarity_with_user = pd.DataFrame(b,index=user_similarity.index)
similarity_with_user.columns=user_similarity.index
similarity_with_user.head()



# user similarity on replacing NAN by item(book) avg
cosine = cosine_similarity(book_similarity)
np.fill_diagonal(cosine, 0)
similarity_with_book = pd.DataFrame(cosine,index=book_similarity.index)
similarity_with_book.columns=user_similarity.index
similarity_with_book.head()



def get_user_similar_books( user1, user2 ):
    common_books = books_details_df[books_details_df.user_id == user1].merge(
    books_details_df[books_details_df.user_id == user2], on = "book_id", how = "inner" )
    return common_books.merge(books_details_df, on='book_id')


a = get_user_similar_books(1,2)
print(a.head())

