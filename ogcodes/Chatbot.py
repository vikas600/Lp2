import time
from datetime import datetime

# Time-based greeting
def time_based_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

# Menu display
def show_menu():
    print("\n--- Customer Support Topics ---")
    print("1. Track Order")
    print("2. Cancel Order")
    print("3. Return Product")
    print("4. Refund Status")
    print("5. Payment Methods")
    print("6. Exchange Policy")
    print("7. Talk to Human Agent")
    print("0. Exit Chat")

# Chatbot response functions
def track_order():
    return "You can track your order in the 'My Orders' section of your account."

def cancel_order():
    return "You can cancel your order before it is shipped from the order details page."

def return_product():
    return "Products can be returned within 7 days of delivery via 'My Orders' > Return."

def refund_status():
    return "Refunds are processed within 5-7 working days after the product is picked up."

def payment_methods():
    return "We accept UPI, Debit/Credit Cards, Net Banking, and Cash on Delivery."

def exchange_policy():
    return "Exchange is available on selected products only. Check the product page."

def human_support():
    time.sleep(2)
    return "All our agents are currently busy. Please describe your issue, and we’ll get back to you soon!"

# Logging function
def log_interaction(name, choice_text):
    with open("chat_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now()}] {name}: {choice_text}\n")

# Main chatbot
def chatbot():
    print("Welcome to ShopSmart Customer Support Chat!")
    name = input("May I know your name? ").strip().title()
    print(f"\nChatbot: {time_based_greeting()}, {name}! How can I assist you today?")

    while True:
        show_menu()
        choice = input("\nEnter your option (0-7): ")

        if choice == "1":
            response = track_order()
        elif choice == "2":
            response = cancel_order()
        elif choice == "3":
            response = return_product()
        elif choice == "4":
            response = refund_status()
        elif choice == "5":
            response = payment_methods()
        elif choice == "6":
            response = exchange_policy()
        elif choice == "7":
            response = human_support()
        elif choice == "0":
            print(f"\nChatbot: Thank you for chatting with us, {name}. Have a great day!")
            break
        else:
            response = "Invalid option. Please enter a number from 0 to 7."

        print(response)
        log_interaction(name, f"Option {choice} - {response}")
        time.sleep(1)

# Run the chatbot
chatbot()
