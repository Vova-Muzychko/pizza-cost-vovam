let HST = 0.13
let LABOUR_COST = 0.75
let RENT_COST = 1
let MATERIAL_COST = 0.5
let diameter = game.askForNumber("\"pizza size?\"")
let subtotal = LABOUR_COST + (RENT_COST + MATERIAL_COST * diameter)
let tax = subtotal * HST
let total = subtotal + tax
game.splash("tax: $" + tax + "" + ("Subtotal: $" + subtotal) + "" + ("total: $" + total))
