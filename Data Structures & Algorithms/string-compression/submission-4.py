class Solution:
    def compress(self, chars: List[str]) -> int:
        # Objective: change in-place of chars array with repeating elements
        # Return: first k elements of the compressed string
        
        # pointer k that stays at the first of the repeating character
        # pointer r that iterate through until we find char != repeating char
        # pointer k increments then assigns length of group's length into string
        n = len(chars)
        write = 0      # where to write compressed chars
        count = 1      # length of current run

        # We start from index 1 and go up to n (inclusive via n+1)
        for i in range(1, n + 1):
            # If still inside array and same char as previous, extend the run
            if i < n and chars[i] == chars[i - 1]:
                count += 1
            else:
                # Run ended at index i-1. Write the char.
                chars[write] = chars[i - 1]
                write += 1

                # If run length > 1, write its digits.
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                # Reset count for the next run
                count = 1

        return write