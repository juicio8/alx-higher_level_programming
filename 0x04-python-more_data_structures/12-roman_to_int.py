#!/usr/bin/python3
nt(roman_string):
    if isinstance(roman_string, str):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000}
        string = list(roman_string)
        print(string)
        sum = 0
        for i in string:
            if string.index(i) < len(string)-1:
                if roman[i] < roman[(string[string.index(i)+1])]:
                    sum -= roman[i]
                else:
                    sum += roman[i]
            else:
                sum += roman[i]
        return sum
