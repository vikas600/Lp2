class AirlineSchedulingSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight_id, seats, cargo):
        if flight_id in self.flights:
            print("Flight already exists.")
        else:
            self.flights[flight_id] = {"seats": seats, "cargo": cargo}
            print(f"Flight {flight_id} added successfully.")

    def display_flights(self):
        if not self.flights:
            print("\nNo flights available.")
            return
        print("\nAvailable Flights:")
        for flight, details in self.flights.items():
            print(f"{flight}: Seats: {details['seats']} | Cargo Capacity: {details['cargo']}kg")

    def book_flight(self, flight_id, seats_needed):
        if flight_id not in self.flights:
            print("Invalid flight ID.")
            return
        if self.flights[flight_id]["seats"] >= seats_needed:
            self.flights[flight_id]["seats"] -= seats_needed
            print(f"{seats_needed} seats booked successfully on {flight_id}.")
        else:
            print(f"Not enough available seats on {flight_id}. Only {self.flights[flight_id]['seats']} seats left.")

    def book_cargo(self, flight_id, cargo_needed):
        if flight_id not in self.flights:
            print("Invalid flight ID.")
            return
        if self.flights[flight_id]["cargo"] >= cargo_needed:
            self.flights[flight_id]["cargo"] -= cargo_needed
            print(f"{cargo_needed}kg cargo booked successfully on {flight_id}.")
        else:
            print(f"Not enough cargo space on {flight_id}. Only {self.flights[flight_id]['cargo']}kg available.")

def airline_expert_system():
    system = AirlineSchedulingSystem()
    print("Welcome to Dynamic Airline Scheduling System \n")

    while True:
        print("\n--- Menu ---")
        print("1. Add Flight")
        print("2. Display Available Flights")
        print("3. Book Seats")
        print("4. Book Cargo")
        print("0. Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            flight_id = input("Enter new flight ID (e.g., F101): ")
            try:
                seats = int(input("Enter total seats: "))
                cargo = int(input("Enter cargo capacity in kg: "))
                system.add_flight(flight_id, seats, cargo)
            except ValueError:
                print("Please enter valid numeric values for seats and cargo.")

        elif choice == "2":
            system.display_flights()

        elif choice == "3":
            flight_id = input("Enter flight ID to book seats: ")
            try:
                seats = int(input("Enter number of seats to book: "))
                system.book_flight(flight_id, seats)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            flight_id = input("Enter flight ID to book cargo: ")
            try:
                cargo = int(input("Enter cargo weight in kg: "))
                system.book_cargo(flight_id, cargo)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "0":
            print("Thank you for using the system. Have a safe journey!")
            break

        else:
            print("Invalid option. Please choose from the menu.")

# Run the dynamic expert system
airline_expert_system()


#input ye dalo

# Welcome to Dynamic Airline Scheduling System ✈️

# --- Menu ---
# 1. Add Flight
# 2. Display Available Flights
# 3. Book Seats
# 4. Book Cargo
# 0. Exit
# Enter your choice (0-4): 1
# Enter new flight ID (e.g., F101): F201
# Enter total seats: 120
# Enter cargo capacity in kg: 4500
# Flight F201 added successfully.

# --- Menu ---
# 1. Add Flight
# 2. Display Available Flights
# 3. Book Seats
# 4. Book Cargo
# 0. Exit
# Enter your choice (0-4): 1
# Enter new flight ID (e.g., F101): F202
# Enter total seats: 180
# Enter cargo capacity in kg: 6000
# Flight F202 added successfully.

# --- Menu ---
# 1. Add Flight
# 2. Display Available Flights
# 3. Book Seats
# 4. Book Cargo
# 0. Exit
# Enter your choice (0-4): 2

# Available Flights:
# F201: Seats: 120 | Cargo Capacity: 4500kg
# F202: Seats: 180 | Cargo Capacity: 6000kg

# --- Menu ---
# Enter your choice (0-4): 3
# Enter flight ID to book seats: F201
# Enter number of seats to book: 50
# 50 seats booked successfully on F201.

# --- Menu ---
# Enter your choice (0-4): 4
# Enter flight ID to book cargo: F202
# Enter cargo weight in kg: 2000
# 2000kg cargo booked successfully on F202.

# --- Menu ---
# Enter your choice (0-4): 2

# Available Flights:
# F201: Seats: 70 | Cargo Capacity: 4500kg
# F202: Seats: 180 | Cargo Capacity: 4000kg

# --- Menu ---
# Enter your choice (0-4): 0
# Thank you for using the system. Have a safe journey!
