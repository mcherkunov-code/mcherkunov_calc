import subprocess
import sys

import pytest

from toolkit.calculator import evaluate


def test_addition():
    assert evaluate('2 + 2') == 4.0


def test_subtraction():
    assert evaluate('9 - 2') == 7.0


def test_multiplication():
    assert evaluate('7 * 8') == 56.0


def test_division():
    assert evaluate('15 / 3') == 5.0


def test_spaces_are_ignored():
    assert evaluate(' 2  +   5  *    8') == 42.0


def test_unary_minus():
    assert evaluate('-9 - -3') == -6.0


def test_unary_plus():
    assert evaluate('+0 + 3') == 3.0


def test_float_numbers():
    assert evaluate('0.5 * 0.5') == 0.25


def test_integer_division():
    assert evaluate('10 // 3') == 3.0


def test_remainder_of_division():
    assert evaluate('10 % 3') == 1.0


def test_integer_division_negative():
    assert evaluate('-10 // 3') == -4.0


def test_remainder_of_division_negative():
    assert evaluate('-10 % 3') == 2.0


def test_empty_expression():
    with pytest.raises(ValueError):
        evaluate('')


def test_invalid_character():
    with pytest.raises(ValueError):
        evaluate('3 + Ab')


def test_missing_operand():
    with pytest.raises(ValueError):
        evaluate('3 4')


def test_two_operators_in_a_row():
    with pytest.raises(ValueError):
        evaluate('6 + * 3')


def test_division_by_zero():
    with pytest.raises(ValueError):
        evaluate('17 / 0')


def test_integer_division_by_zero():
    with pytest.raises(ValueError):
        evaluate('10 // 0')


def test_remainder_of_division_by_zero():
    with pytest.raises(ValueError):
        evaluate('10 % 0')


def test_cli_calculate():
    # Тесты ниже проверяют запуск программы через CLI, а не отдельные функции.
    result = subprocess.run(
        [
            sys.executable,
            '-m',
            'toolkit',
            'calc',
            '2 + 3 * 4',
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == '14.0\n'


def test_cli_division_by_zero():
    result = subprocess.run(
        [
            sys.executable,
            '-m',
            'toolkit',
            'calc',
            '10 / 0',
        ],
        capture_output=True,
        text=True,
        check=False,
       )

    assert result.returncode == 2
    assert 'Ошибка' in result.stderr
