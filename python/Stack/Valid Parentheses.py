"""
Given a string containing algebraic expressions with alphabets (A-Z) and specific parentheses ('(', ')', '{', '}', '[', ']'),
determine if the input string is valid.

An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

Examples:
    (A+B)+(C-D)     : Valid as the expression has matching opening and closing brackets.
    (A+B)+(C-       : Invalid as a closing bracket is missing.
    {(A+B)+[C-D]}   : Valid as opening and closing brackets match correctly.
    ((A+B)-[C+D]}   : Invalid as the last closing bracket does not correspond to an opening bracket.
"""

from python.Stack.Stack import Stack

"""
    Time Complexity : O(n) due to traversal of the expression string
    Space Complexity : O(n) due to stack
"""

def check_valid_parentheses(expression):
    stack = Stack()
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in parentheses_map.values():
            stack.push(char)
        elif char in parentheses_map:
            if stack.is_empty() or stack.pop() != parentheses_map[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    print(check_valid_parentheses("{(A+B)+[C-D]}"))  # Valid
    print(check_valid_parentheses("(A+B)+(C-"))  # Invalid
    print(check_valid_parentheses("((A+B)-[C+D]}"))  # Invalid
    print(check_valid_parentheses("}(A-B){"))  # Invalid
