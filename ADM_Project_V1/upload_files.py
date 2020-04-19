import pandas as pd

# books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/users_books_ratings.csv')
#
# books_details_df = books_details_df.iloc[:5000]
#
# books_details_df.to_csv("C:/Users/Nikhita/Desktop/Dataset/Final/half_users_books_ratings_v1.csv")
# # print(books_details_df.size())


books_details_df = pd.read_csv('C:/Users/Nikhita/Desktop/Dataset/Final/new_data.csv')
# print(books_details_df.columns)

books_details_df = books_details_df.drop(columns=['Unnamed: 0','goodreads_book_id','best_book_id','work_id','book_rating'])

print(books_details_df.columns)
# books_details_df = books_details_df.rename(columns={'book_rating': "rating"})

# data for initial testing purpose
books_details_df = books_details_df.iloc[:5000]

books_details_df.to_csv("C:/Users/Nikhita/Desktop/Dataset/Final/final_book_details.csv")
# # print(books_details_df.size())


# unique books

unique_books_df = books_details_df.drop(columns=['user_id','book_isbn','Invoice_Date','Quantity'])

unique_books_group = unique_books_df.groupby(['book_id','book_authors','book_title','language_code','genres','image_url']).mean()
unique_books_group = unique_books_group.reset_index()
unique_books_group['rating'] = unique_books_group.rating.round(2)

unique_books = unique_books_group

unique_books.to_csv("C:/Users/Nikhita/Desktop/Dataset/Final/unique_books.csv")

