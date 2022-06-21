def numbers_words_recursion(value):
    _20s = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
            "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", ]
    _10s = ["Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"]
    _100s = {100: "Hundred", 1000: "Thousand"}
    if value < 20:
        return _20s[value]
    elif value < 100:
        val = _10s[(int(value / 10) - 2)] + ("" if value % 10 == 0 else " " + _20s[value % 10])
        return val

    _num = [key for key in _100s.keys() if key <= value]
    _max_value = max(_num)
    return (
            numbers_words_recursion((int(value / _max_value))) + " " + _100s[_max_value] + (
        "" if value % _max_value == 0 else " and " + numbers_words_recursion(value % _max_value))
    )


if __name__ == '__main__':
    value = numbers_words_recursion(9090)
    print(value)
