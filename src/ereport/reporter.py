from __future__ import annotations

import os
from abc import ABC, abstractmethod
from time import time
from typing import Final
from inspect import currentframe

from empire_commons.date_util.date_util import current_yyyy_mm_dd_hh_ii_ss_ffff


class _State:
    __run_once: bool = False

    start_time: float = 0.0

    @staticmethod
    def run():
        _State.start_time = time()
        _State.__run_once = True


class Level:
    """
    Reporter level implementation
    """
    __slots__ = (
        'weight',
        'name'
    )

    def __init__(self, weight: int, name: str):
        self.weight = weight
        self.name = name

    def __eq__(self, other) -> bool:
        return isinstance(other, Level) and other.weight == self.weight

    def can_log(self, required_level: Level) -> bool:
        return required_level.weight >= self.weight


class Levels:
    """
    List of levels
    """
    ALL: Final[Level] = Level(0, 'ALL')
    TRACE: Final[Level] = Level(10, 'TRACE')
    DEBUG: Final[Level] = Level(20, 'DEBUG')
    SUCCESS: Final[Level] = Level(30, 'SUCCESS')
    INFO: Final[Level] = Level(40, 'INFO')
    WARN: Final[Level] = Level(50, 'WARN')
    ERROR: Final[Level] = Level(60, 'ERROR')
    SEVERE: Final[Level] = Level(70, 'SEVERE')
    FATAL = Final[Level] = Level(80, 'FATAL')


class Report:
    __slots__ = (
        'date_time',
        'level',
        'module',
        'function',
        'line',
        'message',
        'reporter_name'
    )

    def __init__(
            self,
            level: Level,
            module: str,
            function: str,
            line: int,
            message: str,
            reporter_name: str,
            date_time: str = None,
    ):
        self.date_time: str = date_time if date_time else current_yyyy_mm_dd_hh_ii_ss_ffff()
        self.level: str = level.name
        self.module: str = module
        self.function: str = function
        self.line: int = line
        self.message: str = message
        self.reporter_name: str = reporter_name


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, report: Report) -> str:
        raise NotImplementedError()


class DefaultFormatter:
    def format(self, report: Report) -> str:
        return f'[{report.date_time}] [{report.level}] [{report.reporter_name}] [({report.line}) {report.module}::{report.function}] {report.message}'


class ReporterOutlet(ABC):
    __slots__ = ('formatter',)
    def __init__(self):
        self.formatter = DefaultFormatter()

    def set_formatter(self, formatter):
        self.formatter = formatter

    @abstractmethod
    def emit(self, report: Report):
        raise NotImplementedError()


class ReporterOutletStdOut(ReporterOutlet):
    def emit(self, report: Report):
        pass


class Reporter:
    """
    Reporter class
    """
    __slots__ = (
        '_outlets',
        '_level',
        '_reporter_name'
    )

    def __init__(self, name: str, level: Level):
        self._outlets: list[ReporterOutlet] = []
        self._level: Level = level
        self._reporter_name: str = name

    def _log(self, report: Report):
        [outlet.emit(report) for outlet in self._outlets]

    def trace(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.TRACE):
            self._log(Report(
                level=Levels.TRACE,
                module=module or self._find_module(),
                function=function or self._find_function(),
                line=line or self._find_line_number(),
                message=message,
                reporter_name=self._reporter_name
            ))

    def _find_module(self) -> str:
        return os.path.normcase(currentframe().f_back.f_code.co_filename).replace('\\', '/').split('/')[-1].split('.')[0]

    def _find_function(self) -> str:
        name: str = currentframe().f_back.f_back.f_code.co_name
        if name == '<module>':
            return '<module-level>'

        return name

    def _find_line_number(self) -> int:
        return currentframe().f_back.f_back.f_lineno
