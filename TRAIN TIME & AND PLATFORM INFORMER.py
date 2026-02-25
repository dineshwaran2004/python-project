import datetime

print("Welcome to NotName Railway Station Console Project-Python")

now = datetime.datetime.now()
print("======================================================")
print("Date And Time:", now)
print("======================================================")

trains = {
    "00001": {
        "name": "Kovai Express",
        "arrival": "10:30 AM",
        "departure": "10:45 AM",
        "platform": "1",
    },
    "00002": {
        "name": "Chennai Express",
        "arrival": "12:15 PM",
        "departure": "12:30 PM",
        "platform": "2"
    },
    "00003": {
        "name": "Navjeevan Express",
        "arrival": "04:10 PM",
        "departure": "04:25 PM",
        "platform": "4"
    },
    "00004": {
        "name": "Thirukkural Express",
        "arrival": "06:00 PM",
        "departure": "06:15 PM",
        "platform": "5"
    }
}

while True:
    print("1. View Train Name and Number")
    print("2. View Train Schedule")
    print("3. View Platform Status")
    print("4. Check Train Status")
    print("5. Exit")

    option = input("Enter Your Option: ")

    if option == "1":
        for no, t in trains.items():
            print("================================================================================")
            print(f"{no} - {t['name']}")
            print("================================================================================")

    elif option == "2":
        for no, t in trains.items():
            print("================================================================================")
            print(f"{no} - {t['name']} | {t['arrival']} - {t['departure']}")
            print("================================================================================")

    elif option == "3":
        for no, t in trains.items():
            print("================================================================================")
            print(f"Platform {t['platform']}  {no} – {t['name']}")
            print("================================================================================")

    elif option == "4":
        train_no = input("Enter Train Number: ")
        if train_no in trains:
            t = trains[train_no]
            print("================================================================================")
            print("Train Status")
            print("Train:", t["name"])
            print("Arrival:", t["arrival"])
            print("Departure:", t["departure"])
            print("Platform:", t["platform"])
            print("================================================================================")
        else:
            print("================================================================================")
            print("Train not found!")
            print("================================================================================")

    # EXIT
    elif option == "5":
        print("================================================================================")
        print("Thank you!")
        print("================================================================================")
        break

    else:
        print("================================================================================")
        print("Invalid option. Try again.")
        print("================================================================================")
