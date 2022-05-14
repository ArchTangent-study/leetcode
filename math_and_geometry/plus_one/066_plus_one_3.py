# type: ignore
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Answer will have length of len(digits) OR len(digits) + 1
        answer = [0] * len(digits)
        carry = 1

        # Current digit index
        i = -1
        # Iterate in reverse
        for digit in digits[::-1]:
            match (digit < 9, carry):
                # Cases where digit < 9 (most common)
                case True, 0:
                    answer[i] = digit
                    carry = 0
                case True, 1:
                    answer[i] = digit + 1
                    carry = 0
                # Cases where digit == 9
                case False, 0:
                    answer[i] = digit
                    carry = 0
                # Note: this step can be removed because when digit = 9 and carry = 1:
                # answer[i] is already 0 and carry is already 1
                case False, 1:
                    answer[i] = 0
                    carry = 1
            # Decrement digit index, since moving in reverse
            i -=1

        # Return answer or add extra 1 depending on final carry value
        if carry == 0:
            return answer
        else:
            return [1] + answer
    