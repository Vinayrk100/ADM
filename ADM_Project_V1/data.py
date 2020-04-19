import pandas as pd,csv
import numpy as np

# ratings = pd.read_csv('C:/Users/Nikhita/Desktop/ratings.csv')
# books = pd.read_csv('C:/Users/Nikhita/Desktop/books.csv')
# print(books.head())
# C:\Users\Nikhita\Desktop\Algorithmic Digital Marketing\Project Proposal\Data\books

# books = pd.read_csv('C:/Users/Nikhita/Desktop/books.csv')
first_line = True
books_suggestion = []
with open('C:/Users/Nikhita/Desktop/books.csv',encoding = 'cp850') as csv_file:
    books = csv.reader(csv_file, delimiter=',')
    # print(data)
    for row in books:
        # print(row[0])
        if not first_line:
            books_suggestion.append({
                "bookid": row[0],
                "Author": row[7],
                "title": row[10],
                "image_url": row[21]
            })
        else:
            first_line = False
print(books_suggestion)