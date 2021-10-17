from src.ufu_token import UfuTokenType, UfuToken


class ScanIntException(Exception):
    pass


class ScanInt:
    __init_state = 0
    __accepted_state = 3
    __creating_int = 2

    def scan(self, text: str) -> UfuToken:
        current_state = self.__init_state
        int_value = ''
        current_index = 0

        while current_state != self.__accepted_state:
            current_char = text[current_index]
            if current_state == self.__init_state:

                if current_char.isdigit():
                    current_state = self.__creating_int
                    int_value += current_char
                else:
                    raise ScanIntException('unrecognised symbol')

            if current_state == self.__creating_int:

                if current_char.isdigit():
                    int_value += current_char
                elif current_char == ';':
                    current_state = self.__accepted_state
                else:
                    raise ScanIntException('unrecognised symbol')

            if current_state == self.__accepted_state:
                return UfuToken(UfuTokenType.INT, int_value)

            current_index += 1
