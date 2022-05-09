Users =[("Bob", "Movies", "Football", "Reading"),("Alice", "Swimming", "Handball", "Gaming"), ("Eva", "Movies", "Coding", "Gaming")]

def new_users():
    number_new_users = int(input("How many new users are there? "))
    for i in range(number_new_users):
        new_user = []
        new_username = input("Enter the name of the new user: ")
        new_user.append(new_username)
        new_user_interests = int(input("Enter the number of interests of the new user:"))
        for j in range(new_user_interests):
            new_user_interest = input("Enter the interest of the new user: ")
            new_user.append(new_user_interest)
        Users.append(tuple(new_user))

# new_users()
print(Users)

def users_liking_activity():
    activity = input("Enter an activity: ")
    users_liking_activity = 0
    for user in Users:
        for i in range(len(user)-1):
            if activity in user[i+1]:
                users_liking_activity += 1
    print("There are {} users liking {}".format(users_liking_activity, activity))

# users_liking_activity()

def users_comparison():
    user1 = input("Enter the name of the first user you want to compare : ")
    user2 = input("Enter the name of the second user you want to compare : ")
    common_activities_count = 0
    for i in range(len(user1)-1):
        for j in range(len(user2)-1):
            if user1[i+1] in user2[j+1]:
                common_activities_count += 1
    print("{} and {} have {} common activities".format(user1, user2, common_activities_count))

# users_comparison()

def delete_activity_for_user():
    activity = input("Enter an activity: ")
    user = input("Enter the name of the user: ")
    for i in range(len(Users)):
        if user in Users[i][0]:
            replace_user = list(Users[i])
            replace_user.remove(activity)
            Users[i] = tuple(replace_user)

# delete_activity_for_user()
# print(Users)

def delete_user():
    user = input("Enter the name of the user: ")
    for i in range(len(Users)):
        if user in Users[i][0]:
            removing = i
    Users.pop(removing)

# delete_user()
# print(Users)

def replace_activity_for_user():
    user = input("Enter the name of the user: ")
    activity = input("Enter the old activity: ")
    new_activity = input("Enter the new activity: ")
    for i in range(len(Users)):
        if user in Users[i][0]:
            replace_user = list(Users[i])
            replace_user.remove(activity)
            replace_user.append(new_activity)
            Users[i] = tuple(replace_user)

replace_activity_for_user()
print(Users)