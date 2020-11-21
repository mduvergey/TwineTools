class Story:

    def __init__(self):
        self.passages = {}

    def add_passage(self, passage):
        self.passages[passage.name] = passage
