class Solution:
    def compress(self, chars: List[str]) -> int:
        # Objective: change in-place of chars array with repeating elements
        # Return: first k elements of the compressed string
        
        # pointer k that stays at the first of the repeating character
        # pointer r that iterate through until we find char != repeating char
        # pointer k increments then assigns length of group's length into string
        # n = len(chars)
        # count = 1
        # k = 0

        # for i in range(1, n+1):
        #     if i < n and chars[i] == chars[i-1]:
        #         count += 1
        #     else:
        #         chars[k] = chars[i-1]
        #         k += 1
        #         if count > 1:
        #             for digit in str(count):
        #                 print(k, digit)
        #                 chars[k] = digit
        #                 k += 1
        #             count = 1
        # return k
        read, write, start = 0, 0, 0
        n = len(chars)
        while read < n:
            start = read
            curr = chars[read]
            while read < n and chars[read] == curr:
                read += 1
            chars[write] = curr
            write += 1
            length = read - start
            if length > 1:
                for digit in str(length):
                    chars[write] = digit
                    write += 1
        return write