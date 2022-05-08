def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, cash):
    cc_pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, sold):
    cc_pet_shop["admin"]["pets_sold"] += sold
    return cc_pet_shop["admin"]["pets_sold"]

def get_stock_count(cc_pet_shop):
    stock_count = len(cc_pet_shop["pets"])
    return stock_count

def get_pets_by_breed(cc_pet_shop, breed):
    pets = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

def find_pet_by_name(cc_pet_shop, name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

# STUCK
# def remove_pet_by_name(cc_pet_shop, name):
#      for pet in cc_pet_shop["pets"]:
#          if pet["name"] == name:
#             cc_pet_shop["pets"].remove(pet)

def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

#Optional Tests

def customer_can_afford_pet(customers, new_pet):
    if customers["cash"] >= new_pet["price"]:
        return True
    else:
        return False

# Multi Asserts Tests

# STUCK Not sure what to do with these
def sell_pet_to_customer(cc-pet_shop, pet, customer):
    if get_customer_pet_count 