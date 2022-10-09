"""
Given a string s containing algebraic expressions which contains alphabets from
A-Z and parentheses '(', ')', '{', '}', '[' and ']', determine if the input
string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Examples:
    (A+B)+(C-D)     : Valid as expression has brackets which have same type of opening and closing brackets
    (A+B)+(C-       : Invalid as closing brace is missing
    {(A+B)+[C-D]}   : Valid as opening and closing brackets are of same type
    ((A+B)-[C+D]}   : Invalid as The last closing bracket does not correspond to opening bracket
"""

from Stack import Stack

"""
    Time Complexity : O(n) due to traversal of the expression string
    Space Complexity : O(n) due to stack
"""

OPEN_ITEMS = (
    "(",
    "{",
    "[",
)

CLOSE_ITEMS = [
    ")",
    "}",
    "]",
]


def check_valid_parentheses(expression: str) -> bool:
    st = Stack()

    for item in expression:
        if item in OPEN_ITEMS:
            st.push(item)
        elif item in CLOSE_ITEMS:
            if st.is_empty():
                return False

            last_item = st.peek()

            if (
                item == ")" and last_item != "("
                or item == "}" and last_item != "{"
                or item == "]" and last_item != "["
            ):
                return False

            st.pop()

    if not st.is_empty():
        return False

    return True


if __name__ == "__main__":
    assert check_valid_parentheses("{(A+B)+[C-D]}") == True, "{(A+B)+[C-D]} is True"
    assert check_valid_parentheses("(A+B)+(C-") == False, "(A+B)+(C- is False"
    assert check_valid_parentheses("((A+B)-[C+D]}") == False, "((A+B)-[C+D]} is False"
    assert check_valid_parentheses("}(A-B){") == False, "}(A-B){ is False"
