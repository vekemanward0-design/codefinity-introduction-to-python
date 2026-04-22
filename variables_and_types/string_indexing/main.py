grocery_item = "Grilled Chicken Salad"

# Utilize the len() function to find the length of the string
length_of_item = len(grocery_item)

# Use positive indexing to find the first character of each word
first_char = grocery_item[0]  # 'G' from "Grilled"
second_char = grocery_item[8]  # 'C' from "Chicken"
third_char = grocery_item[16]  # 'S' from "Salad"

# Use negative indexing to find the last character of each word
# The index is calculated as -1 from the end of the string backwards
last_char1 = grocery_item[-1]  # 'd' from "Salad"
last_char2 = grocery_item[-7]  # 'n' from "Chicken"
last_char3 = grocery_item[-15]  # 'd' from "Grilled"

# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)