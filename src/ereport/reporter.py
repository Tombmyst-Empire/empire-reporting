from __future__ import annotations

import os
from inspect import currentframe

from ereport.formatter import AdaptativeColoredFormatter
from ereport.outlet import ReporterOutlet, ReporterOutletStdOut
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
        self._outlets: list[ReporterOutlet] = [
            ReporterOutletStdOut(
                AdaptativeColoredFormatter()
            )
        ]
        self._level: Level = level
        self._reporter_name: str = name

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


_DEFAULT_REPORTER = Reporter('MAIN', Levels.parse_from_string(os.getenv('LOGGING_LEVEL', 'INFO')))


def trace(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.TRACE):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.TRACE,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def debug(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.DEBUG):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.DEBUG,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def success(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.SUCCESS):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.SUCCESS,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def info(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.INFO):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.INFO,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def warn(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.WARN):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.WARN,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def error(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.ERROR):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.ERROR,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def severe(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.SEVERE):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.SEVERE,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def fatal(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.FATAL):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.FATAL,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


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
    print('--------------------------')
    trace('Ceci est un test')
    debug('Ceci est un debug')
    success('Ceci est success')
    info('Ceci est uin info')
    warn('Ceci est un wanring')
    error('Ceci est un error')
    severe('Ceci est un severe')
    fatal('Ceci est un fatal')
