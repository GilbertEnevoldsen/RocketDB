class Database():

    def __init__(self):

        self.storage = {}

    def create_repository(self, name):

        self.storage[name] = Repository()

    def rename_repository(self, repository, name):

        self.storage[name] = self.storage[repository]
        self.storage.pop(repository)

    def delete_repository(self, repository):

        self.storage.pop(repository)

    def list_repositories(self):

        return [repository for repository in self.storage]


class Repository():

    def __init__(self):

        self.storage = {}


class Document():

    def __init__(self):

        self.storage = {}