from typing import List

class Twitter:
    """Simple version with [(userId, tweetId)] tweet list."""

    def __init__(self):
        # Dictionary of {follower: set(followed)}
        self.followed = {}
        # List of (userId, tweetId) pairs
        self.tweets = []        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Composes a new tweet with ID tweetId by the user userId. 

        Each call to this function will be made with a unique tweetId.
        """
        self.tweets.append((userId, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """Retrieves the 10 most recent tweet IDs in the user's news feed.
        
        Each item  in the news feed must be posted by users who the user followed or 
        by the user themself. Tweets must be ordered from most recent to least recent.
        """
        feed = []
        count = 0

        for uid, tid in reversed(self.tweets):
            if uid == userId or uid in self.followed.get(userId, ()):
                feed.append(tid)
                count += 1
                if count == 10:
                    break

        return feed
      
    def follow(self, followerId: int, followeeId: int) -> None:
        """Add followed ID to follower ID's followed list."""
        if followerId in self.followed:
            self.followed[followerId].add(followeeId)
        else:
            self.followed[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Removes followed ID from follower ID's followed list."""
        if followerId in self.followed and followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)
