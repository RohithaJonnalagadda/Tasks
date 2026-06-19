food = input("Enter food name: ")
rating = int(input("Enter food rating (1 to 5): "))

print("\nFood Name:", food)

if rating == 5:
    print("Review: Delicious Food")
    print("Customer loved the food!")

elif rating == 4:
    print("Review: Very Tasty Food ")
    print("Customer enjoyed the food.")

elif rating == 3:
    print("Review: Good Food ")
    print("Food was okay.")

elif rating == 2:
    print("Review: Average Food ")
    print("Food needs improvement.")

elif rating == 1:
    print("Review: Bad Food ")
    print("Customer did not like the food.")

else:
    print("Invalid Rating! Please enter rating between 1 and 5.")
