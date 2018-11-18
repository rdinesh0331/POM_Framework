import logging
import inspect


def custom_log(loglevel):

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(filename='{}.log'.format(logger_name), mode='w')
    file_handler.setLevel(loglevel)

    formatter = logging.Formatter(format('%(asctime)s - %(filename)s - %(levelname)s - %(message)s'),
                                  datefmt='%m:%d:%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

