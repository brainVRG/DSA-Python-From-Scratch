def summed(nums):
    """
    Calculates the total sum of a list of numbers.
    """
    total = 0  # 내장 함수 sum()과의 이름 충돌을 피하기 위해 total 사용
    for num in nums:
        total += num
    return total