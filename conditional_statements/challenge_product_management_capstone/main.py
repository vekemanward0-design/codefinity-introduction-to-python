# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

# Determine the discount based on product type, days until expiration, and stock level
if product_type == "Perishable":
    # Apply a 30% discount if there are 3 days or less until expiration and stock level is over 50
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    # Apply a 20% discount if there are 4 to 6 days until expiration and stock level is over 50
    elif days_until_expiration > 3 and days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    # Apply a 10% discount if there are more than 6 days until expiration and stock level is less than or equal to 50 
    elif days_until_expiration > 6 and stock_level <= 50:
        print("10% discount applied")
# If the product is non-perishable, no discount is available
else:
    print("No discount available for non-perishable items.")