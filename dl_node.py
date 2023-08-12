from uid_generator import UIDGenerator


class DLNode:
    def __init__(self, data):
        self.__id = UIDGenerator.generate_id()
        self.__popularity = 0
        self.data = data
        self.next = None
        self.previous = None

    def get_id(self):
        return self.__id

    def get_popularity(self):
        return self.__popularity

    def record_access(self):
        self.__popularity += 1
