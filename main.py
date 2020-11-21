import json
import re
import sys


class CommandInspector:
    def __init__(self):
        self.commands = []

    def inspect(self, text):
        for m in re.finditer(r'\{\{([^}]+)}}', text):
            command = m.group(1)
            parts = re.split(r':', command, 2)
            self.commands.append({'command': parts[0], 'params': parts[1:]})

    def print_report(self):
        print(self.commands)


class FontInspector:
    def __init__(self):
        self.font_refs = set()

    def inspect(self, text):
        for m in re.finditer(r'<font="([^"]+)">', text):
            self.font_refs.add(m.group(1))

    def print_report(self):
        print(self.font_refs)


with open(sys.argv[1], 'r') as f:
    contents = f.read()

if contents:
    inspectors = [CommandInspector(), FontInspector()]
    link_targets = set()
    story = {'passages': []}

    matches = re.search(r'<tw-storydata.+</tw-storydata>', contents, re.DOTALL)
    if matches:
        storydata = matches.group(0)
        for match in re.finditer(r'<tw-passagedata([^>]+)>([^<]+)</tw-passagedata>', storydata):
            passage_attributes = match.group(1)
            text = match.group(2)
            text = text.replace('&#39;', '\'').replace('&quot;', '"').replace('&lt;', '<').replace('&gt;', '>')\
                .replace('&amp;', '&')

            pid = int(re.search(r' pid="([^"]+)" ', passage_attributes).group(1))
            name = re.search(r' name="([^"]+)" ', passage_attributes).group(1)
            matches = re.search(r' tags="([^"]+)" ', passage_attributes)
            if matches:
                tags = matches.group(1).split(' ')
            else:
                tags = []
            # print(name, pid, tags, text)

            choices = []
            for m in re.finditer(r'\[\[([^]]+)]]', text):
                link = m.group(1)
                parts = re.split(r'\|', link, 2)
                if len(parts) == 1:
                    choices.append({'label': parts[0], 'target': parts[0]})
                    link_targets.add(parts[0])
                else:
                    choices.append({'label': parts[0], 'target': parts[1]})
                    link_targets.add(parts[1])

            story['passages'].append({'pid': pid, 'name': name, 'tags': tags, 'text': text, 'choices': choices})

            for insp in inspectors:
                insp.inspect(text)

    # print(story)
    # print(json.dumps(story))

    #print(link_targets)
    for insp in inspectors:
        insp.print_report()
