class HashMap:
    def insert(self, key, value):
        """Inserts a key-value pair using linear probing to resolve collisions."""
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index += 1
            index %= len(self.hashmap)
            first_iteration = False      
        self.hashmap[index] = (key, value)
    

    def get(self, key):
        """Retrieves a value by key using linear probing to handle collisions."""
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")    
            index += 1
            index %= len(self.hashmap)
            first_iteration = False            
        raise Exception("sorry, key not found")    
            
            
            
            
            
    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

run_cases = [
    (
        2,
        [
            ("Billy Beane", "General Manager"),
            ("Peter Brand", "Assistant GM"),
        ],
        [(False, None), (False, None)],
    ),
    (
        3,
        [
            ("Art Howe", "Manager"),
            ("Ron Washington", "Coach"),
            ("David Justice", "Designated Hitter"),
        ],
        [(False, None), (False, None), (False, None)],
    ),
]

submit_cases = run_cases + [
    (
        2,
        [
            ("Paul DePodesta", "Analyst"),
            ("Ron Washington", "Coach"),
            ("Chad Bradford", "Pitcher"),
        ],
        [
            (False, None),
            (False, None),
            (True, "hashmap is full"),
        ],
    )
]


def test(size, items, errors):
    hm = HashMap(size)
    print("=====================================")
    inserted_items = {}
    for (key, val), (error_expected, expected_error_message) in zip(items, errors):
        print(f"Inserting ({key}, {val})...")
        try:
            hm.insert(key, val)
            if error_expected:
                print(
                    f"Expected error '{expected_error_message}' but insertion succeeded."
                )
                print("Fail")
                return False
            else:
                inserted_items[key] = val
        except Exception as e:
            if error_expected:
                if str(e) == expected_error_message:
                    print(f"Expected error occurred: {e}")
                else:
                    print(
                        f"Error occurred, but message '{e}' does not match expected '{expected_error_message}'."
                    )
                    print("Fail")
                    return False
            else:
                print(f"Unexpected error occurred during insertion: {e}")
                print("Fail")
                return False
    for key, expected_val in inserted_items.items():
        print(f"Getting {key}...")
        try:
            actual_val = hm.get(key)
            print(f"Expected: {expected_val}, Actual: {actual_val}")
            if actual_val != expected_val:
                print("Fail")
                return False
        except Exception as e:
            print(f"Error getting {key}: {e}")
            print("Fail")
            return False
    print("Pass")
    return True


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
