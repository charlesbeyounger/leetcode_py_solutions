class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        
        has_trust = []
        trusted_map = {}

        for t_list in trust:
            if t_list[0] not in has_trust:
                has_trust.append(t_list[0])
            
            if t_list[1] not in trusted_map:
                trusted_map[t_list[1]] = 1
            else:
                trusted_map[t_list[1]] += 1

        for trusted in trusted_map:
            if trusted_map[trusted] == n - 1 and trusted not in has_trust:
                return trusted
        
        return -1
