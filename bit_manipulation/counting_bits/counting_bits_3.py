# type: ignore
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Pre-allocate to size n+1, since size is always known
        answer = [0]*(n + 1)
        # Current and next index shifts
        index_shift = 1
        next_shift = 2

        # Start at 1 since value at 0 is always guaranteed at index 0 by constraints
        for i in range(1, n + 1):
            if i == next_shift:
                index_shift *= 2
                next_shift *= 2

            count = answer[i - index_shift] + 1
            answer[i] = count

        return answer
    