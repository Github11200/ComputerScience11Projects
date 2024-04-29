import math
import pyfiglet

print(pyfiglet.figlet_format(
    "Interest Rate Calculator", font="big", width=500))

print("This is a tool to help you calculate interest, principal, interest rate, or time using the simple interest formula. This program also contains extra functionality for calculating compound interest year on year. Get startedby answering the questions below, and if you don't have an answer to that variable and it is what you want to solve for then simply just input '?' and press enter.")

try:
    option = int(
        input(
            "\n\nWould you like to calculate simple interest rate (enter 0) or compound interest (enter 1)? "
        )
    )
except Exception:
    print("You must input either 0 or 1, nothing else")


def get_input(prompt):
    user_input = input(prompt)
    try:
        data = float(user_input)
        return data
    except Exception:
        return None


print("\n=======================================================================\n")

try:
    if option == 0:
        interest_money_created = get_input(
            "How much money did you generate in interest? "
        )
        principal = get_input("What is your principal in dollars? ")
        interest_rate = get_input("What is your interest rate per year? ")
        time = get_input(
            "How much time has the money been invested or borrowed for, in years? "
        )

        if interest_money_created == None:
            print(
                f"The amount of interest money created in dollars was ${
                    (principal * (interest_rate / 100) * time): .2f}"
            )
        elif principal == None:
            print(f"The amount of money you started off with was ${
                (interest_money_created / ((interest_rate / 100) * time)): .2f}")
        elif interest_rate == None:
            print(f"The interest rate every year was {
                (interest_money_created / (principal * time)): .2f} %")
        else:
            print(f"The number of years the money has been invested or borrowed for is {
                (interest_money_created / (principal * (interest_rate / 100))): .2f} years")
    else:
        print("IMPORTANT: You will NEED to give an input for the number of times the interest rate was applied, but the other variables are optional.")
        final_amount = get_input(
            "What is the final amount of money in dollars? ")
        principal = get_input("What is your principal in dollars? ")
        interest_rate = get_input("What is the interest rate? ")
        number_of_times_interest_is_applied = get_input(
            "How many times was this interest applied per time period? "
        )
        time = get_input("How many number of time periods elapsed? ")

        if final_amount == None:
            print(
                f"The final amount of compound interest you will get is ${
                    principal * (1 + ((interest_rate / 100) / number_of_times_interest_is_applied))**(number_of_times_interest_is_applied * time)}"
            )
        elif principal == None:
            print(
                f"The initial principal balance was ${
                    final_amount / (1 + ((interest_rate / 100) / number_of_times_interest_is_applied))**(number_of_times_interest_is_applied * time)}"
            )
        elif interest_rate == None:
            print(f"The final interest rate is {number_of_times_interest_is_applied * (
                (final_amount / principal)**(1 / time * number_of_times_interest_is_applied) - 1)} %")
        else:
            print(f"The number of times this interest was applied in a time period is {
                math.log(final_amount / principal) / math.log(1 + (interest_rate / 100))} times")
except Exception:
    print("Whoops! You may have not given the program enough information to work or inputting a number that was not valid. Remember, you cannot add a number that is a string, it must the number itself (eg. 78.90, 90)")
