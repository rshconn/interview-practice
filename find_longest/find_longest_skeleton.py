# Given a lowercase string s, find the length of the longest substring that does not contain any vowels.

# Example
# Input: s = 'helloworld'
# Output: 3

def find_longest(s: str) -> int:
  # For every character in s:
    # If the current character is a vowel, then update the value of count to 0. 
    # Else, increment the value of the count by 1.
    # Update the value of maximum substring length to the maximum of res and count.
  #Return the maximum substring length.
