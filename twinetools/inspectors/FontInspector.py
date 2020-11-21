import re


class FontInspector:

    def __init__(self):
        self.font_refs = set()

    def inspect(self, text):
        for match in re.finditer(r'<font="([^"]+)">', text):
            self.font_refs.add(match.group(1))

    def print_report(self):
        print(self.font_refs)
