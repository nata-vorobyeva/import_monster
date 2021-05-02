# -*- coding: utf-8 -*-
"""
Dummy module to use it for import_monster tests
"""


def test_callable():
    """
    Call callable method.
    Test_callable_method is callable,
    this tests intends showing that.
    """
    return


@property
def test_non_callable():
    """Decorator makes it non callable,
    that can be a good check.
    """
    return


def mean(x=1, y=1):
    """Callable function, available in numpy."""
    return (x + y) / 2
