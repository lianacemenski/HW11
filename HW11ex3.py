class UserNotNumberError(Exception):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def valid_number(number):
        try:
            return True if float(number) else True
        except ValueError:
            return False


def main():
    numbers_list = []
    while True:
        number = input('Введите число или "stop" для выхода: ')
        if number == 'stop':
            break
        try:
            if UserNotNumberError.valid_number(number):
                numbers_list.append(float(number))
            else:
                raise UserNotNumberError("Вы ввели не число!")
        except UserNotNumberError as ex:
            print(ex)
            continue
    print(numbers_list)


if __name__ == '__main__':
    main()
