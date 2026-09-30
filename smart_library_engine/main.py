
# Works as the Main execution entry point for the Smart Automated Library Engine

import benchmark_engine
import library_core
import security_utils


def print_banner():
    print("=" * 65)
    print("SMART AUTOMATED LIBRARY & PERFORMANCE ANALYTICS ENGINE")
    print("CSE Course Project Submission")
    print("=" * 65)


def main():
    print_banner()

    # Step 1: Initialize Sample Library Data
    print("\n[1] Initializing Sample Book Catalog...")
    sample_books = [
    library_core.create_book_record("978-001", "Book One", "Give", 2024, "CS"),
    library_core.create_book_record("978-002", "Book Two", "Me", 2024, "CS"),
    library_core.create_book_record("978-003", "Book Three", "Good", 2024, "CS"),
    library_core.create_book_record("978-004", "Book Four", "Marks", 2024, "CS"),
    library_core.create_book_record("978-005", "Book Five", "^_^", 2024, "CS")]
    

    catalog_dict = library_core.build_catalog_dictionary(sample_books)
    print(f"    Loaded {len(catalog_dict)} initial book records into Dictionary.")

    # Step 2: Testing Security & Member Card Module
    print("\n[2] Generating Member Card & Verifying Security Key...")
    card_id = security_utils.generate_member_card_id(prefix="VIT")
    test_key = 10007
    is_prime = security_utils.check_if_prime(test_key)
    print(f"    Generated Card ID : {card_id}")
    print(f"    Security Key {test_key} Prime Status : {is_prime}")

    # Step 3: Test Book Filterring
    print("\n[3] Filtering Catalog for 'CS' Books...")
    cs_books = library_core.filter_books_by_category(catalog_dict, "CS")
    for book in cs_books:
        print(f"    - ISBN: {book[0]} | Title: {book[1]} | Author: {book[2]}")

    # Step 4: Run Performance Benchmark test
    print("\n[4] Running Algorithm Efficiency Test (10,000 Records, 500 Queries)...")
    list_time, dict_time, matched = benchmark_engine.run_search_performance_test(
        record_count=10000, queries_count=500)

    print(f" List Linear Search Time : {list_time:.6f} seconds")
    print(f"   Dictionary Lookup Time  : {dict_time:.6f} seconds")
    print(f" Results Match Verified  : {matched}")
    if dict_time > 0:
        print(f"Performance Improvement : Dictionary is ~{list_time / dict_time:.2f}x faster")

    print("\n" + "=" * 65)
    print(" Execution Completed Successfully.")
    print("=" * 65)


if __name__ == "__main__":
    main()