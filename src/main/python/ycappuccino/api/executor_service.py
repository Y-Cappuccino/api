from __future__ import annotations

from abc import abstractmethod
from threading import Semaphore, current_thread
from concurrent.futures.thread import ThreadPoolExecutor
import logging
import time

from ycappuccino.api.base import IActivityLogger
import typing as t

logger = logging.getLogger(__name__)
# TODO adapter in asyncio


class Callable(object):

    def __init__(self, a_name, a_log=None):
        self._name = a_name
        if a_log is None:
            self._log = a_log
        else:
            self._log = logger

    def run(self):
        """main loop for the thread that call the run"""
        pass


class RunnableProcess(Callable):

    def __init__(self, a_name: str, a_log: IActivityLogger = None) -> None:
        super(RunnableProcess, self).__init__(a_name, a_log)
        self._activate = False
        self._semaphore = Semaphore()
        self._name = a_name

    @abstractmethod
    def process(self) -> None:
        """abstract run class"""
        pass

    def is_active(self) -> bool:
        self._log.info("RunnableProcess {} activate ".format(self._name))
        return self._activate

    def run(self) -> None:
        """main loop for the thread that call the run"""
        try:
            while self._activate:
                self.process()
        except Exception as e:
            self.handle_exception(e)

        self.release_callable()

    def set_activate(self, active: bool) -> None:
        """start the thread"""
        self._semaphore.acquire()
        logger.info("set_activate {} value {}".format(self._name, active))
        self._activate = active
        self._semaphore.release()

    def release_callable(self) -> None:
        """method call when the thread is finish"""
        self._log.info("release RunnableProcess {}  ".format(self._name))

    def handle_exception(self, a_exception: BaseException) -> None:
        """method call when a exception in the main loop occured"""
        self._log.error("ERROR RunnableProcess {}  ".format(self._name))
        self._log.exception(a_exception)


def _run(a_runnable) -> None:
    try:
        if a_runnable != None:
            current_thread().name = a_runnable._name
            return a_runnable.run()
    except Exception as e:
        logger.exception(e)


class ThreadPoolExecutorCallable(object):
    def __init__(self, name: str, a_max_worker: int = 1) -> None:
        self._name = name
        self._executor = ThreadPoolExecutor(max_workers=a_max_worker)

    def submit(self, a_runnable: RunnableProcess) -> None:
        return self._executor.submit(_run, a_runnable)

    def shutdown(self) -> None:
        self._executor.shutdown()


def new_executor(name: str, a_max_worker: int = 1) -> ThreadPoolExecutorCallable:
    return ThreadPoolExecutorCallable(name, a_max_worker)


class ScheduleRunnable(RunnableProcess):
    def __init__(
        self,
        a_executor: SchedulerExecutorCallable,
        a_timer: int,
        a_log: IActivityLogger,
    ):
        super(ScheduleRunnable, self).__init__("ScheduleRunnable", a_log)
        self._timer = a_timer
        self._executor = a_executor

    def process(self) -> None:
        """abstract run class"""
        for a_runnable in self._executor.get_runnable():
            a_runnable.run()
        time.sleep(self._timer)


class SchedulerExecutorCallable(object):
    def __init__(self, name: str, a_timer, logger: IActivityLogger) -> None:
        self._name = name
        self._executor = ThreadPoolExecutor(max_workers=1)
        self._runnable = []
        self._runnable_main = ScheduleRunnable(self, a_timer, logger)
        self._future = None

    def submit(self, a_runnable: RunnableProcess) -> None:
        self._runnable.append(a_runnable)
        if self._future is None:
            self._future = self._executor.submit(_run, self._runnable_main)
        return self._future

    def get_runnable(self) -> t.List[RunnableProcess]:
        return self._runnable

    def shutdown(self) -> None:
        self._executor.shutdown()


def new_schedule_executor(
    name: str, a_timer: int, a_logger: IActivityLogger
) -> SchedulerExecutorCallable:
    return SchedulerExecutorCallable(name, a_timer, a_logger)
