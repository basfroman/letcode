class InMemoryDB:

    def __init__(self):
        self._db = {}

    def execute(self, query):
        command = query[0]
        key = query[1]
        field = query[2]

        if command == 'SET_OR_INC':
            value = query[3]
            return self.set_or_inc(key, field, value)

        elif command == 'GET':
            return self.get(key, field)

        elif command == 'DELETE':
            return self.delete(key, field)

        else:
            return ''

    def set_or_inc(self, key, field, value):
        if not self._db.get(key):
            self._db[key] = {field: value}
        else:
            if not self._db[key].get(value):
                self._db[key][field] = value
            else:
                self._db[key][field] += value
        return self._db[key][field]

    def get(self, key, field):
        if key in self._db and field in self._db[key]:
            return self._db[key][field]
        else:
            return ''

    def delete(self, key, field):
        if key in self._db and field in self._db[key]:
            del self._db[key][field]
            if not self._db[key]:
                del self._db[key]
            return "true"
        else:
            return "false"


def solution(queries):
    db = InMemoryDB()
    result = [db.execute(query) for query in queries]
    print(db._db)
    return result

q = [["GET","dept4","floors"],
 ["GET","dept4","floors"],
 ["SET_OR_INC","dept4","floors","22"],
 ["GET","dept4","floors"],
 ["GET","dept4","floors"],
 ["SET_OR_INC","dept4","floors","4"],
 ["GET","dept4","floors"],
 ["SET_OR_INC","dept4","floors","10"],
 ["GET","dept4","floors"]]
print(solution(q))