class Database():

    def __init__(self):

        self.storage = {}

    def create_subbase(self, id, location=""):

        location = location.split("/")
        while "" in location: 
            location = location.remove("")
            if location == None: location = [] 

        assert type(id) == type(str()) and not "/" in id
        if len(location) == 0:
            self.storage[id] = Subbase()
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_subbase(id, location)

    def create_table(self, id, labels, location=""):

        location = location.split("/")
        while "" in location: 
            location = location.remove("")
            if location == None: location = [] 

        assert type(id) == type(str()) and not "/" in id
        if len(location) == 0:
            self.storage[id] = Table(labels)
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_subbase(id, labels, location)

    def create_datapoint(self, id, labels, location=""):

        location = location.split("/")
        while "" in location: 
            location = location.remove("")
            if location == None: location = [] 

        assert type(id) == type(str()) and not "/" in id
        if len(location) == 0:
            self.storage[id] = Datapoint(labels)
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_datapoint(id, labels, location)


class Subbase():

    def __init__(self):

        self.storage = {}

    def create_subbase(self, id, location):

        if len(location) == 0:
            self.storage[id] = Subbase()
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_subbase(id, location)

    def create_table(self, id, labels):

        self.storage[id] = Table(labels)

    def create_datapoint(self, id, labels):

        self.storage[id] = Datapoint(labels)


class Table():

    def __init__(self, labels):

        self.labels = labels
        self.storage = []


class Datapoint():

    def __init__(self, labels):

        self.storage = {}
        for label in labels:
            self.storage[label] = None