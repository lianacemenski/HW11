import re


class Date:
    RE_SPLIT = re.compile(r'(\d{2}).(\d{2}).(\d{4})')

    def __init__(self, data):
        self.data = self.split_data(data)
        self.validator(self.data)

    @classmethod
    def split_data(cls, data):
        data_parsed = cls.RE_SPLIT.fullmatch(data)
        if not data_parsed:
            raise ValueError(f'wrong_data: {data}')
        return tuple(map(int, data_parsed.groups()))

    @staticmethod
    def validator(data_list):
        day, month, year = data_list
        if not (1 <= day <= 31):
            raise ValueError(f"wrong day")
        if not (1 <= month <= 12):
            raise ValueError(f"wrong month")
        return data_list

    def __str__(self):
        return f"{self.data}"


class AnotherDate(Date):
    RE_SPLIT = re.compile(r'(\d{4}).(\d{2}).(\d{2})')


if __name__ == "__main__":
    cur_day = Date("21-04-2021")
    print(cur_day)
    cur_day2 = Date("04-21-2021")
