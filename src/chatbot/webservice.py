
import requests
import csv
from settings import *


LOGGER = logging.getLogger(__name__)


class Webservice:

    def __init__(self, stock_id):
        self.stock_id = stock_id

    def call(self):
        text = self.download()
        return self.parse_response(text)

    def download(self):
        url = "https://stooq.com/q/l/?s=%s&f=sd2t2ohlcv&h&e=csv" % self.stock_id
        try:
            r = requests.get(url)
        except Exception as ex:
            LOGGER.exception(ex)
            return None

        LOGGER.info(r.status_code)
        LOGGER.info(r.text)
        return r.text

    def parse_response(self, text):
        lines = text.splitlines()
        contents = csv.reader(lines, delimiter=',')
        rows = list(contents)
        if len(rows) < 2:
            return None
        if len(rows[1]) < 6:
            return None
        value = rows[1][6]
        return "%s quote is $%s per share" % (self.stock_id.upper(), value)

# EOF
