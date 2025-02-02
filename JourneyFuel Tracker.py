FUEL_PRICE = 104.71
TOTAL_JOURNEY = 100
LAST_JOURNEY = 50
VEHICLE_AVG = 50
TOTAL_PRICE = 0
FUEL = 0
KM = 0


def set_defaults():
    global FUEL_PRICE, VEHICLE_AVG, TOTAL_JOURNEY, LAST_JOURNEY
    FUEL_PRICE = float(input(f"Enter New Fuel Price ({FUEL_PRICE}) : ")) or FUEL_PRICE
    VEHICLE_AVG = float(input(f"Enter Average of Vehicle ({VEHICLE_AVG}) : ")) or VEHICLE_AVG
    TOTAL_JOURNEY = float(input(f"Enter Total Journey Of Vehicle in Km ({TOTAL_JOURNEY}Km : )")) or TOTAL_JOURNEY
    LAST_JOURNEY = float(input(f"Enter Last Journey In Km ({LAST_JOURNEY}Km : )")) or LAST_JOURNEY


def input_data():
    global FUEL_PRICE, VEHICLE_AVG, TOTAL_JOURNEY, LAST_JOURNEY, TOTAL_PRICE, FUEL, KM
    TOTAL_PRICE = float(input("Enter amount of fuel inserted : ")) or TOTAL_PRICE
    FUEL = (TOTAL_PRICE / FUEL_PRICE)
    KM = VEHICLE_AVG * FUEL
    TOTAL_JOURNEY += LAST_JOURNEY
    LAST_JOURNEY += KM


def display_data():
    global FUEL_PRICE, VEHICLE_AVG, TOTAL_JOURNEY, LAST_JOURNEY, TOTAL_PRICE, FUEL, KM
    print(f"Total Journey: {TOTAL_JOURNEY:.2f} km")
    print(f"Expected Journey: {KM:.2f} km")
    print(f"Vehicle Average: {VEHICLE_AVG:.2f} km/l")
    print(f"Fuel: {FUEL:.2f}")


option = int(input("If you want to change your previous setting or defaults, Press 1 : "))

if option == 1:
    set_defaults()
else:
    input_data()

display_data()

