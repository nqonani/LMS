#Rewrite the entire Task 1 C using Data frames instead of lists.
import pandas as pd

bookDetails = ({'book_id': [int(input("Enter book ID: "))],
                  'title': input[("Enter book name: ")],
                  'author': ["Nqobani Gumede"],
                  'status': ["Available"]})

dfB = pd.DataFrame(bookDetails)

print("Data Frame for books: ", dfB)
    
memberDetails = ({'member_id': [4652],
                    'name': ["Khumalo"],
                    'borrowed_books': [[]]})

dfM = pd.DataFrame(memberDetails)

print("Data Frame for member: ", dfM)