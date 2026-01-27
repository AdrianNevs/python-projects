#calcular com closure
def tax_calculate(value):
    def calculate_value(tax):
        return value + (value * (tax / 100))
    return calculate_value
