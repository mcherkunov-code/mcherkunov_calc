"""Командный интерфейс калькулятора и конвертера"""

import argparse
import sys

from .calculator import evaluate
from .converter import convert

parser = argparse.ArgumentParser(
    # Создаём команды, которые пользователь может вызвать из терминала.
    prog="python -m toolkit",
    description="Calculator and unit converter",
)

commands = parser.add_subparsers(
    dest="command",
    required=True,
)


calc_parser = commands.add_parser(
    "calc",
    help="Calculate an expression",
)

calc_parser.add_argument(
    "expression",
    help="Arithmetic expression",
)


convert_parser = commands.add_parser(
    "convert",
    help="Convert a value between units",
)

convert_parser.add_argument(
    "value",
    type=float,
    help="Value to convert",
)

convert_parser.add_argument(
    "--from",
    dest="from_unit",
    required=True,
    help="Source unit",
)

convert_parser.add_argument(
    "--to",
    dest="to_unit",
    required=True,
    help="Target unit",
)

args = parser.parse_args()

try: # Ошибки вычисления и конвертации выводим в stderr и возвращаем код 2
    if args.command == "calc":
        print(evaluate(args.expression))

    elif args.command == "convert":
        print(convert(args.value, args.from_unit, args.to_unit))

except (ValueError, ZeroDivisionError) as error:
    print(f"Ошибка: {error}", file=sys.stderr)
    raise SystemExit(2) # Код 2 используется для ошибок пользовательского ввода
