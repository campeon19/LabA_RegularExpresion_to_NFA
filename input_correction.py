# Validate that the regular expression is valid

import re


def validate_regex(regex):
    try:
        # Verificar si hay dos o más operadores | consecutivos
        if re.search(r"\|\|", regex):
            raise re.error("Hay dos o más operadores | consecutivos")
        elif re.search(r"\|\)", regex):
            raise re.error(
                "Hay un operador | seguido de un paréntesis de cierre")
        elif re.search(r"\(\|", regex):
            raise re.error(
                "Hay un paréntesis de apertura seguido de un operador |")
        elif re.search(r"\(\)", regex):
            raise re.error(
                "Hay un paréntesis de apertura seguido de un paréntesis de cierre sin nada entre ellos")
        elif re.search(r"\(\*", regex):
            raise re.error(
                "Hay un paréntesis de apertura seguido de un operador *")
        elif re.search(r"\(\?", regex):
            raise re.error(
                "Hay un paréntesis de apertura seguido de un operador ?")
        elif re.search(r"\(\+", regex):
            raise re.error(
                "Hay un paréntesis de apertura seguido de un operador +")
        # Verificar si hay un caracter alfanumérico antes y despues de |
        elif re.search(r"\|", regex):
            if re.search(r"\|", regex).start() == 0 or re.search(r"\|", regex).end() == len(regex):
                raise re.error(
                    "Hay un operador | al inicio o al final de la expresión regular o no hay un simbolo antes y/o después de él")

        re.compile(regex)
        print("La expresión regular es válida")
        return True
    except re.error as e:
        # print(e)
        print("La expresión regular no es válida: {}".format(str(e)))
        return False


def main():
    # regex = input("Enter a regular expression: ")
    # validate_regex(regex)
    print(validate_regex("a||"))    # False
    print(validate_regex("(a|)"))   # False
    print(validate_regex("((a|b)"))  # False
    print(validate_regex("|b"))     # False
    print(validate_regex("?a|b"))  # False
    print(validate_regex("()"))     # False
    print(validate_regex("a|b"))   # True


if __name__ == "__main__":
    main()
