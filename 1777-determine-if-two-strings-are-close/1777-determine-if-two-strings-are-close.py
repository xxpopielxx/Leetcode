class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1
        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        # sprawdzanie tych samych liter
        for i in range(26):
            if (freq1[i] == 0) != (freq2[i] == 0):
                return False

        # tablice zliczające częstotliwości częstotliwości
        n = len(word1)
        count_freq1 = [0] * (n + 1)
        count_freq2 = [0] * (n + 1)

        for f in freq1:
            if f > 0:
                count_freq1[f] += 1
        for f in freq2:
            if f > 0:
                count_freq2[f] += 1

        return count_freq1 == count_freq2