class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        result = 0

        for i in range(len(freq)):
            result += freq[i] * ((i // 8) + 1)

        return result
