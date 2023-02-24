# Validate that the regular expression is valid

import re


def validate_regex(regex):
    try:
        # Verificar si hay dos o más operadores | consecutivos
        if re.search(r'\|\|+', regex):
            raise re.error(
                "Dos o más operadores | consecutivos no están permitidos")

        # Compilar la expresión regular
        re.compile(regex)
        print("La expresión regular es válida")
    except re.error as e:
        print(e)
        print("La expresión regular no es válida: {}".format(str(e)))


def main():
    regex = input("Enter a regular expression: ")
    validate_regex(regex)


if __name__ == "__main__":
    main()
