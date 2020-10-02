"""
Given a string s containing algebraic expressions which contains alphabets from A-Z and parentheses '(', ')',
'{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Examples:
    (A+B)+(C-D)     : Valid as expression has brackets which have same type of opening and closing brackets
    (A+B)+(C-       : Invalid as closing brace is missing
    {(A+B)+[C-D]}   : Valid as opening and closing brackets are of same type
    ((A+B)-[C+D]}   : Invalid as The last closing bracket does not correspond to opening bracket
"""

from python.Stack.Stack import Stack

"""
    Time Complexity : O(n) due to traversal of the expression string
    Space Complexity : O(n) due to stack
"""


def check_valid_parentheses(expression):
    st = Stack()
    valid = True

    for i in expression:
        if i in "({[":
            st.push(i)
        elif i in ")}]":
            if st.is_empty():
                valid = False
                break
            elif (i == ")" and st.peek() != "(") or (i == "}" and st.peek() != "{") or (i == "]" and st.peek() != "["):
                valid = False
                break
            else:
                st.pop()

    if not st.is_empty():
        valid = False

    return valid


if __name__ == "__main__":
    print(check_valid_parentheses("{(A+B)+[C-D]}"))  # Valid
    print(check_valid_parentheses("(A+B)+(C-"))  # Invalid
    print(check_valid_parentheses("((A+B)-[C+D]}"))  # Invalid
    print(check_valid_parentheses("}(A-B){"))  # Invalid
