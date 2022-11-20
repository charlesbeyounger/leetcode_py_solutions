class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        half = len(x_str) // 2
        head = 0
        tail = head - 1

        while head <= half:
            if x_str[head] != x_str[tail]:
                return False

            head += 1
            tail -= 1
            
        return True