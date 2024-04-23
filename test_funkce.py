from funkce import deslabikace
import pytest


def test_deslabikace():
    """
    Test funkce deslabikace.
    """
    #test krátkých slov
    assert deslabikace("a") == "a"
    assert deslabikace("ab") == "ab"
    assert deslabikace("abc") == "abc"
    #test 4 písmena
    assert deslabikace("abcd") == "acbd"
    #test nestandartního zadání
    assert deslabikace("***Zdar***") == "***Zadr***"
    assert deslabikace("-4()*/abcd845") == "-4()*/acbd845"
    #test čísla
    with pytest.raises(ValueError):
        deslabikace("123456")
    #test prázdného zadání
    with pytest.raises(ValueError):
        deslabikace("")
import os
from funkce import cls


"""def test_cls_windows():
    # Simulace Windows 
    os.name = "nt"

    cls()

    # Argument os.system. by měl být cls
    assert os.system.call_args == (("cls",),)"""

"""def test_cls_linux():
    # Simulace Linux
    os.name = "posix"

    cls()

    # Argument os.system. by měl být clear
    assert os.system.call_args == (("clear",),)

def test_cls_other():
    os.name != "nt" """
