import re


class CommandInspector:

    def __init__(self):
        self.commands = []

    def inspect(self, story):
        for passage in story['passages']:
            for match in re.finditer(r'\{\{([^}]+)}}', passage['text']):
                command = match.group(1)
                parts = re.split(r':', command, 2)
                self.commands.append({'command': parts[0], 'params': parts[1:]})

    def print_report(self):
        print(self.commands)