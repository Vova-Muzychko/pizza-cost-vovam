# Pizza Cost Calculator

# HST tax rate (13%)
HST = 0.13

# Labour cost for making one pizza
LABOUR_COST = 0.75
# Rent cost for one pizza
RENT_COST = 1.00

# Material cost per inch of pizza
MATERIAL_COST = 0.50

# Ask the user to enter the pizza diameter
diameter = float(input("Enter pizza diameter: "))

# Calculate the subtotal
subtotal = LABOUR_COST + RENT_COST + (MATERIAL_COST * diameter)

# Calculate the tax amount
tax = subtotal * HST

# Calculate the final total
total = subtotal + tax

# Display the subtotal
print("Subtotal: $", round(subtotal, 2))

# Display the tax
print("Tax: $", round(tax, 2))

# Display the total cost
print("Total: $", round(total, 2))
