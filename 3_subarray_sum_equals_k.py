def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    freq = {0: 1}
    for num in nums:
        prefix_sum += num
        count += freq.get(prefix_sum - k, 0)
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count

# Test Cases
print("Test 1:", subarraySum([1,1,1], 2))   # Expected: 2
print("Test 2:", subarraySum([1,2,3], 3))   # Expected: 2
