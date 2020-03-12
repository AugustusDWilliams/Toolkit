from collections import defaultdict
from loguru import logger


if __name__ == "__main__":
    sample_dict = defaultdict(str)
    sample_dict['Name'] = "Daniel Williams"
    sample_dict['Age'] = 29
    sample_dict['Nickname']
    logger.debug(sample_dict)
    logger.debug(sample_dict['Occupation'])
