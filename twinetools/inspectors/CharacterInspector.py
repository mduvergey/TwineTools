import re


class CharacterInspector:

    def __init__(self):
        self.character_refs = set()

    def inspect(self, story):
        for name, passage in story.passages.items():
            for match in re.finditer(r'\{\{(?:ShowCharacter|HideCharacter):([^}]+)}}', passage.text):
                self.character_refs.add(match.group(1))

    def print_report(self):
        print('-- Referenced characters --')
        if len(self.character_refs):
            for ref in sorted(self.character_refs):
                print(ref)
        else:
            print('No character references found.')
