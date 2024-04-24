from funkce import deslabikace
import math

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
    assert deslabikace("odla") == "olda"
    #test nestandartního zadání
    assert deslabikace("***Zdar***") == "***Zadr***"
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

"""class TestUlozSoubor(unittest.TestCase):

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
    unittest.main()"""




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
import unittest
import os
from funkce import NactiSoubor  # Replace 'your_module' with your module name

def test_NactiSoubor_existing_file():
    # Test reading an existing file
    test_folder = "soubory"
    test_filename = "test.txt"
    test_file_content = "Hello, world!"

    # Create a test folder and a test file with content
    os.makedirs(test_folder, exist_ok=True)
    with open(os.path.join(test_folder, test_filename), 'w', encoding='utf-8') as file:
        file.write(test_file_content)

    # Call the function to read the test file
    try:
        result = NactiSoubor(test_filename)
        assert result == test_file_content
    except FileNotFoundError:
        assert False, "NactiSoubor raised FileNotFoundError unexpectedly"

    # Clean up: Remove the test folder and its contents
    if os.path.exists(test_folder):
        import shutil
        shutil.rmtree(test_folder)

def test_NactiSoubor_non_existing_file():
    # Test trying to read a non-existing file
    non_existing_filename = "non_existing_file.txt"

    # Call the function with a non-existing file
    with unittest.TestCase().assertRaises(FileNotFoundError):
        NactiSoubor(non_existing_filename)

def test_NactiSoubor_invalid_folder():
    # Test trying to read from a non-existing folder
    invalid_folder = "invalid_folder"
    invalid_filename = "test.txt"

    # Call the function with an invalid folder
    with unittest.TestCase().assertRaises(FileNotFoundError):
        NactiSoubor(os.path.join(invalid_folder, invalid_filename))

if __name__ == '__main__':
    test_NactiSoubor_existing_file()
    test_NactiSoubor_non_existing_file()
    test_NactiSoubor_invalid_folder()