import re


class BackgroundInspector:

    def __init__(self):
        self.background_refs = set()

    def inspect(self, story):
        for name, passage in story.passages.items():
            for match in re.finditer(r'\{\{LoadBackground:([^}]+)}}', passage.text):
                self.background_refs.add(match.group(1))

    def print_report(self):
        print('-- Referenced backgrounds --')
        if len(self.background_refs):
            for ref in sorted(self.background_refs):
                print(ref)
        else:
            print('No background references found.')
