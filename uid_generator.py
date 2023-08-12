import random


class UIDGenerator:
    id_seed = 4220

    @staticmethod
    def generate_random_number_string(length):
        return ''.join([str(random.randint(0, 9)) for _ in range(length)])

    @staticmethod
    def decimal_to_hexavigesimal(value):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        while value > 0:
            remainder = value % 26
            result = alphabet[remainder] + result
            value = value // 26
        return result

    @classmethod
    def generate_id(cls):
        random_number = cls.generate_random_number_string(3)
        random_string = cls.decimal_to_hexavigesimal(cls.id_seed)
        cls.id_seed += 1
        return f"{random_number}-{random_string}"
