def minWindow(s, t):
    from collections import Counter
    need = Counter(t)
    have, total = 0, len(need)
    window = {}
    result, result_len = [-1, -1], float("inf")
    left = 0
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1
        while have == total:
            if (right - left + 1) < result_len:
                result = [left, right]
                result_len = right - left + 1
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    l, r = result
    return s[l:r+1] if result_len != float("inf") else ""

# Test Cases
print("Test 1:", minWindow("ADOBECODEBANC", "ABC"))   # Expected: "BANC"
print("Test 2:", minWindow("a", "a"))                  # Expected: "a"
print("Test 3:", minWindow("a", "aa"))                 # Expected: ""
