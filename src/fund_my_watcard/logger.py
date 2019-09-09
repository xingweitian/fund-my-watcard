import logging
import colorlog
from .config_file import CONFIG_FILE_PATH

PRINT_PREFIX = "[fund-my-watcard]"

""" 
add new level - SUCCESS
"""
SUCCESS = logging.ERROR - 1
logging.addLevelName(SUCCESS, 'SUCCESS')

def success(self, msg, lvl=SUCCESS, *args, **kws):
    self.log(lvl, msg, *args, **kws)

logging.Logger.success = success


def init_logger():
    # create logger
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    logfile = CONFIG_FILE_PATH.replace("config", "log")
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)

    # create stream handler and set level to debug
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    # create formatter
    colors = {
        'INFO': 'black',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'SUCCESS': 'blue'
    }
    LOG_FORMAT_FILE = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_FORMAT_CONSOLE = '%(log_color)s' + PRINT_PREFIX + ' - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    formatter_file = logging.Formatter(LOG_FORMAT_FILE, date_format)

    formatter_console = colorlog.ColoredFormatter(
        LOG_FORMAT_CONSOLE,
        log_colors=colors,
    )

    # add formatter to handler
    fh.setFormatter(formatter_file)
    sh.setFormatter(formatter_console)

    # add handler to logger
    logger.addHandler(fh)
    logger.addHandler(sh)

    return logfile