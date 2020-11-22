class PassageInspector:

    def __init__(self):
        self.report = ''

    def inspect(self, story):
        for name, passage in story.passages.items():
            self.report = self.report + '-- Passage "{0}" (pid: {1}) --\nTags: {2}\n{3}\n'\
                .format(passage.name, passage.pid, passage.tags, passage.text)

    def print_report(self):
        print(self.report)
