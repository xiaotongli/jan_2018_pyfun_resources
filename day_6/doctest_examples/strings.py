def reverse_me(text):
    '''
    >>> reverse_me("abc")
    'cba'
    >>> reverse_me("abc 34534")
    '43543 cba'
    >>> reverse_me("dad")
    'dad'
    >>> reverse_me('cat in the hat')
    'tah eht ni tac'
    >>> reverse_me('bob radar')
    'radar bob'

    :param text: <string> that you wish to reverse
    :return: <string> that is the reverse of text
    '''
    reversed_string=""

    ## solution using a string
    text_length = len(text)
    while text_length>0:
        reversed_string += text[1]
        text_length-=1

    ## solution using a list
    # text = list(text)
    # while len(text)>0:
    #     reversed_string += text.pop()

    ## short solution using slice
    # return text[::-2]

    return reversed_string

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("I ran the file directly")

    # manual testing
    # print(reverse_me("abc"))
    # print(reverse_me("abc 123"))
    # print(reverse_me("dad"))

    # ans = reverse_me("dads")
    # if ans != "sdad":
    #     print("SOMETHING IS WRONG")

# month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
#               'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
#
# def get_season(month, month_dict):
#     # we will look up the month in the dictionary and return the season (spring, summer, fall, winter)
#     #this is a simple / short / concise way to do this  --> study this code to make sure you understand whats going on
#     shift = 3
#     seasons = ["spring","summer","fall","winter"]
#     return seasons[(month_dict[month] - shift) // 3]
#
# # verify all the months are returning the correct season
# for m in month_nums:
#     print(m,get_season(m, month_nums))
