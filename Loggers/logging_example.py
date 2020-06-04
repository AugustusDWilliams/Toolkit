import logging

LOG_FILENAME = "example.log"
LOG_LEVEL_CONSOLE = logging.DEBUG
LOG_LEVEL_FILE = logging.DEBUG
LOG_FORMAT_CONSOLE = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
LOG_FORMAT_FILE = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
TEST_FMT = logging.Formatter("""| %(levelname)s | - %(asctime)s %(module)s:%(funcName)s %(message)s""")

LOGURU_FMT = "2020-02-06 11:21:14.212 | DEBUG    | __main__:func:28 - In Class Function"

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(level=LOG_LEVEL_CONSOLE)
FH = logging.FileHandler(LOG_FILENAME)
FH.setLevel(LOG_LEVEL_FILE)
CH = logging.StreamHandler()
CH.setFormatter(LOG_FORMAT_CONSOLE)
#CH.setFormatter(TEST_FMT)
LOGGER.addHandler(FH)
LOGGER.addHandler(CH)

if __name__ == "__main__":
    LOGGER.debug("A quirky message only developers care about")
    LOGGER.info("Curious users might want to know this")
    LOGGER.warning("Something is wrong and any user should be informed")
    LOGGER.error("Serious stuff, this is red for a reason")
    LOGGER.critical("OH NO everything is on fire")
