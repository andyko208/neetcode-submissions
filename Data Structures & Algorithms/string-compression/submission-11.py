class Solution:
    def compress(self, chars: List[str]) -> int:
        # Objective: change in-place of chars array with repeating elements
        # Return: first k elements of the compressed string
        
        # pointer k that stays at the first of the repeating character
        # pointer r that iterate through until we find char != repeating char
        # pointer k increments then assigns length of group's length into string
        n = len(chars)
        k = i = 0

        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1

            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1
            i = j
        return k
        # read, write, start = 0, 0, 0
        # n = len(chars)
        # while read < n:
        #     start = read
        #     curr = chars[read]
        #     while read < n and chars[read] == curr:
        #         read += 1
        #     chars[write] = curr
        #     write += 1
        #     length = read - start
        #     if length > 1:
        #         for digit in str(length):
        #             chars[write] = digit
        #             write += 1
        # return write