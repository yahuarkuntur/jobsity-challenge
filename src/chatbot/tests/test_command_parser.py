
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

        with self.assertRaises(Exception) as context:
            parser.parse("/stock= not a command")
            self.assertTrue('Unknown command' in context.exception)

        with self.assertRaises(Exception) as context:
            parser.parse("/not a command")
            self.assertTrue('Unknown command' in context.exception)

        command = parser.parse("not a command")
        self.assertEqual(command, None)


if __name__ == "__main__":
    unittest.main()
