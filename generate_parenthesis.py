"""
Using recursion/backtracking. There are three main cases
we deal with:
1) Base case is when we run out of open parenthesis,
   in which case, we just append the rest of the
   close parenthesis. ex. '((('
2) When we have an equal number of open and close
   parenthesis, we can only open, otherwise we create
   an imbalance where we have more open than close
   parenthesis. ex. '(())'
3) Lastly, when the number of close is greater than
   open parenthesis, we can go either way, so we
   address both cases. ex. '())'
See:
   - https://www.youtube.com/watch?v=sz1qaKt0KGQ
   - https://www.youtube.com/watch?v=LxwiwlUDOk4 
"""
def gen_paren(n):
    def _gen_paren(parens, opened, closed):
        if opened == 0:
            print(parens)
            print(parens + (')' * closed))
            return [parens + (')' * closed)]
        elif opened == closed:
            return _gen_paren(parens + ('('), opened - 1, closed)
        elif closed > opened:
            return _gen_paren(parens + ('('), opened - 1, closed) + _gen_paren(parens + ')', opened, closed - 1)
    if n == 0:
        return []
    else:
        return _gen_paren('', n, n)

print gen_paren(3)