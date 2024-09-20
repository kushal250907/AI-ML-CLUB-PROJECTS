 def calculate_income_tax(income):
    """
    Calculate income tax based on given income using defined tax slabs and rates.

    :param income: The total income of the individual (float or int).
    :return: Total tax amount (float).
    """

    # Define tax slabs and rates as tuples of (upper limit, rate)
    slabs = [(250000, 0), (500000, 0.05), (1000000, 0.2), (float('inf'), 0.3)]
    tax = 0.0

    # Iterate over slabs and calculate tax for each slab
    for i in range(len(slabs)):
        lower_limit = slabs[i - 1][0] if i > 0 else 0
        upper_limit, rate = slabs[i]

        if income > lower_limit:
            taxable_income = min(income, upper_limit) - lower_limit
            tax += taxable_income * rate

    return tax


# User input
try:
    income = float(input("Enter your total income: "))
    if income < 0:
        print("Income cannot be negative.")
    else:
        tax = calculate_income_tax(income)
        print(f"The total tax on an income of {income} is: {tax:.2f}")
except ValueError:
    print("Please enter a valid number for income.")
