#Rewrite the entire task 1B without using functions

#Initialize two data structures to keep track of books and members both represented as lists.
books = []
members = []

bookDetails = ({'book_id': int(input("Enter book ID: ")),
                  'title': input("Enter a book title: "),
                  'author': "Nqobani Gumede",
                  'status': "Available"})

books.append(bookDetails)

    
memberDetails = ({'member_id': 4652,
                    'name': "Khumalo",
                    'borrowed_books': []})
    
members.append(memberDetails)

"""Suppose you use the system to add a book titled "Python Programming" written by Jacob Zuma with a
book_id of 2024001, and a member named Anelisa Maleka with a member_id of 1."""
#write a print statement for them.
print("Books", books)
print("\nMembers:", members)

