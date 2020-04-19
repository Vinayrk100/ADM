import pandas as pd

def read_book_details(title):
    df = pd.read_csv("C:/Users/Nikhita/Desktop/Dataset/Final/unique_books.csv")
    lst = df[df['book_title'] == title]
    return lst
