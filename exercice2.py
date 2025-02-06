import time

my_global = "ma_variable_globale"

def my_arg(argument):
    ma_variable_locale = "ma_variable_locale"

    variables = [my_global, argument, ma_variable_locale]

    for var in variables:
        print(var)
        time.sleep(1111111111)

my_arg("ma_variable_argument")