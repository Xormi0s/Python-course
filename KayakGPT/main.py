print("Welcome to KayakGPT. Let's find you the perfect adventure!")
start = int(input("Enter 1 to start. Enter 2 to stop: "))
while start != 2:
    destination = input("Do you already have an destination in mind? ").lower()
    if destination == "yes":
        print("That's amazaing news! Let's plan your trip then.")
        transport = input("What is your preffered method of transportation? Plane, train or car: ").lower()
        if transport == 'plane':
            class_type = input("Which class do you want? First, economy or business? ").lower()
            luggage = int(input("Enter the baggage weight in kg: "))
            if luggage >= 25 and class_type == "business" or class_type == "first":
                print("Great, that is well within the limits.")
            elif luggage < 25 and class_type == "business" or class_type == "first":
                print("You can bring more withing this class if you want.")
            else:
                print("Warning you are above the limit for your class")
        elif transport == "train":
            seat_class = input("Economy or business seating? ").lower()
            if seat_class == "business":
                print("Great choice for comfort")
            elif seat_class == "economy":
                print("Good savings option, smart!")
            else:
                print("We don't have that option available.")
        elif transport == "car":
            print("Road trips are very fun!")
            num_people = int(input("How many people: "))
            if num_people <= 4:
                print("Great, you could rent a car!")
            else:
                print("You might want to rent a van instead of a car!")
        else:
            print("We don't have that transport type...")
    else:
        print("I can help you find your perfect destination!")
        trip_type = input("Preffered destinatinon? Beach, city or adventure: "). lower()
        if trip_type == "beach":
            print("What do you think about Hawaii?")
            beach_type = input("Popular loaction or more remote? ").lower()
            if beach_type == "popular":
                print("You should check out Waikiki beach!")
            elif beach_type == "remote":
                print("You should check out Maui!")
            else:
                print("We don't have that option...")
        elif trip_type == "city":
            print("You could travel to New York City")
            activity = input("Indoor or outdoor activities? ").lower()
            if activity == "indoor":
                print("Check out the famous wax museum!")
            elif activity == "outdoor":
                print("You can relax in Central Park.")
            else:
                print("Wrong intput.")
        elif trip_type == "adventure":
            print("Let's head out to Yosimite Nation Park!")
            outdoor_activity = input("Hiking or camping? ").lower()
            if outdoor_activity == "hiking":
                print("Try hiking the half dome")
            elif outdoor_activity == "camping":
                print("There are a lot of great options to checkout.")
            else:
                print("That option is not available...")
        else:
            print("That trip type is not available...")
            
    print("Enter for a chance to win a free trip!")
    for i in range(1,4):
        if input("What is the greatest country? ").lower() == "belgium":
            print("You just won a trip to the greatest country Belgium!")
            break

    start = int(input("Enter 1 to start again. Enter 2 to stop: "))
    print("Thanks for using KayakGPT!")