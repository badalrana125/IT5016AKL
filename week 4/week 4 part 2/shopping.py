def get_shoppinglist():
    shopping_list = []
    total_price = 0
    while True:
            item = input("Enter the name of the iteam or type 'done' to finish:")
            if item.lower()=='done':
               break
            try:
              price = float(input("enetr the price of the '{item}': "))
              shopping_list.append((item,price))
              total_price += price
            except ValueError:
                print("invalade input. please enter a numeric valie for the price.")
    return shopping_list, total_price
    
def main():
    print("welcome to the shopping list program")
    shopping_list, total_price = get_shoppinglist()

    if not shopping_list:
        print("No iteams were entered")
    else:
        print("\nShoppin list: ")
        for item, price in shopping_list:
            print(f"{item},${price:.2f}")
        print(f"\nTotal price: ${total_price:.2f}")
main()