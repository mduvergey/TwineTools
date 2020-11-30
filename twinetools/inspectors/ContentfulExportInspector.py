import contentful_management


class ContentfulExportInspector:

    def __init__(self, api_token, space_id):
        client = contentful_management.Client(api_token)
        self.environment = client.environments(space_id).find('master')

    def inspect(self, story):
        entry_attributes = {
            'content_type_id': 'story',
            'fields': {
                'name': {
                    'fr': story.name
                }
            }
        }
        story_entry = self.environment.entries().create(
            None,
            entry_attributes
        )
        story_entry.publish()
        for _, passage in story.passages.items():
            entry_attributes = {
                'content_type_id': 'passage',
                'fields': {
                    'name': {
                        'fr': passage.name
                    },
                    'text': {
                        'fr': passage.text
                    },
                    'story': {
                        'fr': {
                            'sys': {
                                'type': 'Link',
                                'linkType': 'Entry',
                                'id': story_entry.id
                            }
                        }
                    }
                }
            }
            passage_entry = self.environment.entries().create(
                None,
                entry_attributes
            )
            passage_entry.publish()

    def print_report(self):
        pass
