from friendsApp.config.mysqlDB import connect

class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.userId = data['userId']
        self.friendId = data['friendId']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM friendships;'
        allfriends = connect('friends').query_db(query)
        friends = []
        for u in allfriends:
            friends.append(cls(u))
        return friends

    @classmethod
    def save(cls, data):
        query = 'Insert INTO friendships (userId, friendId, createdAt) VALUES(%(ui)s, %(fi)s, NOW());'
        newFriends = connect('friends').query_db(query, data)
        return newFriends