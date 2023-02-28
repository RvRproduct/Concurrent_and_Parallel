"""
Callback Intuition
Calling one function from another function taking some context from the calling function.

Example:
You are requested by broker to get Health Insurance and you told that you will get insurance
if you get a bonus on monthend.

Broker gives his mobile number to callback if you get bonus

In monthend, you will do check salary and based on bonus, will decide to call broker.
"""

"""
Callback Intuition - Function format

On salary day, below are happening
Checking salary for your employee id
Calling back broker as you had mobile# already.

// Checking the balance
function check_salary(emp_id, broker)
{
    if get_salary(emp_id) > 50000: //Bonus event happens
        broker() // calling back broker
}
"""

inventory = {}
min_retail = 500

def add_with_retail_check(product, price):
    if price < min_retail:
        return False
    if price >= min_retail:
        inventory.update({product: price})
        return True

# callback function
def get_product(product):
    print(product, "\t\t- Product Added to Inventory, and Price:", inventory[product])

def add_to_inventory(product, price, callback):
    add_status = add_with_retail_check(product, price)
    if add_status:
        callback(product)
    else:
        print(product, "\t\t- Product was not added due to low retail amount less than", min_retail)

add_to_inventory("Shirt", 800, get_product)
add_to_inventory("Watch", 500, get_product)
add_to_inventory("Pen", 150, get_product)
add_to_inventory("Marker", 150, get_product)

get_product("Watch")
print(get_product)