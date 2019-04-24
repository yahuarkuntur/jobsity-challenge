
import re

STOCK_CODE_COMMAND = re.compile("^/stock=(?P<command>\S+)$", re.I)
HELP_COMMAND = re.compile("^/help$", re.I)


class CommandParser:

    def parse(self, message):

        result = STOCK_CODE_COMMAND.search(message)
        if result and 'command' in result.groupdict().keys():
            return result.groupdict()['command']

        result = HELP_COMMAND.search(message)
        if result:
            return 'help'

        if self.is_command(message):
            raise Exception('Unknown command "%s"' % message)

        return None

    def is_command(self, message):
        if message[0] == "/":
            return True
        return False

# EOF
