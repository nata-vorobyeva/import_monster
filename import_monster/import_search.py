# -*- coding: utf-8 -*-
import builtins
import importlib
import math
from collections.abc import Callable
from types import ModuleType
from typing import List, Union

import scipy


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    met_list = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType")
            met = getattr(mod, method_name, None)
            if callable(met):
                met_list.append(met)
        except ImportError:
            continue
    return met_list


if __name__ == "__main__":
    print(methods_importer("__import__", ["builtins"]))
    # <built-in function __import__>

    print(methods_importer("nothing", ["builtins"]))
    # None

    print(methods_importer("sum", [math, builtins, scipy]))
    # <built-in function sum>
