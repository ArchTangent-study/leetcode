# type: ignore
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Most common scenario: least siginificant digit is < 9
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        # Remaining case: least significant digit == 9
        answer = [0]
        carry = 1

        # start from 2nd to last digit, iterating in reverse
        for digit in digits[-2::-1]:
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

        # Reverse answer
        answer.reverse()
        return answer
        