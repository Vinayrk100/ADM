import pandas as pd,csv
import flask

def recommend_books(l_title,l_author,l_lg,l_genre):
    first_line = True
    books_suggestion = []
    with open('C:/Users/Nikhita/Desktop/books.csv', encoding='cp850') as csv_file:
                books = csv.reader(csv_file, delimiter=',')
                for row in books:
                    # print(row[0])
                    if not first_line:
                        # 04/11
                        if (l_title != ""):
                              if row[10] == l_title:
                                books_suggestion.append({
                                                "bookid": row[0],
                                                "Author": row[7],
                                                "title": row[10],
                                                "image_url": row[21]
                                                    })

                        if l_author != "" or  l_lg != "" or l_genre != "":
                            if row[7] == l_author or row[11] == l_lg:
                                books_suggestion.append({
                                    "bookid": row[0],
                                    "Author": row[7],
                                    "title": row[10],
                                    "image_url": row[21]
                                })
                    else:
                        first_line = False
    return books_suggestion