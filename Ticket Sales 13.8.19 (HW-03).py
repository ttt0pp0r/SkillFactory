# Inputs
x = int(input("How many tickets do you need? "))
younger_18 = int(input("How many people are younger than 18? "))
middle_18 = int(input("How many people are between 18 and 25? "))
higher_25 = int(input("How many people are older than 25? "))


# logick
def ticket_sales():
    result_1 = middle_18 * 990
    result_2 = higher_25 * 1390
    # sum
    overall = result_1 + result_2

    return (overall)


if x >= 3:
    total = ticket_sales() - (ticket_sales() * 0.10);

    print(f"Your overall comes to {total}RUB: ")
else:
    print(f"Your overall comes to {ticket_sales()}RUB: ")
