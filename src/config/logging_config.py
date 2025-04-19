import logging
from colorlog import ColoredFormatter


logger = logging.getLogger("SpaceX")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()

formatter = ColoredFormatter(
    "%(asctime)s %(log_color)s%(levelname)-2s%(reset)s %(blue)s%(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    log_colors={
        "ERROR": "red",
        "WARNING": "yellow",
        "INFO": "green",
        "DEBUG": "cyan",
        "CRITICAL": "magenta",
    },
)


console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
