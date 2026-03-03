def last_work_experience(work_experiences):
    """Returns the last work experience from the list or None if empty in O(1) time."""
    return work_experiences[-1] if work_experiences else None


run_cases = [
    (["Software Engineer", "Data Analyst", "Project Manager"], "Project Manager"),
    (["Intern", "Junior Developer"], "Junior Developer"),
]

submit_cases = run_cases + [
    ([], None),
    (["CEO"], "CEO"),
    (["Cashier", "Supervisor", "Manager", "Director"], "Director"),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input work experiences: {input1}")
    print(f"Expected output: {expected_output}")
    
    original = list(input1)
    result = last_work_experience(input1)
    
    print(f"Actual output: {result}")
    
    if result == expected_output and input1 == original:
        print("Pass")
        return True
        
    print("Fail")
    return False


def main():
    test_cases = submit_cases 
    
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1 
            
    print("\n========= Test Summary =========")
    print(f"Total: {len(test_cases)}, Passed: {passed}, Failed: {failed}, Skipped: {skipped}")

if __name__ == "__main__":
    main()