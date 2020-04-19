import pandas as pd

books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/final_book_details.csv')
df_ratings = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/ratings.csv')
user_rating_data = df_ratings[df_ratings.user_id == 2]

user_full = (user_rating_data.merge(books_details_df, how='left', on='book_id').sort_values(['rating'], ascending=False))
print(user_full)
print(user_full.columns)