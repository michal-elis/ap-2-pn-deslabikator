from funkce import deslabikace


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
    assert deslabikace("123456") == "123456"
    assert deslabikace("aaaaaaaa") == "aaaaaaaa"
    assert deslabikace("aaaaaaaaa") == "aaaaaaaaa"
    assert deslabikace("aaaaaaaaaa") == "aaaaaaaaaa"
    assert deslabikace("aaaaaaaaaaa") == "aaaaaaaaaaa"
    assert deslabikace("aaaaaaaaaaaa") == "aaaaaaaaaaaa"
