import logging

from python_logger import setup_logger

logger = logging.getLogger("my_app")


def main():
    setup_logger("./logging_config/config.json")

    logger.warning("This is test")
    logger.debug("this is my second test")
    logger.info("this is test 3")


if __name__ == "__main__":
    main()
