def process_location(location):

    location = location.split("/")
    while "" in location: 
        location = location.remove("")
        if location == None: location = [] 

    return location

class Database():

    def __init__(self):

        self.storage = {}

    def create_subbase(self, id, location=""):

        location = process_location(location)

        assert type(id) == type(str()) and not "/" in id
        if len(location) == 0:
            self.storage[id] = Subbase()
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_subbase(id, location)

    def create_table(self, id, fields, location=""):

        location = process_location(location) 

        assert type(id) == type(str()) and not "/" in id
        if len(location) == 0:
            self.storage[id] = Table(fields)
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_table(id, fields, location)

    def create_datapoint(self, id, fields, location=""):

        location = process_location(location)

        assert type(id) == type(str()) and not "/" in id
        if len(location) == 0:
            self.storage[id] = Datapoint(fields)
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_datapoint(id, fields, location)

    def get_fields(self, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot get fields from type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            return self.storage[immediate_location].get_fields(location)

    def create_field(self, name, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot create field in type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_field(name, location)

    def rename_field(self, field, name, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot rename field from type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].rename_field(field, name, location)

    def delete_field(self, field, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot delete field from type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].delete_field(field, location)

    def insert(self, record, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot insert to type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].insert(record, location)

    def get(self, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot get from type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            return self.storage[immediate_location].get(location)

    def get_where(self, match, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot get from type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            return self.storage[immediate_location].get_where(match, location)

    def write(self, data, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot write to type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].write(data, location)

    def write_where(self, match, data, location):

        location = process_location(location)

        if len(location) == 0:
            raise ValueError("Cannot write to type 'Database'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].write_where(match, data, location)

    def delete(self, location):

        location = process_location(location)

        if len(location) == 0:
            self.storage = []
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].delete(location)

    def delete_where(self, location, id="", match={}):

        location = process_location(location)

        if len(location) == 0:
            self.storage.pop(id)
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].delete_where(match, location)


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

    def create_table(self, id, fields, location):

        if len(location) == 0:
            self.storage[id] = Table(fields)
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_table(id, fields, location)

    def create_datapoint(self, id, fields):

        self.storage[id] = Datapoint(fields)

    def get_fields(self, location):

        if len(location) == 0:
            raise ValueError("Cannot get fields from type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            return self.storage[immediate_location].get_fields(location)

    def create_field(self, name, location):

        if len(location) == 0:
            raise ValueError("Cannot create field in type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].create_field(name, location)

    def rename_field(self, field, name, location):

        if len(location) == 0:
            raise ValueError("Cannot rename field from type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].rename_field(field, name, location)

    def delete_field(self, field, location):

        if len(location) == 0:
            raise ValueError("Cannot delete field from type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].delete_field(field, location)

    def insert(self, record, location):

        if len(location) == 0:
            raise ValueError("Cannot insert to type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].insert(record, location)

    def get(self, location):

        if len(location) == 0:
            raise ValueError("Cannot get from type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            return self.storage[immediate_location].get(location)

    def get_where(self, match, location):

        if len(location) == 0:
            raise ValueError("Cannot get from type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            return self.storage[immediate_location].get_where(match, location)

    def write(self, data, location):

        if len(location) == 0:
            raise ValueError("Cannot write to type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].write(data, location)

    def write_where(self, match, data, location):

        if len(location) == 0:
            raise ValueError("Cannot write to type 'Subbase'")
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].write_where(match, data, location)

    def delete(self, location):

        if len(location) == 0:
            self.storage = []
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].delete(location)

    def delete_where(self, location, id="", match={}):

        if len(location) == 0:
            self.storage.pop(id)
        else:
            immediate_location = location[0]
            location = location[1:]
            self.storage[immediate_location].delete_where(match, location)


class Table():

    def __init__(self, fields):

        self.fields = fields
        self.storage = []

    def get_fields(self, location):

        if len(location) == 0:
            return self.fields
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def create_field(self, name, location):

        if len(location) == 0:
            self.fields.append(name)
            for record in self.storage:
                record.append(None)
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def rename_field(self, field, name, location):

        if len(location) == 0:
            self.fields[self.fields.index(field)] = name
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def delete_field(self, field, location):

        if len(location) == 0:
            field_i = self.fields.index(field)
            self.fields.pop(field_i)
            for record in self.storage:
                record.pop(field_i)
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def insert(self, record, location):

        if len(location) == 0:
            self.storage.append([record[field] for field in self.fields])
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def get(self, location):

        if len(location) == 0:
            o = []
            for record in self.storage:
                o.append({field: item for field, item in zip(self.fields, record)})
            return o
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def get_where(self, match, location):

        if len(location) == 0:
            o = []
            for record in self.storage:
                if not False in [match[field] == record[self.fields.index(field)] for field in match]:
                    o.append({field: item for field, item in zip(self.fields, record)})
            return o
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def write(self, data, location):

        if len(location) == 0:
            for record in self.storage:
                for field in data:
                    record[self.fields.index(field)] = data[field]
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def write_where(self, match, data, location):

        if len(location) == 0:
            for record in self.storage:
                if not False in [match[field] == record[self.fields.index(field)] for field in match]:
                    for field in data:
                        record[self.fields.index(field)] = data[field]
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def delete(self, location):

        if len(location) == 0:
            self.storage = []
        else:
            raise ValueError("Type 'Table' is not subscriptable")

    def delete_where(self, match, location):

        if len(location) == 0:
            pop_i = []
            for i, record in enumerate(self.storage):
                if not False in [match[field] == record[self.fields.index(field)] for field in match]:
                    pop_i.insert(0, i)
            for i in pop_i:
                self.storage.pop(i)
        else:
            raise ValueError("Type 'Table' is not subscriptable")


class Datapoint():

    def __init__(self, fields):

        self.storage = {}
        for label in fields:
            self.storage[label] = None