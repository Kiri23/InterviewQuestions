''' 
Problem: String permuations 
Description:

Generate all possible permutations of a given string using recursion.
Example: "abc" -> ["abc", "acb", "bac", "bca", "cab", "cba"]

Key takeways: This example show how to mantain state betwen recursion call, 
then having a base case to construct the final state. 

Two Different Approaches Shown:
   a) Forward approach (demonstrate_concept):
      - Picks first character and builds forward
      - Maintains state with 'current' parameter
   
   b) Backward approach (get_permutations):
      - Takes last character and works backwards
      - Inserts last char in all possible positions
Usage:
str = 'abc'
permutations = demonstrate_concept(str)  # Returns ['abc', 'acb', 'bac', ...]
'''


def demonstrate_concept(str, current='', per=[]):
    if len(str) == 1:
        print(f"Reach the end. The permutation is -> {current + str}")
        per.append(current + str)
    for i in range(len(str)):
        first_char = str[i]
        remaining_chars = str[:i] + str[i+1:]
        demonstrate_concept(remaining_chars, current + first_char, per)
    return per


str = 'abc'
per = demonstrate_concept(str)
print(f" # ofpermutation: {len(per)},for string {str} lenght:{len(str)}")


# Solution given by parker from interview cake , take out the last character and do the permuations with all the words
# execpt the last one
def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(
        all_chars_except_last)

    # Put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutation_of_all_chars_except_last[:position]
                + last_char
                + permutation_of_all_chars_except_last[position:]
            )
            permutations.add(permutation)

    return permutations


# get_permutations(str)
