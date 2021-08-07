from wallApp.config.mysqlDB import connect

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.creatorId = data['creatorId']
        self.recipientId = data['recipientId']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM messages;'
        allMessages = connect('flaskWall').query_db(query)
        return allMessages

    @classmethod
    def save(cls, data):
        query = 'Insert INTO messages (content, creatorId, recipientId, createdAt) VALUES(%(c)s, %(ci)s, %(ri)s, NOW());'
        messageId = connect('flaskWall').query_db(query, data)
        return messageId

    @classmethod
    def findByUserId(cls, data):
        query = 'SELECT * FROM messages m JOIN users u ON m.creatorId = u.id WHERE recipientId = %(i)s;'
        theseMessages = connect('flaskWall').query_db(query, data)
        return theseMessages

    @classmethod
    def findById(cls, data):
        query = 'SELECT * FROM messages WHERE id = %(i)s;'
        thisMessage = connect('flaskWall').query_db(query, data)
        return cls(thisMessage[0])

    @classmethod
    def deleteById(cls, data):
        query = 'DELETE FROM messages WHERE id = %(i)s;'
        connect('flaskWall').query_db(query, data)

    @classmethod
    def sentMessagesCount(cls, data):
        query = 'SELECT COUNT(id) FROM messages WHERE creatorId = %(i)s;'
        count = connect('flaskWall').query_db(query, data)
        val = 0
        for c in count:
            for v in c:
                val = c[v]
        return val

    @classmethod
    def recievedMessageCount(cls, data):
        query = 'SELECT COUNT(id) FROM messages WHERE recipientId = %(i)s;'
        count = connect('flaskWall').query_db(query, data)
        val = 0
        for c in count:
            for v in c:
                val = c[v]
        return val