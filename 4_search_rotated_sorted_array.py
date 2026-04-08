def searchRotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Test Cases
print("Test 1:", searchRotated([4,5,6,7,0,1,2], 0))   # Expected: 4
print("Test 2:", searchRotated([4,5,6,7,0,1,2], 3))   # Expected: -1
print("Test 3:", searchRotated([1], 0))                # Expected: -1
