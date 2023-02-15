def calculate_attend_and_miss(n: int) -> str:
    """
    Calculates the probability of missing the graduation ceremony given the total number of academic days.

    Args:
        n (int): The total number of academic days.

    Returns:
        str: The probability of missing the graduation ceremony as a string in the format "Answer of (2) / Answer of (1)".

    Raises:
        ValueError: If n is less than zero or less than max_consecutive_absences.

    """
    max_consecutive_absences = 4  # as it's a static value in question statement

    # Check for invalid input
    if n < max_consecutive_absences or n < 0:
        raise ValueError("Invalid inputs")

    # Create a 2D list to store intermediate results
    dp_table = [[0] * (max_consecutive_absences + 1) for _ in range(n + 1)]

    # Fill in the base cases of the table
    for i in range(max_consecutive_absences):
        dp_table[0][i] = 1

    # Compute the dynamic programming table using bottom-up approach
    for i in range(1, n + 1):
        for j in range(max_consecutive_absences - 1, -1, -1):
            # Compute the number of valid ways to attend classes on i-th day and miss j days in a row
            dp_table[i][j] = dp_table[i - 1][0] + dp_table[i - 1][j + 1]

    total_ways_to_attend = dp_table[n][0]
    total_ways_to_miss_last_day = dp_table[n - 1][1]

    return f"{total_ways_to_miss_last_day}/{total_ways_to_attend}"


if __name__ == "__main__":
    try:
        days = int(input("Enter number of academic days: "))
        print("Number of academic days is {}".format(days))
    except Exception as e:
        print(e)
    else:
        print("Probability of missing the graduation ceremony", calculate_attend_and_miss(days))

