import logging

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


def add_log():
    logging.basicConfig(filename='test.log', filemode='w',level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S', format="%(module)s : %(levelname)s: %(asctime)s %(message)s")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger
