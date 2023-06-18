class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, words_to_pr = s.split(' '), dict()

        # check base case
        if len(pattern) != len(words): 
            return False
        # now check unique
        if len(set(pattern)) != len(set(words)):
            return False

        # now check
        for i in range(len(words)):
            # if not present put into dict
            if words[i] not in words_to_pr:
                words_to_pr[words[i]] = pattern[i]
            # if found check is it match with patter
            elif words_to_pr[words[i]] != pattern[i]:
                return False

        return True