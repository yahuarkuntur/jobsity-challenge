
import logging
import os
import ConfigParser

# absolute paths hack
current_dir = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(current_dir, '..'))

# config
CONFIG = ConfigParser.RawConfigParser()
CONFIG.read(os.path.join(ROOT_DIR, 'config', 'main.conf'))

# logging
LOG_FORMAT = '[%(asctime)s] %(levelname)s %(name)s %(funcName)s %(lineno)d: %(message)s'
LOG_LEVEL = logging.DEBUG

if 'INFO' == CONFIG.get('server', 'log-level'):
    LOG_LEVEL = logging.INFO

if 'ERROR' == CONFIG.get('server', 'log-level'):
    LOG_LEVEL = logging.ERROR

if 'WARNING' == CONFIG.get('server', 'log-level'):
    LOG_LEVEL = logging.WARNING

if 'CRITICAL' == CONFIG.get('server', 'log-level'):
    LOG_LEVEL = logging.CRITICAL


logging.basicConfig(
    # filename=os.path.join(ROOT_DIR, 'logs', 'jobsity.log'),
    level=LOG_LEVEL,
    format=LOG_FORMAT
)

# EOF
