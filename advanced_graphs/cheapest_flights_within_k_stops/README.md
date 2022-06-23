# Cheapest Flights Within K Stops ([LC787](https://leetcode.com/problems/cheapest-flights-within-k-stops/))
Difficulty: Medium

## Problem

There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `fromi` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return the ***cheapest price*** from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

Constraints:
- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from_i, to_i < n`
- `fromi != to_i`
- `1 <= price_i <= 10⁴`
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## Thought Process

Edge Cases / Caveats / Pitfalls:

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:  ms, MB (%, %)
