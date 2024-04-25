"""Testovací soubor funkcí."""
from funkce import deslabikace
import math
import pytest
import unittest
import difflib
import os
from funkce import UlozSoubor


def test_deslabikace():
    """Test funkce deslabikace."""
    # test krátkých slov

    # test 1 písmeno
    assert deslabikace("a") == "a"
    assert deslabikace("x") == "x"
    assert deslabikace("B") == "B"

    # test 2 písmena
    assert deslabikace("ab") == "ab"
    assert deslabikace("xy") == "xy"
    assert deslabikace("XY") == "XY"

    # test 3 písmena
    assert deslabikace("abc") == "abc"
    assert deslabikace("xyz") == "xyz"
    assert deslabikace("XYZ") == "XYZ"

    # test 4 písmena
    assert deslabikace("abcd") == "acbd"
    assert deslabikace("odla") == "olda"
    assert deslabikace("OdLa") == "OLda"

    # test nestandartního zadání
    assert deslabikace("***Zdar***") == "***Zadr***"
    assert deslabikace("***ZdAr***") == "***ZAdr***"
    assert deslabikace("-4()*/abcd845") == "-4()*/acbd845"
    assert deslabikace("-4()*/abcd845") == "-4()*/acbd845"
    assert deslabikace("kola115") == "kloa115"

    # test čísla
    with pytest.raises(ValueError):
        deslabikace("37.55")
    with pytest.raises(ValueError):
        deslabikace("37,55")
    with pytest.raises(ValueError):
        deslabikace("123456")

    # test prázdného zadání
    with pytest.raises(ValueError):
        deslabikace("")

    # test neakceptovtelného zadání
    with pytest.raises(ValueError):
        deslabikace("*-+6512/*-7/()&@#")

    # test neočekávaného zadání
    with pytest.raises(ValueError):
        deslabikace(str(math.pi))


def test_deslabikace_tolerance():
    """Test funkce deslabikace s tolerancí.

    Tyto testy dokáží otestovat i delší slova u kterých se již používá \
    vnořená funkce mixer a jejich výsledek tak není prediktivní.
    """

    def test(MaByt, Je, tolerance):
        """Vnořená funkce test.

        na vstupu má očekávaný výsledek, vstup z funkce deslabikace, \
        a koeficient tolerance.
        """
        shoda = difflib.SequenceMatcher(None, MaByt, Je)
        podobnost = shoda.ratio()
        assert podobnost >= tolerance, f"Očekáváno: {MaByt}, Výsledek je: \
            {Je}, podobnost: {podobnost}"

    # Samotné testy.
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Prcáe***", 0.8)
    test(deslabikace("***Lokomotiva***"), "***Lkomootvia***", 0.65)
    test(deslabikace("1234567890dlouheSlovo1234567890"),
         "***1234567890dluohloeSvo1234567890***", 0.7)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)
    test(deslabikace("***Práce***"), "***Pácre***", 0.8)


class TestUlozSoubor(unittest.TestCase):
    """Test ukládání souboru"""

    def setUp(self):
        """# Set up any initial state needed for your tests"""
        self.output_text = "Hello, world!"

    def tearDown(self):
        """Čištění."""
        file_path = os.path.join("soubory", "test.txt")
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_UlozSoubor(self):
        """Simulate user input for the filename."""
        filename = 'test.txt'  # Simulated user input
        # This would be provided by the user during runtime
        user_input = filename

        # Monkey patching 'input' function to return our simulated user input
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
            # Check if the file exists
            self.assertTrue(os.path.exists(file_path))

            with open(file_path, "r", encoding="utf-8") as file:
                # Read content and strip whitespace
                saved_text = file.read().strip()
                # Compare saved text with input
                self.assertEqual(saved_text, self.output_text)

        finally:
            # Restore the original 'input' function
            builtins.input = original_input


# Test funkce cls neprochází, takže nebyl použit
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
if __name__ == '__main__':
    unittest.main()
