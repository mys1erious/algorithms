from collections import defaultdict
from typing import List
import heapq


# My solution
# class User:
#     def __init__(self, id):
#         self.id = id
#         self.followed_users: dict[int, User] = {}
#
#     def __str__(self):
#         return str(self.id)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Tweet:
#     def __init__(self, user_id, tweet_id):
#         self.user_id = user_id
#         self.tweet_id = tweet_id
#
#     def __str__(self):
#         return str(self.tweet_id)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# # M: t+u+f
# class Twitter:
#     NEWS_FEED_LEN = 10
#
#     def __init__(self):
#         self.tweets: list[Tweet] = []
#         self.users: dict[int, User] = {}
#
#     def postTweet(self, userId: int, tweetId: int) -> None:
#         self._add_user_if_not_exists(userId)
#         self.tweets.append(Tweet(userId, tweetId))
#
#     # T: (t)
#     def getNewsFeed(self, userId: int) -> List[int]:
#         self._add_user_if_not_exists(userId)
#
#         cur_len = 0
#         tweets = []
#
#         for i in range(len(self.tweets)-1, -1, -1):
#             if cur_len == self.NEWS_FEED_LEN:
#                 break
#
#             if self.tweets[i].user_id == userId or self.users.get(userId).followed_users.get(self.tweets[i].user_id):
#                 tweets.append(self.tweets[i].tweet_id)
#                 cur_len+=1
#
#         return tweets
#
#     def follow(self, followerId: int, followeeId: int) -> None:
#         self._add_user_if_not_exists(followerId)
#         self._add_user_if_not_exists(followeeId)
#
#         self.users[followerId].followed_users[followeeId] = self.users[followeeId]
#
#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         self._add_user_if_not_exists(followerId)
#         self._add_user_if_not_exists(followeeId)
#
#         self.users[followerId].followed_users.pop(followeeId, None)
#
#     def _add_user_if_not_exists(self, user_id):
#         if not self.users.get(user_id):
#             self.users[user_id] = User(user_id)
#
#     def __str__(self):
#         return f'Tweets: {self.tweets}; Users: {self.users}'
#
#     def __repr__(self):
#         return self.__str__()


class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId not in self.tweetMap:
                continue
            index = len(self.tweetMap[followeeId])-1
            count, tweetId = self.tweetMap[followeeId][index]
            minHeap.append([count, tweetId, followeeId, index-1])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index < 0: continue
            count, tweetId = self.tweetMap[followeeId][index]
            heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)  # User 1 posts a new tweet (id = 5).
    twitter.getNewsFeed(1)  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2)  # User 1 follows user 2.
    twitter.postTweet(2, 6)  # User 2 posts a new tweet(id=6).
    twitter.getNewsFeed(1)  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2)  # User 1 unfollows user 2.
    twitter.getNewsFeed(1)  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
