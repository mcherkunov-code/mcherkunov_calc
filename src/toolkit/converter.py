def convert(value: float, from_unit: str, to_unit: str):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    length_units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
    }

    mass_units = {
        'g': 1.0,
        'kg': 1000.0,
    }

    temperature_units = {'c', 'f', 'k'}

    all_units = set(length_units) | set(mass_units) | temperature_units

    if from_unit not in all_units or to_unit not in all_units:
        raise ValueError('Неизвестная единица')

    if from_unit in temperature_units and to_unit in temperature_units:
        if from_unit == 'c':
            celsius = value
        elif from_unit == 'f':
            celsius = (value - 32) * 5 / 9
        elif from_unit == 'k':
            celsius = value - 273.15

        if celsius < -273.15:
            raise ValueError('Температура ниже абсолютного нуля')

        if from_unit == to_unit:
            return float(value)


        if to_unit == 'c':
            return float(celsius)
        elif to_unit == 'f':
            return float(celsius * 9 / 5 + 32)
        elif to_unit == 'k':
            return float(celsius + 273.15)
    elif from_unit in length_units and to_unit in length_units:
        units = length_units
    elif from_unit in mass_units and to_unit in mass_units:
        units = mass_units
    else:
        raise ValueError('Несовместимые единицы!')

    from_value = units[from_unit]
    to_value = units[to_unit]

    result = value * from_value / to_value

    return float(result)
