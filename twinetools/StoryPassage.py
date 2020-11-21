class StoryPassage:

    def __init__(self, name, pid, text, tags):
        self.name = name
        self.pid = pid
        self.text = text
        self.tags = list(tags)
        self.choices = []

    def add_choice(self, label, target=None):
        self.choices.append((label, target or label))
