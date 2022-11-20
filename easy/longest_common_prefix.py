class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''
        for prefix_index in range(0, len(strs[0])):
            for index, s in enumerate(strs):
                if index == 0:
                    result += s[prefix_index]
                else:
                    if prefix_index < len(s) and s[prefix_index] != result[-1]:
                        return result[:len(result) - 1]
                    elif prefix_index >= len(s):
                        return result[:len(result) - 1]
        
        return result
