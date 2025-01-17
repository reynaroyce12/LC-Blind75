from collections import Counter, defaultdict

# Approach 1. Using Counter
class Solution_1(object):
    def groupAnagrams(self, strs):
        anagrams_dict = {}

        for word in strs:
            character_frequency = tuple(sorted(Counter(word).items()))

            if character_frequency in anagrams_dict:
                anagrams_dict[character_frequency].append(word)
            else:
                anagrams_dict[character_frequency] = [word]

        return list(anagrams_dict.values())


# Approach 2. Using fixed size Arrays as Keys
class Solution_2(object):
    def groupAnagrams(self, strs):
        anagrams_dict = defaultdict(list)

        for word in strs:
            frequency_list = [0] * 26

            for character in word:
                frequency_list[ord(character) - ord('a')] += 1

            key = tuple(frequency_list)
            anagrams_dict[key].append(word)

        return list(anagrams_dict.values())
            