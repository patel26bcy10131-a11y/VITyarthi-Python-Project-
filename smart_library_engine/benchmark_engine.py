import time
import library_core

def generate_large_dataset(record_count=10000):
    #Generates a large list of synthetic book tuples.
    dataset = []
    categories = ["CS", "Calculus", "English", "Environmental Studies "]

    for i in range(1, record_count + 1):
        isbn = f"978-{100000 + i}"
        title = f"Book Title {i}"
        author = f"Author {i % 100}"
        year = 2000 + (i % 25)
        category = categories[i % len(categories)]

        book = library_core.create_book_record(isbn, title, author, year, category)
        dataset.append(book)

    return dataset


def run_search_performance_test(record_count=10000, queries_count=500):
    
    #Measures and compares sequential list search vs dictionary lookup time.

    dataset_list = generate_large_dataset(record_count)
    catalog_dict = library_core.build_catalog_dictionary(dataset_list)

    # Picking a sample of ISBNs to search for
    search_isbns = [f"978-{100000 + (i * 17) % record_count + 1}" for i in range(queries_count)]

    # 1. Benchmark Sequential List Search O(N)
    start_time = time.perf_counter()
    list_found_count = 0
    for target_isbn in search_isbns:
        for book in dataset_list:
            if book[0] == target_isbn:
                list_found_count += 1
                break
    list_search_time = time.perf_counter() - start_time

    # 2. Benchmark Dictionary Key Lookup O(1)
    start_time = time.perf_counter()
    dict_found_count = 0
    for target_isbn in search_isbns:
        if target_isbn in catalog_dict:
            dict_found_count += 1
    dict_search_time = time.perf_counter() - start_time

    return list_search_time, dict_search_time, (list_found_count == dict_found_count)