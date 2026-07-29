class Solution:
    def compress(self, chars: List[str]) -> int:
        # Objective: change in-place of chars array with repeating elements
        # Return: first k elements of the compressed string
        
        # pointer k that stays at the first of the repeating character
        # pointer r that iterate through until we find char != repeating char
        # pointer k increments then assigns length of group's length into string
        read = write = 0

        n = len(chars)
        while read < n:
            start = read
            curr_char = chars[read]
            # Move read to the end of this run of current_char
            while read < n and chars[read] == curr_char:
                read += 1
            # Write the character itself
            chars[write] = curr_char
            write += 1
            run_length = read - start
            if run_length > 1:
                for digit in str(run_length):
                    chars[write] = digit
                    write += 1
        return write



        