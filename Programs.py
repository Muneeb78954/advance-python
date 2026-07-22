#User input
name = input("What is your name? ")
print(f"Hello {name}, welcome to the program!")

print("Hi, I am your AI virtual shopping mall, would you like to buy something?")
response = input("Please enter your choice: ")
print(f"You chose: {response}")
item_list = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Here is the list of items available for purchase:")
for item in item_list:
    print(item)
price_list = [1.5, 0.5, 2.0, 1.0, 3.0]
item_dict = dict(zip(item_list, price_list))
total_price = 0
while True:
    item_choice = input("Enter the item you want to buy (or type 'done' to finish): ")
    if item_choice.lower() == 'done':
        break
    if item_choice in item_dict:
        total_price += item_dict[item_choice]
        print(f"{item_choice} added to your cart. Current total: ${total_price:.2f}")
    else:
        print("Item not found. Please choose from the available items.")
print(f"Your total purchase amount is: ${total_price:.2f}. Thank you  for shopping with us!")