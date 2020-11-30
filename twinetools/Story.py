class Story:

    def __init__(self, name):
        self.name = name
        self.passages = {}

    def add_passage(self, passage):
        self.passages[passage.name] = passage
