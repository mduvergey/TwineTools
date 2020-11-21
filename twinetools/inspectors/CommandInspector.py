import re


class CommandInspector:
    known_commands = ('AddItemToBag', 'AddLocationOnMap', 'ClearFlag', 'DisableActionMode', 'EnableActionMode',
                      'EnableMap', 'EndGame', 'EndIf', 'HideCharacter', 'IfFlagNotSet', 'IfFlagSet',
                      'IfHasNotVisitedPassage', 'IfHasVisitedPassage', 'IfItemInBag', 'IfItemNotInBag', 'IfKarmaBad',
                      'IfKarmaGood', 'IfKarmaNeutral', 'LoadBackground', 'NoteBadAction', 'NoteGoodAction', 'PlayMusic',
                      'PlaySound', 'RemoveItemFromBag', 'RemoveLocationFromMap', 'SetFlag', 'SetTimer', 'ShowCharacter',
                      'ShowManicule', 'ShowMap', 'StopAllSounds', 'StopMusic', 'Wait')

    def __init__(self):
        self.distinct_commands = {}
        self.unknown_commands = []

    def inspect(self, story):
        for name, passage in story.passages.items():
            for match in re.finditer(r'\{\{([^}]+)}}', passage.text):
                command = match.group(1)
                parts = re.split(r':', command, 3)
                if not parts[0] in CommandInspector.known_commands:
                    self.unknown_commands.append((passage, parts[0]))
                if not parts[0] in self.distinct_commands:
                    self.distinct_commands[parts[0]] = []
                self.distinct_commands[parts[0]].append({'command': parts[0], 'params': parts[1:]})

    def print_report(self):
        print('-- Commands --')
        if len(self.distinct_commands):
            for key, value in sorted(self.distinct_commands.items()):
                print('{0}: {1}'.format(key, len(value)))
        else:
            print('No commands found.')
        if len(self.unknown_commands):
            print('-- Unknown commands --')
            for uc in self.unknown_commands:
                print('Unknown command in passage "{0}": {1}'.format(uc[0].name, uc[1]))
