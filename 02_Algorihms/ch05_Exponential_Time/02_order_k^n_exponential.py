def letter_combinations(digits):
    """
    Returns all possible letter combinations for a given string of digits.
    """
    if not digits:
        return []
    
    result = [""]

    for digit in digits:
        if digit not in digit_to_letters:
            raise ValueError(f"invalid digit: {digit}")
        
        letters = digit_to_letters[digit]
        new_result = []
        for combo in result:
            for letter in letters:
                new_result.append(combo+letter)
        result = new_result
    return result    
        
# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


# input; output length; first three output strings; a string that should be present
TestCase = tuple[str, int, list[str], str]

run_cases: list[TestCase] = [
    ("", 0, [], ""),
    ("67", 12, ["mp", "mq", "mr"], "op"),
    ("43556", 243, ["gdjjm", "gdjjn", "gdjjo"], "hello"),
    ("2668338", 2187, ["ammtddt", "ammtddu", "ammtddv"], "bootdev"),
]

submit_cases: list[TestCase] = run_cases + [
    ("420", 0, [], "ValueError"),
    ("7878326", 3888, ["ptptdam", "ptptdan", "ptptdao"], "rustfan"),
    ("4568346", 2187, ["gjmtdgm", "gjmtdgn", "gjmtdgo"], "ilovego"),
]


def test(
    digits: str,
    expected_length: int,
    expected_initial: list[str],
    expected_contains: str,
) -> bool:
    print("---------------------------------")
    print(f"Input: '{digits}'")
    try:
        result = letter_combinations(digits)
        print(f"Expected combos: {expected_length}")
        actual_length = len(result)
        print(f"Actual combos:   {actual_length}")
        if expected_length == 0 and actual_length == expected_length:
            print("Pass")
            return True
        print(f"Expected initial combos: {expected_initial}")
        actual_initial = result[:3]
        print(f"Actual initial combos:   {actual_initial}")
        print(f"Expected to contain: '{expected_contains}'")
        actual_contains = expected_contains in result
        print(f"Actual contains '{expected_contains}'? {actual_contains}")
        if (
            actual_length == expected_length
            and actual_initial == expected_initial
            and actual_contains
        ):
            print("Pass")
            return True
    except ValueError as ve:
        print(f"Caught ValueError: {ve}")
        if expected_length == 0 and expected_contains == "ValueError":
            print("Expected ValueError")
            print("Pass")
            return True
    print("Fail")
    return False


def main() -> None:
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


test_cases: list[TestCase] = submit_cases

if __name__ == "__main__":
    main()