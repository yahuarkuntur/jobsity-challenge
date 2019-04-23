
import unittest
import csv
from chatbot.chatbot import *
from settings import *


class ChatbotTest(unittest.TestCase):

    def test_parse_response(self):
        bot = Chatbot('aapl.us')
        text = "Symbol,Date,Time,Open,High,Low,Close,Volume\nAAPL.US,2019-04-22,22:00:16,202.83,204.94,202.34,204.53,19439545"
        msg = bot.parse_response(text)
        self.assertEqual(msg, 'AAPL.US quote is $202.83 per share')

        text = ""
        msg = bot.parse_response(text)
        self.assertEqual(msg, None)

        text = "Symbol,Date,Time,Open,High,Low,Close,Volume"
        msg = bot.parse_response(text)
        self.assertEqual(msg, None)

        text = "Symbol,Date,Time,Open,High,Low,Close,Volume\nAAPL.US,2019-04-22,22:00:16,202.83"
        msg = bot.parse_response(text)
        self.assertEqual(msg, 'AAPL.US quote is $202.83 per share')

    def test_download(self):
        bot = Chatbot('aapl.us')
        text = bot.download()
        lines = text.splitlines()
        contents = csv.reader(lines, delimiter=',')
        rows = list(contents)
        self.assertEqual(rows[0], ['Symbol', 'Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        # response values change over time, so we test for the values that don't
        self.assertEqual(rows[1][0], 'AAPL.US')


if __name__ == "__main__":
    unittest.main()
