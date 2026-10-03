def tokenize(expression: str):
    tokens: list[tuple[str, float | str]] = []
    state = "START"
    current_token = ""
    expect_number = True

    for char in expression:
        if state == "START":
            if char.isdigit():
                state = "NUMBER"
                current_token = char
                expect_number = False
            elif char in "+-":
                if expect_number:
                    current_token = char
                    state = "SIGNED_NUMBER"
                else:
                    tokens.append(("OPERATOR", char))
                    expect_number = True

            elif char in "*/":
                tokens.append(("OPERATOR", char))
                expect_number = True
            elif char.isspace():
                continue
            else:
                raise ValueError(f"Неизвестный символ: {char}")

        elif state == "SIGNED_NUMBER":
            if char.isdigit():
                current_token += char
                state = "NUMBER"
                expect_number = False
            else:
                raise ValueError("После знака ожидалось число")

        elif state == "NUMBER":
            if char.isdigit():
                current_token += char
            elif char == ".":
                current_token += char
                state = "DOT_AFTER_INT"
            else:
                tokens.append(("NUMBER", float(current_token)))
                current_token = ""
                state = "START"
                expect_number = False

                if char in "+-*/":
                    tokens.append(("OPERATOR", char))
                elif char.isspace():
                    continue
                else:
                    raise ValueError(f"Неизвестный символ: {char}")

        elif state == "DOT_AFTER_INT":
            if char.isdigit():
                current_token += char
                state = "NUMBER"
            else:
                raise ValueError("Некорректное число")

    if state == "NUMBER":
        tokens.append(("NUMBER", float(current_token)))

    return tokens


def validate(tokens):
    if not tokens:
        raise ValueError("Пустое выражение")

    if tokens[0][0] != "NUMBER":
        raise ValueError("Выражение должно начинаться с числа")

    if tokens[-1][0] != "NUMBER":
        raise ValueError("Выражение должно заканчиваться числом")

    for i in range(len(tokens) - 1):
        current_type = tokens[i][0]
        next_type = tokens[i + 1][0]

        if current_type == "NUMBER" and next_type == "NUMBER":
            raise ValueError("Между числами пропущен оператор")

        if current_type == "OPERATOR" and next_type == "OPERATOR":
            raise ValueError("Два оператора идут подряд")


def calculate(tokens):
    acc = tokens[0][1]
    reduced = []
    i = 1

    while i < len(tokens):
        operator = tokens[i][1]
        number = tokens[i + 1][1]

        if operator == "*":
            acc *= number
            i += 2
            continue

        if operator == "/":
            if number == 0:
                raise ValueError("Попытка деления на 0")
            acc /= number
            i += 2
            continue

        reduced.append(acc)
        reduced.append(operator)
        acc = number
        i += 2

    reduced.append(acc)

    result = reduced[0]
    i = 1

    while i < len(reduced):
        operator = reduced[i]
        number = reduced[i + 1]

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number

        i += 2

    return result


def evaluate(expression: str):
    tokens = tokenize(expression)
    validate(tokens)
    return calculate(tokens)
