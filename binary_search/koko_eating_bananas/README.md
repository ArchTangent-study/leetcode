# Koko Eating Bananas ([LC875](https://leetcode.com/problems/koko-eating-bananas/))
Difficulty: **Medium**

## Problem

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

*Return the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

Constraints:
- `1 <= piles.length <= 10⁴`
- `piles.length <= h <= 10⁹`
- `1 <= piles[i] <= 10⁹`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Properly counting multiple eating sessions (e.g. `11` bananas with `k` of `3`)
- Overeating a given `pile`

## Procedure

### Method 1: Binary Search w/Minimization

Key Ideas:
1. Mininum eat rate is `1`, maximum is the largest pile
2. It's a *guessing game* to find the lowest *valid* eat rate -> *binary search* is the best choice.

Big Picture:
1. `L, M, R = left, middle, right` pointers
    - `L = 1`(min amount of bananas possible to eat)
    - `R = max(piles)` (largest pile in piles)
2. Perform below steps while `L <= R`:
3. `k = M = (L+R) // 2` (amount of bananas to eat per hour)
4. Count number of `hours_to_eat` each `pile` in `piles`
5. If `hours_to_eat <= h`:
    - update `answer` with `k` and look for better one (slower eat rate)
    - `R = M - 1`
6. If `hours_to_eat > h`:
    - need to eat more
    - `L = M + 1`
7. At the end, return `answer`

Complexity:
- Time: split the problem space in half each time -> `O(log n)`
- Space: constant extra space required -> `O(1)`

## Results (Python 3)

**Method 1**: 622 ms, 15.6 MB (64.27%, 23.95%)
