"""
    Module with the main class for the calculator.
"""

from enum import Enum

class Operations(Enum):
    SUM  = 'a'
    SUBS = 'b'
    MULT = 'c'
    DIV  = 'd'

class Calculator():
    """My Calculator."""

    operations = {
        Operations.SUM.value: 'sumar', 
        Operations.SUBS.value: 'restar', 
        Operations.MULT.value: 'multiplicar',
        Operations.DIV.value: 'dividir'
    }

    def run_calculator(self):
        """Main method to run the calculator."""

        print('\nCALCULATOR\n----------')
        while self._run_calculator():
            pass
        print('\n¡Hasta la próxima!\n')

    def _run_calculator(self):
        """Method that runs the calculator."""

        while (option := self._select_option()) not in self.operations.keys():
            if option == 'q':
                return False
            print(f'\nOpción no válida.')

        while not (values := self._ask_for_input_values(option)):
            pass

        result = self._perform_operation(option, values)
        print(f'\nRESULTADO: {result}')

        while (other_operation := input('\n¿Desea realizar otra operación (s/n)?: ').strip().lower()) not in ['s', 'n']:
            print('\nPor favor, introduzca "s" para realizar otra operación o "n" para salir.')

        return True if other_operation == 's' else False

    def _select_option(self):
        """Method to ask the user which action to perform."""

        print('\n¿Qué operación desea realizar?\n')
        for option, action in self.operations.items():
            print(f'  {option}) {action.capitalize()}')
        print('\nIntroduzca "q" para salir.')

        return input('\nElija una opción: ').strip().lower()

    def _ask_for_input_values(self, option):
        """Method to get the input values for the operation from the user."""

        values = input(f'\nIntroduzca los valores que desea {self.operations[option]} separados por comas: ').strip(',').split(',')
        values = self._cast_input_values_as_integers(values)
        all_positive = self._check_all_input_values_are_positive(values)
        valid_number_of_input_values = self._check_valid_number_of_input_values(values, option)

        return [] if not values or not all_positive or not valid_number_of_input_values else values

    def _cast_input_values_as_integers(self, values):
        """Method to cast all the values introduced by the user as integers."""

        try:
            values = [int(value) for value in values]
        except ValueError:
            print('\nAlguno de los valores introducidos no es válido. Todos los valores deben ser números enteros.')
            values = []

        return values

    def _check_all_input_values_are_positive(self, values):
        """Method that checks that all the introduced values are positive."""

        all_positive = all(value >= 0 for value in values)
        if not all_positive:
            print('\nEsta calculadora sólo funciona con valores positivos actualmente.')

        return all_positive

    def _check_valid_number_of_input_values(self, values, option):
        """Method to check if the number of input values is valid."""

        valid_number_of_input_values = True

        if option in [Operations.SUM.value, Operations.MULT.value] and len(values) <= 1: 
            valid_number_of_input_values = False
            print('\nPara sumar o multiplicar se debe introducir al menos 1 valor.')

        if option in [Operations.SUBS.value, Operations.DIV.value] and len(values) != 2:
            valid_number_of_input_values = False
            print('\nPara restar o dividir se deben introducir exactamente 2 valores.')

        return valid_number_of_input_values

    def _perform_operation(self, option, values):
        """Method to perform the operation specified by the user."""

        if option == Operations.SUM.value:
            result = self._sum_values(values)

        if option == Operations.SUBS.value:
            result = self._substract_values(values)

        if option == Operations.MULT.value:
            result = self._multiply_values(values)

        if option == Operations.DIV.value:
            result = self._divide_values(values)

        return result

    def _sum_values(self, values):
        """Method to sum all the values in the values collection."""

        return len([1 for value in values for _ in range(value)])

    def _substract_values(self, values):
        """Method to substract the second value in values from the first one."""

        result = [1 for _ in range(values[0])]
        if_negative_result = []
        for _ in range(values[1]):
            try:
                result.pop()
            except IndexError:
                if_negative_result.append(1)

        return -len(if_negative_result) if if_negative_result else len(result)

    def _multiply_values(self, values):
        """Method to multiply all the values in the values collection."""

        result = values[0]
        for value in values[1:]:
            result = self._multiply_two_values(result, value)

        return result

    def _multiply_two_values(self, value_1, value_2):
        """Method to multiply two values."""

        return len([1 for _ in range(value_1) for _ in range(value_2)])

    def _divide_values(self, values):
        """Method to divide two values."""

        print('\nEsta operación no está disponible actualmente.')

if __name__ == '__main__':

    calculator = Calculator()
    calculator.run_calculator()
