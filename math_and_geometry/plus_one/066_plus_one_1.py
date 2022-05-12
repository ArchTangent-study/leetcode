# type: ignore
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = []
        carry = 1

        for digit in reversed(digits):
            if carry == 1:
                if digit == 9:
                    answer.append(0)
                    carry = 1
                else:
                    answer.append(digit + 1)
                    carry = 0
            else:
                answer.append(digit)

        if carry == 1:
            answer.append(1)

        answer.reverse()
        
        return answer
    