from __future__ import annotations

import os
from inspect import currentframe

from ereport.outlet import ReporterOutlet
from ereport.level import Level, Levels
from ereport.report import Report


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
