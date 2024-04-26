class Guest:
    def __init__(self, first, last, rank, age):
        self.last_name = last
        self.first_name = first
        self.rank = int(rank)
        self.age = int(age)
        
    def guest_info(self, all_guests):
        for guest in all_guests:
            print(guest.first_name, guest.last_name, "Age:",guest.age)
            
    def loyalty_program(self, all_guests):
        gold_members = [guest.last_name for guest in all_guests if guest.rank >= 10]
        if gold_members:
            print("Gold members:")
            for member in gold_members:
                print("\tGuest:", member)
    
    def guest_avg(self, all_guests):
        total_age = 0
        for guest in all_guests:
            total_age += guest.age
        avg_age = total_age / len(all_guests)
        print("Average customer age:", avg_age)
            
            
all_guests = list()
num_guests = int(input("Enter a number of guests: "))
for i in range(num_guests):
    data = input("First Name/Last Name/Rank/Age: ").split("/")
    all_guests.append(Guest(data[0], data[1], data[2], data[3]))
    
guest = all_guests[0]
guest.loyalty_program(all_guests)
guest.guest_info(all_guests)
guest.guest_avg(all_guests)