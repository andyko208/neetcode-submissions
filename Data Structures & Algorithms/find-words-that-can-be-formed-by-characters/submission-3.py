class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # turn chars into a counter of hashmap
        char_map = Counter(chars)
        # keep the length
        sum_len = 0
        # iterate through word in words
        for word in words:
            # turn word in a counter hashmap and check if chars have enough of it
            word_counter = Counter(word)
            # helper vars to check validity
            # tmp_map = char_map
            valid_chars = 0
            flag = True
            # iterate through each char to check validity
            for char, count in word_counter.items():
                # valid char should remain ratio >= 1
                # if char_map[char] // count >= 1:
                if char_map[char] < count:
                    # valid_chars += 1
                    flag = False
                    break
            # good string if valid_chars == len(word)
            # print(word, valid_chars)
            # if valid_chars == len(word_counter):
            if flag:
                sum_len += len(word)
        return sum_len


            
            