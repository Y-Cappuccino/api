from abc import ABC

from ycappuccino.api.core import YCappuccinoComponent


class IListComponent(YCappuccinoComponent, ABC):
    def call(self, a_comp_name, a_method): ...


class IActivityLogger(YCappuccinoComponent, ABC):

    def debug(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        ...

    def info(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "notable problem", exc_info=1)
        """
        ...

    def warning(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        ...

    def warn(self, msg, *args, **kwargs): ...

    def error(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        ...

    def exception(self, msg, *args, exc_info=True, **kwargs):
        """
        Convenience method for logging an ERROR with exception information.
        """
        ...

    def critical(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        ...

    def fatal(self, msg, *args, **kwargs):
        """
        Don't use this method, use critical() instead.
        """
        ...


class IConfiguration(YCappuccinoComponent, ABC):
    def get(self, key, default=None):
        """
        Get configuration value.

        :param key: type: str       Configuration key.
        :return:    type: str       Configuration value, or None.
        """
        ...

    def has(self, key):
        """
        Determine whether a configuration exists.

        :param key: type: str       Configuration key.
        :return:    type: boolean
        """
        ...

    def backupConfig(self):
        """backup last configuration file"""
        ...

    def set(self, key, value): ...
