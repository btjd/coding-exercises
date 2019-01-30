"""
LeetCode 929
"""
def unique_emails(emails):
    res = set()
    for email in emails:
        l_email = list(email)
        i = 0
        while i < len(l_email)-1 and l_email != '@':
            if l_email[i] == '+':
                j = i+1
                while l_email[j] != '@':
                    j += 1
                print l_email, i, j
                print ''.join(l_email[:i]), ''.join(l_email[j:])
                res.add(''.join(l_email[:i]+l_email[j:]))
                break
            if l_email[i] == '.':
                l_email.pop(i)
                i += 1
            else:
                i += 1
        
    print res
    return len(res)

# print unique_emails(['test.email+alex@leetcode.com'])
# print unique_emails(['test.e.mail+bob.cathy@leetcode.com'])
print unique_emails(['testemail+david@lee.tcode.com'])