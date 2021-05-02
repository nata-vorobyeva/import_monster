# -*- coding: utf-8 -*-
# import math
import types

# import numpy as np
# import pytest
import tests.test_module as t
from import_monster import methods_importer


class TestImportMonster:
    def test_callable_method(self):
        assert isinstance(t, types.ModuleType)
        isok = methods_importer(
            method_name="test_callable", modules=[t])
        assert isok == [t.test_callable]

    def test_const(self):
        assert isinstance(t, types.ModuleType)
        isok = methods_importer(method_name="const", modules=[t])
        assert isok == []

    def test_non_callable_method(self):
        assert isinstance(t, types.ModuleType)
        isok = methods_importer(
            method_name="test_non_callable", modules=[t])
        assert isok == []

    # def test_incorrect_type(self):
    #     with pytest.raises(TypeError):
    #         methods_importer(method_name="test_callable", modules=[1])
    #
    # def test_str_module(self):
    #     isok = methods_importer(method_name="mean", modules=["numpy"])
    #     assert isok == [np.mean]
    #
    # def test_two_modules_callable(self):
    #     isok = methods_importer(method_name="sin", modules=["numpy", "math"])
    #     assert isok == [np.sin, math.sin]
    #
    # def test_two_more_modules_callable(self):
    #     isok = methods_importer(method_name="mean", modules=["numpy", t])
    #     assert isok == [np.mean, t.mean]
    #
    # def two_modules_non_callable_test(self):
    #     isok = methods_importer(method_name="pi", modules=["numpy", "math"])
    #     assert isok == []
    #
    # def test_methods_importer_other_module(self):
    #     isok = methods_importer(method_name="mean", modules=[t, "other"])
    #     assert isok == [t.mean]
