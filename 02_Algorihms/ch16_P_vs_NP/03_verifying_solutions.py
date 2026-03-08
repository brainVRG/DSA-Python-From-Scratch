def get_num_guesses(length):
    """Calculates the total number of possible lowercase letter password combinations up to the given length."""
    total = 0
    for i in range(length):
        total += 26**(i+1)
    return total



run_cases = [
    (1, 26),
    (2, 702),
    (3, 18278),
]

submit_cases = run_cases + [
    (4, 475254),
    (5, 12356630),
    (6, 321272406),
    (7, 8353082582),
    (8, 217180147158),
    (9, 5646683826134),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    result = get_num_guesses(input)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
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
