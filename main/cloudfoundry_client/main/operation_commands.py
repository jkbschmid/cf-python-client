from cloudfoundry_client.main.command_domain import Command
from cloudfoundry_client.operations.push.push import PushOperation


def generate_push_command():
    entry = 'push_app'

    def generate_parser(parser):
        command_parser = parser.add_parser(entry)
        command_parser.add_argument('manifest_path', metavar='manifest_paths', type=str, nargs=1,
                                    help='The manifest path')
        command_parser.add_argument('-space_guid', action='store', dest='space_guid', type=str,
                                    help='Space guid')

    def execute(client, arguments):
        manifest_path = arguments.manifest_path[0]
        PushOperation(client).push(arguments.space_guid, manifest_path)

    return Command(entry, generate_parser, execute), 'Push an application by its manifest'
