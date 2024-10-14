import json
import logging
import logging.config
import pathlib


def setup_logger(file_path: str) -> None:
    config_file = pathlib.Path(file_path)

    with open(config_file) as f_in:
        config = json.load(f_in)
        logging.config.dictConfig(config)
