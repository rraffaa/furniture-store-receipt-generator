def calculate_total_and_itemization(prices, descriptions):
    try:
        # Check if all prices are valid numbers (integers or floats)
        if not all(isinstance(price, (int, float)) for price in prices):
            raise ValueError("All prices must be valid numbers.")

        # Check if all descriptions are non-empty strings
        if not all(isinstance(description, str) and description.strip() != "" for description in descriptions):
            raise ValueError("All descriptions must be non-empty strings.")
        
        total = sum(prices)  # Calculate the total of the purchases
        itemization = " ".join(descriptions)  # Join the descriptions into a single string
        return total, itemization

    except ValueError as e:
        print(f"Error: {e}")
        return None, None  # Return default values in case of error

# pieces
cozy_couch_description = """Cozy Couch. Plush velvet fabric over a sturdy oak frame. 34 inches high x 60 inches wide x 35 inches deep. Available in blue or grey."""
modern_armchair_description = """Modern Armchair. Faux leather on pinewood. 30 inches high x 28 inches wide x 30 inches deep. Available in tan or charcoal."""
elegant_lamp_description = """Elegant Lamp. Ceramic base with a linen shade. 40 inches tall. Elegant white base with a soft beige shade."""
dining_table_description = """Dining Table. Solid wood with a natural finish. 30 inches high x 60 inches wide x 40 inches deep. Seats up to 6 people."""
wooden_desk_description = """Wooden Desk. Crafted from durable oak wood. 30 inches high x 50 inches wide x 25 inches deep. Perfect for office use."""
turquoise_sofa_description = """Turquoise Sofa. Soft fabric with a modern design. 36 inches high x 72 inches wide x 34 inches deep. Seats 3 comfortably."""
second_elegant_lamp_description = """Second Elegant Lamp. Ceramic base with a white linen shade. 38 inches tall. A minimalist design in a soft, matte finish."""
red_lamp_description = """Red Lamp. Metal base with a red shade. 36 inches tall. Bright red finish perfect for a bold statement."""
dark_wood_shelf_description = """Dark Wood Shelf. A sturdy bookshelf made from dark oak. 40 inches high x 30 inches wide x 12 inches deep. Ideal for books or decor."""
rug_one_description = """Rug One. Soft, plush material with intricate patterns. 5 feet by 7 feet in size. A warm tone with golden accents."""
rug_two_description = """Rug Two. Smooth weave with geometric designs. 6 feet by 9 feet in size. Deep green and cream colors for a stylish touch."""

# prices
cozy_couch_price = 320.00
modern_armchair_price = 150.75
elegant_lamp_price = 65.30
dining_table_price = 299.00
wooden_desk_price = 150.00
turquoise_sofa_price = 309.00
second_elegant_lamp_price = 49.00
red_lamp_price = 57.00
dark_wood_shelf_price = 137.00
rug_one_price = 43.00
rug_two_price = 86.00

# tax
sales_tax = .075

# customers
customer_one_total = cozy_couch_price + elegant_lamp_price
customer_two_total = dining_table_price + wooden_desk_price + turquoise_sofa_price
customer_three_total = second_elegant_lamp_price + red_lamp_price + dark_wood_shelf_price + rug_one_price + rug_two_price

# purchases
customer_one_itemization = "" 
customer_one_itemization += cozy_couch_description
customer_one_itemization += " " + elegant_lamp_description

customer_two_itemization = ""
customer_two_itemization += dining_table_description
customer_two_itemization += " " + wooden_desk_description
customer_two_itemization += " " + turquoise_sofa_description

customer_three_itemization = ""
customer_three_itemization += second_elegant_lamp_description
customer_three_itemization += " " + red_lamp_description
customer_three_itemization += " " + dark_wood_shelf_description
customer_three_itemization += " " + rug_one_description
customer_three_itemization += " " + rug_two_description

# checkout
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

customer_three_tax = customer_three_total * sales_tax
customer_three_total += customer_three_tax

# Display results for Customer One
customer_one_total, customer_one_itemization = calculate_total_and_itemization(
    [cozy_couch_price, elegant_lamp_price], 
    [cozy_couch_description, elegant_lamp_description]
)

if customer_one_total is not None:
    print("Customer One Items:")
    print(customer_one_itemization)
    print("Total: $", round(customer_one_total, 2))
else:
    print("There was an error processing Customer One.")

# Display results for Customer Two
customer_two_total, customer_two_itemization = calculate_total_and_itemization(
    [dining_table_price, wooden_desk_price, turquoise_sofa_price], 
    [dining_table_description, wooden_desk_description, turquoise_sofa_description]
)

if customer_two_total is not None:
    print("\nCustomer Two Items:")
    print(customer_two_itemization)
    print("Total: $", round(customer_two_total, 2))
else:
    print("There was an error processing Customer Two.")

# Display results for Customer Three
customer_three_total, customer_three_itemization = calculate_total_and_itemization(
    [second_elegant_lamp_price, red_lamp_price, dark_wood_shelf_price, rug_one_price, rug_two_price], 
    [second_elegant_lamp_description, red_lamp_description, dark_wood_shelf_description, rug_one_description, rug_two_description]
)

if customer_three_total is not None:
    print("\nCustomer Three Items:")
    print(customer_three_itemization)
    print("Total: $", round(customer_three_total, 2))
else:
    print("There was an error processing Customer Three.")
