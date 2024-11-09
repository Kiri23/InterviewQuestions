from collections import defaultdict
# group anagram letcode https://leetcode.com/problems/group-anagrams/description/

'''
Problem: Group Anagrams
Description:
- Given an array of strings strs, group the anagrams together and return them in any order
- Anagrams are strings that have the same characters in different orders
- All inputs are lowercase English letters

Example:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Approach:
1. Use character count as key to group anagrams
2. Each string gets converted to a 26-length array (a-z count)
3. Strings with same character counts are anagrams

Time Complexity: O(n * k) where n is number of strings, k is max length of a string
Space Complexity: O(n * k) to store all strings in hash map

Example Step by Step: groupAnagrams(["cat", "act"])

1. Initialize:
defaultdict(list) = {}

2. Process first string "cat":
   
   Step 1: Create count array [0] * 26 for a-z
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   
   Step 2: Count each character
   'c' -> index 2  (ord('c') - ord('a') = 2)
   'a' -> index 0  (ord('a') - ord('a') = 0)
   't' -> index 19 (ord('t') - ord('a') = 19)
   
   Final count array for "cat":
   [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                ^     ^                   ^
                a     c                   t

   Step 3: Use this count array as key:
   defaultdict = {
       (1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0): ["cat"]
   }

3. Process second string "act":
   
   Steps 1&2: Create and fill count array
   - Same result because it's an anagram:
   [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
                ^     ^                   ^
                a     c                   t

   Step 3: Same key exists, append to list:
   defaultdict = {
       (1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0): ["cat", "act"]
   }

4. Return values:
[["cat", "act"]]
'''


def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()


result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
