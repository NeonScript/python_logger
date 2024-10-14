import json
import logging
import logging.config
import pathlib


def setup_logger(config_file: str) -> None:
    config_file = pathlib.Path(config_file)

    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)
