import pytest
from io import StringIO
from unittest.mock import patch
import funkce
import main
import sys

"""# Test pro hlavní menu
@patch('builtins.input', side_effect=['1', 'test text', '1'])
def test_FunkceMainMenu_input_1(mock_input):
    output = StringIO()
    sys.stdout = output

    main.FunkceMainMenu()

    sys.stdout = sys.__stdout__  # Obnova standardního výstupu

    assert "Text byl úspěšně uložen do souboru" in output.getvalue()
    assert "Nashledanou" in output.getvalue()"""

"""# Test pro druhé menu
@patch('builtins.input', side_effect=['1', '2', '1'])
def test_FunkceMenu2_input_1(mock_input):
    output = StringIO()
    sys.stdout = output

    main.FunkceMenu2("Testovací text", "Vstupní text")

    sys.stdout = sys.__stdout__  # Obnova standardního výstupu

    assert "Stiskněte enter pro ukončení" in output.getvalue()
    assert "Text byl úspěšně uložen do souboru" in output.getvalue()
    assert "Nashledanou" in output.getvalue()
"""