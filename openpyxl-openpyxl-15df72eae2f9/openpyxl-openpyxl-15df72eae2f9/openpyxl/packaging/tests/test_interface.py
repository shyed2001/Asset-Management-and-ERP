# Copyright (c) 2010-2019 openpyxl

import pytest

def test_interface():
    from ..interface import ISerialisableFile

    class DummyFile(ISerialisableFile):

        pass

    with pytest.raises(TypeError):

        df = DummyFile()
