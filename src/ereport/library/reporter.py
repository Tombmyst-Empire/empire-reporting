from __future__ import annotations

import os
from inspect import currentframe

from ereport.library.formatter import AdaptativeColoredFormatter
from ereport.library.outlet import ReporterOutlet, ReporterOutletStdOut
from ereport.library.level import Level, Levels
from ereport.library.report import Report


class Reporter:
    """
    Reporter class
    """
    __slots__ = (
        '_outlets',
        '_level',
        '_reporter_name'
    )

    _instances: dict[str, Reporter] = {}

    def __init__(self, name: str, level: Level):
        self._outlets: list[ReporterOutlet] = [
            ReporterOutletStdOut(
                AdaptativeColoredFormatter()
            )
        ]
        self._level: Level = level
        self._reporter_name: str = name.upper()
        Reporter._instances[name.upper()] = self

    @classmethod
    def get_or_make(cls, name: str, env_var_logging_level: str = None, default_level: str | Levels = Levels.INFO) -> Reporter:
        name = name.upper()

        env_level: str | None = os.getenv(env_var_logging_level) if env_var_logging_level else None
        required_level: Level = (
            Levels.parse_from_string(env_level) if env_level else None
        ) or default_level

        if name in Reporter._instances:
            return Reporter._instances[name]

        return cls(name, required_level)

    @property
    def level(self) -> Level:
        return self._level

    @level.setter
    def level(self, value: Level):
        self.level = value

    @property
    def name(self) -> str:
        return self.name

    def add_outlet(self, outlet: ReporterOutlet) -> Reporter:
        self._outlets.append(outlet)
        return self

    def remove_outlet_at(self, index: int) -> Reporter:
        del self._outlets[index]
        return self

    def get_all_outlets(self) -> tuple[ReporterOutlet]:
        return tuple(self._outlets)

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

    def debug(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.DEBUG):
            self._log(Report(
                level=Levels.DEBUG,
                module=module or self._find_module(),
                function=function or self._find_function(),
                line=line or self._find_line_number(),
                message=message,
                reporter_name=self._reporter_name
            ))

    def success(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.SUCCESS):
            self._log(Report(
                level=Levels.SUCCESS,
                module=module or self._find_module(),
                function=function or self._find_function(),
                line=line or self._find_line_number(),
                message=message,
                reporter_name=self._reporter_name
            ))

    def info(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.INFO):
            self._log(Report(
                level=Levels.INFO,
                module=module or self._find_module(),
                function=function or self._find_function(),
                line=line or self._find_line_number(),
                message=message,
                reporter_name=self._reporter_name
            ))

    def warn(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.WARN):
            self._log(Report(
                level=Levels.WARN,
                module=module or self._find_module(),
                function=function or self._find_function(),
                line=line or self._find_line_number(),
                message=message,
                reporter_name=self._reporter_name
            ))

    def error(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.ERROR):
            self._log(Report(
                level=Levels.ERROR,
                module=module or self._find_module(),
                function=function or self._find_function(),
                line=line or self._find_line_number(),
                message=message,
                reporter_name=self._reporter_name
            ))

    def severe(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.SEVERE):
            self._log(Report(
                level=Levels.SEVERE,
                module=module or self._find_module(),
                function=function or self._find_function(),
                line=line or self._find_line_number(),
                message=message,
                reporter_name=self._reporter_name
            ))

    def fatal(self, message: str, module: str | None = None, function: str | None = None, line: int | None = None):
        if self._level.can_log(Levels.FATAL):
            self._log(Report(
                level=Levels.FATAL,
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


if __name__ == '__main__':
    r = Reporter('test', Levels.TRACE)
    r.trace('Ceci est un test')
    r.debug('Ceci est un debug')
    r.success('Ceci est success')
    r.info('Ceci est uin info')
    r.warn('Ceci est un wanring')
    r.error('Ceci est un error')
    r.severe('Ceci est un severe')
    r.fatal('Ceci est un fatal')
