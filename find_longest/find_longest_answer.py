# Given a lowercase string s, find the length of the longest substring that does not contain any vowels.

# Example
# Input: s = 'helloworld'
# Output: 3

def find_longest(s):
 	max = 0
 	char_count = 0
  
  # For every character in s:
 	for char in s:

    # If the current character is a vowel, then update the value of count to 0. 
		if char in ['a', 'e', 'i', 'o', 'u']:
			char_count = 0

    # Else, increment the value of the count by 1.
		else:
			char_count += 1

    # Update the value of maximum substring length to the maximum of res and count.
		max = max(max, char_count)

  # Return the maximum substring length.
	return maximum

