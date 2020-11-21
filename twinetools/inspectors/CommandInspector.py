import re


class CommandInspector:

    def __init__(self):
        self.distinct_commands = {}

    def inspect(self, story):
        for passage in story['passages']:
            for match in re.finditer(r'\{\{([^}]+)}}', passage['text']):
                command = match.group(1)
                parts = re.split(r':', command, 3)
                if not parts[0] in self.distinct_commands:
                    self.distinct_commands[parts[0]] = []
                self.distinct_commands[parts[0]].append({'command': parts[0], 'params': parts[1:]})

    def print_report(self):
        for key, value in sorted(self.distinct_commands.items()):
            print('{0}: {1}'.format(key, len(value)))
