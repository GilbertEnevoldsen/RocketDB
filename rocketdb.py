# Returns if data matches search
def _matches(document, match, or_match=False):

    results = []

    for field in match:

        if field[0] == "$":

            if field[1:] == "greater":
                for subfield in match[field]:
                    results.append(subfield in document and type(document[subfield]) in [type(int()), type(float())] and document[subfield] > match[field][subfield])
                    break
                continue

            elif field[1:] == "less":
                for subfield in match[field]:
                    results.append(subfield in document and type(document[subfield]) in [type(int()), type(float())] and document[subfield] < match[field][subfield])
                continue

            elif field[1:] == "exists":
                for subfield in match[field]:
                    results.append(subfield in document and subfield in document)
                    break
                continue

            elif field[1:] == "in":
                for subfield in match[field]:
                    results.append(subfield in document and type(document[subfield]) in [type(list()), type(dict())] and match[field][subfield] in document[subfield])
                    break
                continue

            elif field[1:] == "and":
                results.append(subfield in document and _matches(document, match[field]))
                continue

            elif field[1:] == "or":
                results.append(subfield in document and _matches(document, match[field], True))
                continue

            elif field[1:] == "not":
                results.append(subfield in document and _matches(document, match[field]) ^ True)
                continue

        else: 
            results.append(field in document and document[field] == match[field])
            continue

        results.append(True)

    if or_match: return True if True in results else False
    else: return False if False in results else True


# Contains and manages repositories
class Database():

    # Initiates database
    def __init__(self):

        self.storage = {}

    # Creating a repository
    def create_repository(self, name):

        self.storage[name] = Repository()

    # Renaming a repository
    def rename_repository(self, repository, name):

        self.storage[name] = self.storage[repository]
        self.storage.pop(repository)

    # Deletes a repository
    def delete_repository(self, repository):

        self.storage.pop(repository)

    # Returns a list containing the names of all repositories
    def list_repositories(self):

        return [repository for repository in self.storage]

    # Inserts a document in a repository
    def insert(self, repository, data):

        return self.storage[repository].insert(data)

    # Returns documents in a repository
    def get(self, repository, match={}, fields=[]):

        return self.storage[repository].get(match, fields)

    # Writes to documents in a repository
    def write(self, repository, match={}, data={}):

        return self.storage[repository].write(match, data)

    # Merges to documents in a repository
    def merge(self, repository, match={}, data={}):

        return self.storage[repository].merge(match, data)

    # Merges to documents in a repository
    def delete(self, repository, match={}):

        return self.storage[repository].delete(match)


# Contains and manages documents
class Repository():

    # Initiates repository
    def __init__(self):

        self.storage = []

    # Inserts a document
    def insert(self, data):

        self.storage.append(data)

    # Returns documents
    def get(self, match, fields):

        results = []

        for document in self.storage:
            if _matches(document, match):
                if len(fields) > 0:
                    results.append({field: document[field] for field in fields})
                else:
                    results.append(document)

        return results

    # Writes to documents
    def write(self, match, data):

        for i, document in enumerate(self.storage):
            if _matches(document, match):
                self.storage[i] = data

    # Writes to documents
    def merge(self, match, data):

        for document in self.storage:
            if _matches(document, match):
                for field in data:
                    document[field] = data[field]