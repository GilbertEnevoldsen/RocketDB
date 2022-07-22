class Database():

    def __init__(self):

        self.storage = {}

    def create_subbase(self, id):

        assert type(id) == type(str())
        self.storage[id] = Subbase()

    def create_tabel(self, id, labels):

        assert type(id) == type(str())
        self.storage[id] = Tabel(labels)

    def create_datapoint(self, id, labels):

        assert type(id) == type(str())
        self.storage[id] = Datapoint(labels)


class Subbase():

    def __init__(self):

        self.storage = {}

    def create_subbase(self, id):

        assert type(id) == type(str())
        self.storage[id] = Subbase()


class Tabel():

    def __init__(self, labels):

        self.labels = labels
        self.storage = []


class Datapoint():

    def __init__(self, labels):

        self.storage = {}
        for label in labels:
            self.storage[label] = None