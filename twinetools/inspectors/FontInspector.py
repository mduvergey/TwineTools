import re


class FontInspector:

    def __init__(self):
        self.font_refs = set()

    def inspect(self, story):
        for name, passage in story.passages.items():
            for match in re.finditer(r'<font="([^"]+)">', passage.text):
                self.font_refs.add(match.group(1))

    def print_report(self):
        print('-- Referenced fonts --')
        if len(self.font_refs):
            print(sorted(self.font_refs))
        else:
            print('No font references found.')
