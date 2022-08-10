# Design Twitter ([LC355](https://leetcode.com/problems/design-twitter/))
Difficulty: **Medium**

## Problem

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.

Implement the `Twitter` class:
- `Twitter()` Initializes your twitter object.
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique `tweetId`.
- `List<Integer> getNewsFeed(int userId)` Retrieves the `10` most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be **ordered from most recent to least recent**.
- `void follow(int followerId, int followeeId)` The user with ID `followerId` started following the user with ID `followeeId`.
- `void unfollow(int followerId, int followeeId)` The user with ID `followerId` started unfollowing the user with ID `followeeId`.

Constraints:
- `1 <= userId, followerId, followeeId <= 500`
- `0 <= tweetId <= 10⁴`
- All the tweets have unique IDs.
- At most `3 * 10⁴` calls will be made to `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.

## Thought Process

Questions:
- How to determine timestamps to see which tweets are posted before others?
- Do the `tweetId` values increase with time, e.g. tweet `5` is posted later than `1`?
- Do users follow themselves automatically?
- Can you unfollow yourself? -> NO (as per test cases)
- Are `tweetIds` serialized starting from `0`? -> NO

Edge Cases / Caveats / Pitfalls:
- Determining `10` most recent tweets
- Returning fewer than `10` most recent tweets
- Returning tweets from the user themself

Approaches:
- Since only `500` unique `userID`s are used, a spare list would work (though doesn't scale well).
- Max heap to store tweets by most recent (highest) timestamp.  It's like getting the `k` most recent tweets.
- Intervals:  overlap `lowest, highest` tweets for each followed user.

## Procedure

### Method 1: List of (userId, tweetId) Tweets

Key Idea:  keep it simple with a list of `(userId, tweetId)` pairs, searching in reverse (most recent) to get the news feed, stopping once the count is `10`.  Changes could be made to make the news feed more efficient, but sometimes simple suffices.

Complexity:
- Follow: every user follows all other users -> `O(u²)`
- Unfollow: `O(1)`
- Post Tweet: `O(1)`
- Get News Feed: may have to traverse all tweets to get `10` of them -> `O(n)`
- Space: every user follows every other user, store all tweets -> `O(u² + n)`

Where:
- `n` is number of tweets
- `u` is number of users

## Results (Python 3)

**Method 1**: 35 ms, 14.1 MB (86.13%, 66.07%)
