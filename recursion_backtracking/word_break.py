# def word_break(s, wordDict):
#     if s == '':
#         print "end"
#         return True
#     else:
#         filtered_word_dict = [w for w in wordDict if w[0]==s[0]]
#         if filtered_word_dict == []:
#             return False
#         else:
#             for word in filtered_word_dict:
#                 print filtered_word_dict
#                 print word, s
#                 if s[:len(word)] == word:
#                     return word_break(s[len(word):], wordDict)
#                 else:
#                     return False


def word_break(s, wordDict):
    def _helper(s, wordDict, result):
        print s, result
        if s == '':
            print "end"
            result.append('matched')
            return result
        else:
            filtered_word_dict = [w for w in wordDict if w[0]==s[0]]
            if filtered_word_dict == []:
                return
            else:
                for word in filtered_word_dict:
                    print "    ", filtered_word_dict
                    print "    ", word, s
                    print "    ", s[:len(word)]
                    if s[:len(word)] == word:
                        _helper(s[len(word):], wordDict, result)
                    else:
                        return
    result = []
    _helper(s, wordDict, result)
    if result:
        return True
    else:
        return False


# print(word_break("applepenapple", ["apple", "pen"]))
# print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
# print(word_break("cars", ["car", "ca","rs"]))
print(word_break("bccdbacdbdacddabbaaaadababadad", ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]))