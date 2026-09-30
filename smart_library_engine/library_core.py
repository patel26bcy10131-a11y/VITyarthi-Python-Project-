
# libraray core code --
def create_book_record(isbn, title, author, pub_year, category):
    
    #Returns an immutable tuple representing a single book record
    (isbn, title, author, pub_year, category)
    
    return (str(isbn), str(title), str(author), int(pub_year), str(category))


def build_catalog_dictionary(book_tuple_list):
    
#this Converts a list of book tuples into a dictionary mapped by ISBN
    
    catalog_dict = {}
    for book in book_tuple_list:
        isbn = book[0]
        catalog_dict[isbn] = book
    return catalog_dict


def filter_books_by_category(catalog_dict, category_name):
#Filtering  catalog dictionary entries matching a specific category

    matches = []
    for isbn, book_info in catalog_dict.items():
    # book info 4 represents the category field
        if book_info[4].lower() == category_name.lower():
            matches.append(book_info)
    return matches