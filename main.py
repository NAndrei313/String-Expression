import re


def string_expression(str_param):
    new_string = str_param[:]
    number_list = [
        ('zero', '0'),
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9'),
        ('minus', '-'),
        ('plus', '+')
    ]

    # Replace words with corresponding numbers and operators
    for word, digit in number_list:
        new_string = re.sub(word, digit, new_string)

    # Evaluate the expression
    result = eval(new_string)
    result_str = str(result)

    # Replace numbers back with words in the result
    for word, digit in number_list[:10]:    # Only use 0-9 for replacement
        result_str = re.sub(digit, word, result_str)

    # Replace '-' with 'negative' if result is negative
    result_str = result_str.replace('-', 'negative')

    return result_str


# Test the function with an input string
print(string_expression(input()))
