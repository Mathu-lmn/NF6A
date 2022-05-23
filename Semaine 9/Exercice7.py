from datetime import date, timedelta
from termcolor import colored

Hotel = {"single": [],
    "double": [],
    "triple": []}

x1 = date(2021, 1, 1) # Start date (year, month, day)
x2 = date(2023, 1, 2) # Ending date (year, month, day)
Hotel["single"].append((101, [(x1, x2)]))
for i in range(102, 111):
    x = (i,[])
    Hotel["single"].append(x)
for i in range(201, 216):
    x = (i,[])
    Hotel["double"].append(x)
for i in range(301, 319):
    x = (i,[])
    Hotel["triple"].append(x)

def is_room_free(room_type, date_from, date_to):
    for room in Hotel[room_type]:
        if len(room[1]) == 0:
            j = True
        else:
            if room[1][-1][0] <= date_from <= room[1][-1][1] or room[1][-1][0] <= date_to <= room[1][-1][1]:
                    j = False
            else:
                j = True
    return j

# k = is_room_free("single", date(2020, 1, 1), date(2020, 1, 2))
# print(k)

def create_reservation():
    room_type = input("What type of room would you like to book? ")
    date_from = date(int(input("Enter the year of your stay: ")), int(input("Enter the month of your stay: ")), int(input("Enter the day of your stay: ")))
    nights = int(input("How many nights would you like to stay? "))
    date_to = date_from + timedelta(nights)
    if date_from > date_to:
        print("Your arrival date is after your departure date")
        return
    if room_type not in Hotel:
        print("We do not have that room type")
        return
    if not is_room_free(room_type, date_from, date_to):
        print("We do not have any room of that type available")
        return
    else:
        for room in Hotel[room_type]:
            print("Checking room", room[0])
            if len(room[1]) == 0:
                room[1].append((date_from, date_to))
                print("Your room has been booked")
                return
            else:
                if room[1][-1][0] <= date_from <= room[1][-1][1] or room[1][-1][0] <= date_to <= room[1][-1][1]:
                    pass
                else:
                    room[1].append((date_from, date_to))
                    print("Your room has been booked")
                    return

# create_reservation()

def room_invoice():
    room = int(input("Enter the room number: "))
    for room_type in Hotel:
        for room_number in Hotel[room_type]:
            if room_number[0] == room:
                print("Room number:", room)
                print("Arrival date:", room_number[1][-1][0])
                print("Departure date:", room_number[1][-1][1])
                nights = (room_number[1][-1][1] - room_number[1][-1][0]).days
                print("Number of nights:", nights)
                if room_type == "single":
                    print("Price:", nights * 60)
                elif room_type == "double":
                    print("Price:", nights * 80)
                elif room_type == "triple":
                    print("Price:", nights * 100)
                return

# room_invoice()

def edit_hotel():
    choice = input("Would you like to add a room or delete a room? ")
    if "add" in choice:
        room_type = input("What type of room would you like to add? ")
        if room_type not in Hotel:
            print("We do not have that room type")
            return
        else:
            room_number = Hotel[room_type][-1][0] + 1
            Hotel[room_type].append((room_number, []))
            print("Room added")
            return
    elif "delete" in choice:
        j = False
        room = int(input("Enter the room number: "))
        for room_type in Hotel:
            for room_number in Hotel[room_type]:
                if room_number[0] == room:
                    Hotel[room_type].remove(room_number)
                    print("Room deleted")
                    j = True
                elif room_number[0] > room and room_number[0] < Hotel[room_type][-1][0]:
                    i = room_number[0]
                    new_room = (i - 1, room_number[1])
                    room_number = new_room
        if j == False:
            print("We do not have that room number")
            return

# edit_hotel()

def display_hotel():
    for room_type in Hotel:
        print(colored(f"\nRoom type : {room_type}\n", "red", attrs=["bold", "underline"]))
        for room in Hotel[room_type]:
            print(colored(f"Room number:{room[0]}", attrs=["underline"]))
            if room[1] == []:
                print("\tRoom is free")
            elif room[1][-1][1] > date(2022, 5, 23):
                print("\tThe room is rented until", room[1][-1][1])
            else:
                print("\tThe room is free since", room[1][-1][1])

display_hotel()