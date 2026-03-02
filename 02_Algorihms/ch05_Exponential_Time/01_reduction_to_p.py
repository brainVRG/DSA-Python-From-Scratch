def fib(n):
    """
    Calculates the nth Fibonacci number in O(N) time.
    """
    if n <= 1:
        return n
    
    grandparent = 0
    parent = 1

    for _ in range(n-2):
        current = grandparent + parent
        grandparent, parent = parent, current

    return grandparent + parent


run_cases = [
    (1, 1),
    (10, 55),
    (20, 6765),
]

submit_cases = run_cases + [
    (0, 0),
    (40, 102334155),
    (70, 190392490709135),
    (160, 1226132595394188293000174702095995),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected:  {expected_output}")
    result = fib(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
