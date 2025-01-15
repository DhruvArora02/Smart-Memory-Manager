from input_handler import get_input
from paging_algorithm import furthest_in_future_paging

def main():
    test_cases = get_input()
    for k, requests in test_cases:
        page_faults = furthest_in_future_paging(k, requests)
        print(f"Page Faults: {page_faults}")

if __name__ == "__main__":
    main()
