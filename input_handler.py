def get_input():
    num_instances = int(input("Enter number of test cases: "))
    test_cases = []
    for _ in range(num_instances):
        k = int(input("Enter cache size: "))
        n = int(input("Enter number of app requests: "))
        requests = list(map(int, input("Enter app requests: ").split()))
        test_cases.append((k, requests))
    return test_cases
