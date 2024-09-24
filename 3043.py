class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        res = 0
        arr1Prefixes = set()

        for number in arr1:
            str1 = str(number)

            for i in range(1, len(str1) + 1):
                arr1Prefixes.add(str1[:i])

        for number in arr2:
            str1 = str(number)

            for i in range(1, len(str1) + 1):
                prefix = str1[:i]

                if prefix in arr1Prefixes:
                    res = max(res, len(prefix))

        return res
