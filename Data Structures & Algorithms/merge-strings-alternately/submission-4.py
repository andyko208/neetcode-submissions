class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # # two pointers w1, w2
        # w1, w2 = 0, 0
        # # final string word
        # word = ""
        # # iterate through until both reaches the end for each
        # while w1 < len(word1) or w2 < len(word2):
        #     # need to check which word's turn is it to append by len(word)
        #     if len(word) % 2 == 0:
        #         # only append to word if pointer for each is at a valid position
        #         if w1 < len(word1):
        #             word += word1[w1]
        #             w1 += 1
        #         # implies that w2 is longer, so append all at once
        #         else:
        #             # if w2 < len(word2):
        #             #     word += word2[w2]
        #             #     w2 += 1
        #             word += word2[w2:]
        #             w2 += len(word2) - w2
                    
        #     else:
        #         if w2 < len(word2):
        #             word += word2[w2]
        #             w2 += 1
        #         else:
        #             # if w1 < len(word1):
        #             #     word += word1[w1]
        #             #     w1 += 1
        #             word += word1[w1:]
        #             w1 += len(word1) - w1
        # return word
        
        w1, w2 = 0, 0
        word = ""
        # iterate until one word is over
        while w1 < len(word1) and w2 < len(word2):
            word += word1[w1]
            word += word2[w2]
            w1, w2 = w1 + 1, w2 + 1
        # append the whole other word if one is over
        word += word1[w1:]
        word += word2[w2:]

        return word

