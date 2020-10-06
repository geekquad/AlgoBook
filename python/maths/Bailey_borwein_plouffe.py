def bailey_borwein_plouffe(digit_position: int, precision: int = 1000) -> str:

    if (not isinstance(digit_position, int)) or (digit_position <= 0):
        raise ValueError("Digit position must be a positive integer")
    elif (not isinstance(precision, int)) or (precision < 0):
        raise ValueError("Precision must be a nonnegative integer")

    sum_result = (
        4 * _subsum(digit_position, 1, precision)
        - 2 * _subsum(digit_position, 4, precision)
        - _subsum(digit_position, 5, precision)
        - _subsum(digit_position, 6, precision)
    )

    return hex(int((sum_result % 1) * 16))[2:]


def _subsum(
    digit_pos_to_extract: int, denominator_addend: int, precision: int
) -> float:
    Private helper function to implement the summation
    functionality.
    @param digit_pos_to_extract: digit position to extract
    @param denominator_addend: added to denominator of fractions in the formula
    @param precision: same as precision in main function
    @return: floating-point number whose integer part is not important
    """
    sum = 0.0
    for sum_index in range(digit_pos_to_extract + precision):
        denominator = 8 * sum_index + denominator_addend
        exponential_term = 0.0
        if sum_index < digit_pos_to_extract:
           
            exponential_term = pow(
                16, digit_pos_to_extract - 1 - sum_index, denominator
            )
        else:
            exponential_term = pow(16, digit_pos_to_extract - 1 - sum_index)
        sum += exponential_term / denominator
    return sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
