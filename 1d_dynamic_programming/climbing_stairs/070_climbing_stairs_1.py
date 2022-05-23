class Solution:
    def climbStairs(self, n: int) -> int:
        # Each number of combininations in `ways` is the sum of the combinations
        # of all step patterns that add to the number.

        # Dict to list of lists, storing all the combinations (ways) to step
        ways = {
            1: [ [1] ],
            2: [ [1,1],  [2] ],
        }

        # Early exit if n already present
        if n in ways:
            return len(ways[n])

        # For every number above 2, attempt to:
        # - append 1 to left and right of each step pattern (way) for `number - 1`
        # - appent 2 to left and right of each step pattern (way) for `number - 2`
        # And add it to the set.
        for number in range(3, n + 1):
            current_ways = set()
            minus_1 = ways[number - 1]
            for way in minus_1:
                # Need to use tuples for set insertion as lists are not hashable
                left_way = [1] + way
                right_way = way + [1]
                current_ways.add(tuple(left_way))
                current_ways.add(tuple(right_way))

            minus_2 = ways[number - 2]
            for way in minus_2:
                # Need to use tuples for set insertion as lists are not hashable
                left_way = [2] + way
                right_way = way + [2]
                current_ways.add(tuple(left_way))
                current_ways.add(tuple(right_way))

            # Add new step pattern to ways as a *list*
            ways[number] = [list(w) for w in current_ways]

        # Sum all the unique step patterns (ways) for the given number
        return len(ways[n])
    