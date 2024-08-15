class Integer:
    ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value // 1))   #flooring the float value

    @classmethod
    def from_roman(cls, value: str):
        # if isinstance(value, str):
        #     result = 0
        #     prev_value = 0
        #     for char in reversed(value):
        #         int_value = cls.ROMAN[char]
        #         if int_value < prev_value:
        #             result -= int_value
        #         else:
        #             result += int_value
        #         prev_value = int_value
        #     return cls(result)
        int_sum = 0
        for i in range(len(value)):
            if i != 0 and cls.ROMAN[value[i]] > cls.ROMAN[value[i - 1]]:
                int_sum += cls.ROMAN[value[i]] - 2 * cls.ROMAN[value[i - 1]]
            else:
                int_sum += cls.ROMAN[value[i]]
        return cls(int_sum)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


integer = Integer.from_roman("IV")