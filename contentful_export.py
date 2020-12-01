from contentful import Client
from argparse import ArgumentParser
import re
import json

arg_parser = ArgumentParser(description='Export passages from Contentful.')
arg_parser.add_argument('--contentful-api-token', help='Contentful CDA API token')
arg_parser.add_argument('--contentful-space-id', help='Contentful space ID')
arg_parser.add_argument('--story-id', help='Story ID')
args = arg_parser.parse_args()

client = Client(
    args.contentful_space_id,
    args.contentful_api_token,
    environment='master'  # Optional - it defaults to 'master'.
)

entries_by_content_type = client.entries({'content_type': 'passage', 'fields.story.sys.id': args.story_id})

nodes = []
mapping = {}
for index, entry in enumerate(entries_by_content_type):
    #nodes.append({'name': entry.name, 'text': entry.text})
    nodes.append({'name': entry.name})
    #print(entry.name)
    mapping[entry.name] = index

links = []
for entry in entries_by_content_type:
    for m in re.finditer(r'\[\[([^]]+)]]', entry.text):
        link = m.group(1)
        parts = re.split(r'\|', link, 2)
        if len(parts) == 1:
            target = parts[0]
        else:
            target = parts[1]
        links.append({'source': mapping[entry.name], 'target': mapping[target]})

print(json.dumps(nodes))
print(json.dumps(links))
