from json import dumps
from random import randint

class Repository:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
        self.available_topics = ['bash', 'git', 'python', 'vim']


    def random(self, topic):
        if not topic in self.available_topics: return [5]
        res = [('','')]
        try:
            sql1 = f'SELECT MAX(id) FROM ' + topic
            self.__cur.execute(sql1)
            max_id = self.__cur.fetchone()[0]
            new_id = randint(1, max_id)
            sql2 = "SELECT name, description FROM " + topic + " WHERE id = ?"
            self.__cur.execute(sql2, (new_id,))
            raw_res = self.__cur.fetchone()
            res = self._map(raw_res)
        except Exception as e:
            print(e)
            pass
        return res


    def cheatsheet(self, topic):
        if not topic in self.available_topics: return []
        res = []
        try:
            sql1 = f'SELECT name, description FROM ' + topic
            self.__cur.execute(sql1)
            raw_res = self.__cur.fetchall()
            res = [self._map(i) for i in raw_res]
        except Exception as e:
            print(e)
            pass
        return res

    def _map(self, data):
        name, description = data
        name = "" if name is None else name
        description = "" if description is None else description
        item = { 'command': name, 'description': description }
        return item