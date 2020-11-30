from argparse import ArgumentParser
from twinetools import TwineParser
from twinetools.inspectors import CommandInspector, ContentfulExportInspector, FontInspector, PassageInspector

arg_parser = ArgumentParser(description='Extract information from Twine files.')
arg_parser.add_argument('file', nargs='+', help='Twine HTML file to parse')
arg_parser.add_argument('-c', '--list-commands', help='List interpreter commands', action='store_true')
arg_parser.add_argument('-e', '--export-to-contenful', help='Export stories to Contentful', action='store_true')
arg_parser.add_argument('--contentful-api-token', help='Contentful Management API token')
arg_parser.add_argument('--contentful-space-id', help='Contentful space ID')
arg_parser.add_argument('-f', '--list-fonts', help='List referenced fonts', action='store_true')
arg_parser.add_argument('-p', '--dump-passages', help='Dump all passages', action='store_true')
args = arg_parser.parse_args()

for filename in args.file:
    try:
        with open(filename, 'r') as f:
            contents = f.read()

            print('== Parsing file {0} =='.format(filename))

            inspectors = []
            if args.list_commands:
                inspectors.append(CommandInspector())
            if args.export_to_contenful:
                inspectors.append(ContentfulExportInspector(args.contentful_api_token, args.contentful_space_id))
            if args.list_fonts:
                inspectors.append(FontInspector())
            if args.dump_passages:
                inspectors.append(PassageInspector())

            parser = TwineParser(inspectors)
            parser.parse(contents)
            parser.print_report()
    except EnvironmentError:
        print('Error: unable to read file {0}'.format(filename))
