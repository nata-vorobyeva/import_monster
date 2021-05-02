# -*- coding: utf-8 -*-
import math

import numpy as np
import pytest

from import_monster import methods_importer


class TestImportMonster:
    @pytest.mark.parametrize(
        "test_case,expected_result",
        [
            (("__import__", ["builtins"]), [__import__]),
            (("sqrt", ["numpy", "math", "builtins"]), [np.sqrt, math.sqrt]),
            (("min", ["numpy", "math", "builtins"]), [np.min, min]),
            (("nothing", ["builtins", "scipy"]), [])
        ],
    )
    def test_callable_list(self, test_case, expected_result):
        """
        Tests main functionality:
        search method name in list of modules and return list of modules containing this method
        """
        assert list(methods_importer(*test_case)) == expected_result

    def test_wrong_module_type(self):
        """
        Tests that the function methods_importer checks module type.
        If it's integer, the function should raise TypeError
        """
        with pytest.raises(TypeError):
            methods_importer(method_name="sum", modules=[int(42)])

    def test_output_type(self):
        """
        Tests that the function returns type List.
        If it's integer, function raises TypeError
        """
        case = methods_importer("nothing", ["builtins"])
        assert isinstance(case, list)
