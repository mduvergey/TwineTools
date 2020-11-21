import re
from .Story import Story
from .StoryPassage import StoryPassage


class TwineParser:

    def __init__(self, inspectors=()):
        self.inspectors = tuple(inspectors)
        self.story = None

    def parse(self, twine_text):
        self.story = Story()

        matches = re.search(r'<tw-storydata.+</tw-storydata>', twine_text, re.DOTALL)
        if matches:
            story_data = matches.group(0)
            for match in re.finditer(r'<tw-passagedata([^>]+)>([^<]+)</tw-passagedata>', story_data):
                passage_attributes = match.group(1)
                passage_text = match.group(2).replace('&#39;', '\'').replace('&quot;', '"').replace('&lt;', '<')\
                    .replace('&gt;', '>').replace('&amp;', '&')

                pid = int(re.search(r' pid="([^"]+)" ', passage_attributes).group(1))
                name = re.search(r' name="([^"]+)" ', passage_attributes).group(1)
                matches = re.search(r' tags="([^"]+)" ', passage_attributes)
                if matches:
                    tags = matches.group(1).split(' ')
                else:
                    tags = ()

                passage = StoryPassage(name, pid, passage_text, tags)

                for m in re.finditer(r'\[\[([^]]+)]]', passage_text):
                    link = m.group(1)
                    parts = re.split(r'\|', link, 2)
                    if len(parts) == 1:
                        passage.add_choice(parts[0])
                    else:
                        passage.add_choice(parts[0], parts[1])

                self.story.add_passage(passage)

        for inspector in self.inspectors:
            inspector.inspect(self.story)

    def print_report(self):
        for inspector in self.inspectors:
            inspector.print_report()
