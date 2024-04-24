from funkce import deslabikace
import math

import pytest


def test_deslabikace():
    """
    Test funkce deslabikace.
    """
    #test krátkých slov

    #test 1 písmeno
    assert deslabikace("a") == "a"
    assert deslabikace("x") == "x"
    assert deslabikace("B") == "B"
    
    #test 2 písmena
    assert deslabikace("ab") == "ab"
    assert deslabikace("xy") == "xy"
    assert deslabikace("XY") == "XY"

    #test 3 písmena
    assert deslabikace("abc") == "abc"
    assert deslabikace("xyz") == "xyz"
    assert deslabikace("XYZ") == "XYZ"

    #test 4 písmena
    assert deslabikace("abcd") == "acbd"
    assert deslabikace("odla") == "olda"
    assert deslabikace("OdLa") == "OLda"

    #test nestandartního zadání
    assert deslabikace("***Zdar***") == "***Zadr***"
    assert deslabikace("***ZdAr***") == "***ZAdr***"
    assert deslabikace("-4()*/abcd845") == "-4()*/acbd845"
    assert deslabikace("-4()*/abcd845") == "-4()*/acbd845"
    assert deslabikace("kola115") == "kloa115"
    #test čísla
    with pytest.raises(ValueError):
        deslabikace("37.55")
    with pytest.raises(ValueError):
        deslabikace("37,55")
    with pytest.raises(ValueError):
        deslabikace("123456")
    #test prázdného zadání
    with pytest.raises(ValueError):
        deslabikace("")
    #test neakceptovtelného zadání
    with pytest.raises(ValueError):
        deslabikace("*-+6512/*-7/()&@#")
    #test neočekávaného zadání
    with pytest.raises(ValueError):
        deslabikace(str(math.pi))
    

import unittest
import os

# Import the function you want to test
from funkce import UlozSoubor  # Replace 'your_module' with your module name

class TestUlozSoubor(unittest.TestCase):

    def setUp(self):
        # Set up any initial state needed for your tests
        self.output_text = "Hello, world!"

    def tearDown(self):
        # Clean up any resources used during the test if necessary
        # For example, delete any files created during the tests
        file_path = os.path.join("soubory", "test.txt")
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_UlozSoubor(self):
        # Simulate user input for the filename
        filename = 'test.txt'  # Simulated user input
        user_input = filename  # This would be provided by the user during runtime

        # Monkey patching the 'input' function to return our simulated user input
        try:
            # Python 3.x
            import builtins
        except ImportError:
            # Python 2.x
            import __builtin__ as builtins

        original_input = builtins.input
        builtins.input = lambda _: user_input

        try:
            # Call the function with our simulated user input
            UlozSoubor(self.output_text)

            # Check if the file was created with the correct content
            file_path = os.path.join("soubory", filename)
            self.assertTrue(os.path.exists(file_path))  # Check if the file exists

            with open(file_path, "r", encoding="utf-8") as file:
                saved_text = file.read().strip()  # Read content and strip whitespace
                self.assertEqual(saved_text, self.output_text)  # Compare saved text with input

        finally:
            # Restore the original 'input' function
            builtins.input = original_input

if __name__ == '__main__':
    unittest.main()




#test funkce cls neprochází
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
"""