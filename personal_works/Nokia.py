print("\t\t\t\t\t WELCOME TO YOUR PHONE!:)")

print("""**List of menu functions**
            1.Phonebook
            2.Messages
            3.Chat
            4.Call register
            5.Tones
            6.Settings
            7.Call divert
            8.Games
            9.Calculator
            10.Reminders
            11.Clock
            12.Profiles
            13.SIM services
            0.Press 0 to go back """)


menu_list = int(input("Select an option: "))
if menu_list == 1:
    print(f"""  1.Search
                2.Service Nos
                3.Add name
                $.Erase
                5.Edit
                6.Assign tone
                7.Send b'card
                8.Options 
                9.Speed dials
                10.Voice tags 
                0.Press 0 to go back """)
    if menu_list == 0 or menu_list != 1:
        print(f"""  1.Search
                2.Service Nos
                3.Add name
                $.Erase
                5.Edit
                6.Assign tone
                7.Send b'card
                8.Options 
                9.Speed dials
                10.Voice tags 
                0.Press 0 to go back """)
    user_input = int(input("Select a number "))
    if user_input == 8:
        print("1.type of view\n2.Memory status")
elif menu_list == 2:
    print()



