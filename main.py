import json
import sys
from twinetools import TwineParser
from twinetools.inspectors import CommandInspector, FontInspector


with open(sys.argv[1], 'r') as f:
    contents = f.read()

if contents:
    parser = TwineParser((CommandInspector(), FontInspector()))

    parser.parse(contents)

    link_targets = set()
    for passage in parser.story['passages']:
        for choice in passage['choices']:
            link_targets.add(choice['target'])

    # print(story)
    # print(json.dumps(story))

    print(link_targets)
    parser.print_report()
