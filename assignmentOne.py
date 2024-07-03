# Recieve the price of a product exclusive the taxes from the user
priceExclusive = input("Skriv in priset exklusive moms: ")
# Change the int type of the input to a float number and multiply it with 1.25 to get the price inclusive taxes
priceInclusive = float(priceExclusive) * 1.25
# Print the price inclusive taxes to the user
print("Priset inklusive moms är: ", priceInclusive)

"""
If the user inputs 100 as the price exclusive taxes the output will be 125.0 (not 125 since the calculation is done with floats).
A possible error is if the user input isn't a number. Then the program will crash since I don't have any error handling.
If there is any syntax errors, check the error message in the terminal or debugg the code by using breakpoints.
If there is any logical errors I can divide the calculation into smaller parts. First make the input to a float. Then multiply it
and assign the value to the variable.
"""