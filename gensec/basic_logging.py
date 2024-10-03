from __future__ import annotations

import logging


class BasicLogger:
    def __init__(
        self,
        name: str | None = None,
        level: int | None = logging.DEBUG,
        log_format: str | None = None,
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ) -> None:
        self.name = name or __name__
        self.level = level
        self.log_format = (
            log_format
            or "%(asctime)s | %(name)s | %(filename)s | %(module)s | %(funcName)s | %(levelname)s | %(message)s"
        )
        self.date_format = date_format

        self.logger = self._get_or_create_logger()

    def _get_or_create_logger(self) -> logging.Logger:
        # create logger
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)

        if not logger.hasHandlers():
            # create formatter
            formatter = logging.Formatter(self.log_format, self.date_format)

            # create console handler and set level and formatter
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.level)
            console_handler.setFormatter(formatter)

            # add console handler to logger
            logger.addHandler(console_handler)

        # disable propagation
        logger.propagate = False

        return logger
