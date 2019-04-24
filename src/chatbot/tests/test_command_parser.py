
import unittest
from chatbot.command_parser import CommandParser


class CommandParserTest(unittest.TestCase):

    def test_parse(self):
        parser = CommandParser()
        command = parser.parse("/help")
        self.assertEqual(command, 'help')

        command = parser.parse("/stock=test")
        self.assertEqual(command, 'test')

        command = parser.parse("/stock=aapl.us")
        self.assertEqual(command, 'aapl.us')

        command = parser.parse("/stock= not a command")
        self.assertEqual(command, None)

        command = parser.parse("not a command")
        self.assertEqual(command, None)


if __name__ == "__main__":
    unittest.main()
