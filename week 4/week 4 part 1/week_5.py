
def collect_user_id(id_counter=5000):
    name = input("Enter Your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email address: ")
    unique_id = id_counter + 1
    
    # Collect user information
    user_info = {
        "ID": unique_id,
        "Name": name,
        "Age": age,
        "EMAIL": email
    }
    
    return user_info

def main(user_info):
    print(f"\n User Information")
    print(f"Unique ID: {user_info['ID']}")
    print(f"Name: {user_info['Name']}")
    print(f"Age: {user_info['Age']}")
    print(f"Email: {user_info['EMAIL']}")

# Collect user information
user_info = collect_user_id()

# Display the information using the main function
main(user_info)


#2
def calculate_total_amount():
    total_amount = 0.0
    
    while True:
        price = input("Enter the price of the item (or type 'finish' to end): ")
        
        if price.lower() == "finish":
            break
        
        try:
            total_amount += float(price)
        except ValueError:
            print("Please enter a valid price.")
    
    print(f"The total amount is: ${total_amount:.2f}")

calculate_total_amount()


#3
def categorize_request():
    Total_price= float(input("Enter a price: "))
    if Total_price < 150: 
        category = "low"
        recommend = "procced witn standard processing."
    else:
        category = "High"
        recommend= "Review for potential discount."

    print("Request Summary: ")
    print(f"Total amount: ${Total_price}")
    print(f"Category:{category}")
    print(f"Recommend:{recommend}")

categorize_request()




def create_detailed_report(user_name, total_amount, category, recommendation, id_counter, user_age, user_email):
    print("detailed report")
    print (f"Unique ID: {id_counter}")
    print (f"Username: {user_name} ")
    print (f"Age: {user_age}")
    print(f"Email: {user_email}")
    print (f"Total Amount: ${total_amount: 2f}")
    print (f"Category:{category}")
    print (f"Recommendation: {recommendation}")
def main():
    id_counter = 5000
    id_counter, username, user_age, user_email = collect_user_id(id_counter)
    total_amount, items = calculate_total_amount ()
    category, recommendation = categorize_request(total_amount)
    create_detailed_report(id_counter, username, user_age, user_email, total_amount, category, recommendation)
main()
   