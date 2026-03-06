class Trie:
    def exists(self, word):
        """Checks if a complete word exists in the trie by traversing character nodes and verifying the end symbol."""
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return self.end_symbol in current

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"



import json

run_cases = [
    (["dev", "devops", "devs", "designer"], "devops", True),
    (["manager", "qa", "dev", "intern"], "ceo", False),
    (["engineer", "developer", "janitor"], "dev", False),
]

submit_cases = run_cases + [
    (
        ["dev", "developer", "devops", "manager"],
        "hr",
        False,
    ),
    (["qa", "qaops", "qam"], "qaops", True),
]


def test(words, word_to_check, expected_output):
    print("---------------------------------")
    trie = Trie()
    for word in words:
        trie.add(word)
    print("Trie:")
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f'Checking if "{word_to_check}" exists:')
    print(f"Expected: {expected_output}")
    try:
        actual = trie.exists(word_to_check)
        print(f"Actual:   {actual}")
        if actual == expected_output:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
