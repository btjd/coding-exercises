"""
LeetCode 17
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the 
number could represent.
A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.
"""
# def mnemonics(phone_number):
#     mapper = [' ', ' ', 'abc', 'def', 'ghi', 
#                'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#     result = []
#     mnemonic = [''] * len(phone_number)
#     def _helper(digit):
#         if digit == len(phone_number):
#             return result.append(''.join(mnemonic))
#         for letter in mapper[int(phone_number[digit])]:
#             mnemonic[digit] = letter
#             _helper(digit + 1)
#     _helper(0)
#     return result
# print(mnemonics('23'))

# The attempt below doesn't work because when
# using two for loops, we create more permutations
# than we need, for a '23' input we get:
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf', 'dd', 'de', 'df', 'ed', 'ee', 'ef', 'fd', 'fe', 'ff']
# We want just one loop so we get 'abc', the letters of 2
# to be the only top letters in the recursive tree, otherwise
# rcursion will apply to all the mappings of all the digits in the
# phone number. We can see that correction made in the implementation
# below this one, the correction was, instead of using phone_list[1:]
# we instead use a digit_index pointer that we increment with every 
# recursive call to allow us to traverse the phone number linearly.
# def menmo(phone_number):
#     phone_list = list(phone_number)
#     mnemonic = ''
#     result = []
#     mapper = [' ', ' ', 'abc', 'def', 'ghi', 
#     'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
#     def _helper(phone_list, mnemonic, result):
#         if phone_list == []:
#             result.append(mnemonic)
#             # print "        result is: ", result
#         for digit in phone_list:
#             print "current digit is: ", digit
#             print "current phone list is: ", phone_list
#             for letter in mapper[int(digit)]:
#                 print "    current letter is: ", letter
#                 print "    ", mnemonic+letter, phone_list[1:]
#                 _helper(phone_list[1:], mnemonic + letter, result)
#     _helper(phone_list, mnemonic, result)
#     return result
# print(menmo('23'))

def mnemonic(phone_number):
    letter_combo = ''
    result = []
    mapper = [' ', ' ', 'abc', 'def', 'ghi', 
    'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def _helper(digit_index, letter_combo):
        if digit_index == len(phone_number):
            result.append(letter_combo)
        else:
            for letter in mapper[int(phone_number[digit_index])]:
                _helper(digit_index + 1, letter_combo + letter)
    _helper(0, letter_combo)
    return result

def test_mnemonic():
    assert mnemonic('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

