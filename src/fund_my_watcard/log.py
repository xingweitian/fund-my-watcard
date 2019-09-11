import logging
import colorlog
from .config_file import USER_DIR
from .util import PRINT_PREFIX

# add new level - SUCCESS
SUCCESS = logging.ERROR - 1
logging.addLevelName(SUCCESS, "SUCCESS")


def success(self, msg, lvl=SUCCESS, *args, **kws):
    self.log(lvl, msg, *args, **kws)


logging.Logger.success = success


def init_logger():
    # create logger
    logger = logging.getLogger("logger")
    logger.setLevel(logging.INFO)

    # create file handler and set level to INFO
    logfile = USER_DIR + "/.watcard_log"
    fh = logging.FileHandler(logfile)
    fh.setLevel(SUCCESS)

    # create stream handler and set level to INFO
    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)

    # create formatter
    colors = {"INFO": "black", "WARNING": "yellow", "ERROR": "red", "SUCCESS": "blue"}
    log_format_file = "%(asctime)s - %(levelname)s - %(message)s"
    log_format_console = "%(log_color)s" + PRINT_PREFIX + " %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    formatter_file = logging.Formatter(log_format_file, date_format)
    formatter_console = colorlog.ColoredFormatter(log_format_console, log_colors=colors)

    # add formatter to handler
    fh.setFormatter(formatter_file)
    sh.setFormatter(formatter_console)

    # add handler to logger
    logger.addHandler(fh)
    logger.addHandler(sh)

    return logfile
