def menu():
    print(f"""
    **List of menu functions**
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
    user_input = input("select a number ")
    if user_input == "1":
        Phonebook()
    elif user_input == "2":
        Messages()
    elif user_input == "3":
        Chat()
    elif user_input == "4":
        Call_register()
    elif user_input == "5":
        Tones()
    elif user_input == "6":
        Settings()
    elif user_input == "7":
        Call_divert()
    elif user_input == "8":
        Games()
    elif user_input == "9":
        Calculator()
    elif user_input == "10":
        Reminders()
    elif user_input == "11":
        Clock()
    elif user_input == "12":
        Profiles()
    elif user_input == "13":
        SIM_services()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        menu()


def Phonebook():
    print(f""" 
        **Phone book**
                1.Search
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
    user_input = input("select a number: ")
    if user_input == "8":
        Options()
    elif user_input == "0":
        menu()
    elif user_input == "1":
        Search()
    elif user_input == "2":
        Service_nos()
    elif user_input == "3":
        Add_name()
    elif user_input == "4":
        Erase()
    elif user_input == "5":
        Edit()
    elif user_input == "6":
        Assign_tone()
    elif user_input == "7":
        Send_bcard()
    elif user_input == "9":
        Speed_dials()
    elif user_input == "10":
        Voice_tags()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Phonebook()


def Search():
    print("""EMPTY
            0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Search()


def Service_nos():
    print("""EMPTY
               0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Service_nos()


def Add_name():
    print("""EMPTY
               0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Add_name()


def Erase():
    print("""EMPTY
                  0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Erase()


def Edit():
    print("""EMPTY
                  0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Edit()


def Assign_tone():
    print("""EMPTY
                  0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Assign_tone()


def Send_bcard():
    print("""EMPTY
                  0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Send_bcard()


def Speed_dials():
    print("""EMPTY
                  0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Speed_dials()


def Voice_tags():
    print("""EMPTY
                  0.BACK""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Phonebook()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Voice_tags()


def Options():
    print("""
**Options**
    1. Type of view
    2. Memory status
    3. Back""")
    user_input = input("select a number: ")
    if user_input == "3":
        Phonebook()
    elif user_input == "1":
        Type_of_view()
    elif user_input == "2":
        Memory_status()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Options()


def Type_of_view():
    print("""NOT YET IMPLEMENTED
            0.Back""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Options()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Options()


def Memory_status():
    print("""MEMORY STATUS EMPTY
            0.Back""")
    user_input = input("Press 0 to go back ")
    if user_input == "0":
        Options()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Options()


def Messages():
    print(f""" 
    **Messages**
                1. Write messages
                2. Inbox
                3. Outbox
                4. Picture messages
                5. Templates
                6. Smileys
                7. Message settings
                8.Info service
                9.Voice mailbox number
                10.Service command editor 
                0.Back""")
    user_input = input("select a number ")
    if user_input == "7":
        Message_settings()
    elif user_input == "0":
        menu()
    elif user_input == "1":
        Write_messages()
    elif user_input == "2":
        Inbox()
    elif user_input == "3":
        Outbox()
    elif user_input == "4":
        Picture_messages()
    elif user_input == "5":
        Templates()
    elif user_input == "6":
        Smileys()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Messages()


def Write_messages():
    user_input = input("1.Write a message"
                       "0.Back")
    if user_input == "1":
        print(user_input)
    if user_input == "0":
        Messages()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Write_messages()


def Inbox():
    print("Inbox empty"
          "0.Press 0 to go back")
    user_input = input("Select a number")
    if user_input == "0":
        Messages()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Inbox()


def Outbox():
    print("Outbox empty"
          "0.Press 0 to go back")
    user_input = input("Select a number")
    if user_input == "0":
        Messages()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Outbox()


def Picture_messages():
    print("No pictures found"
          "0.Press 0 to go back")
    user_input = input("Select a number")
    if user_input == "0":
        Messages()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Picture_messages()


def Templates():
    print("No templates available"
          "0.Press 0 to go back")
    user_input = input("Select a number")
    if user_input == "0":
        Messages()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Templates()


def Smileys():
    print("Download smileys online"
          "0.Press 0 to go back")
    user_input = input("Select a number")
    if user_input == "0":
        Messages()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Smileys()


def Message_settings():
    print(f""" 
    **Message_settings**
                1.Set
                2.Common
                3.Back """)
    user_input = input("select a number ")
    if user_input == "1":
        Set()
    elif user_input == "2":
        Common()
    elif user_input == "3" or user_input != "1" or "2":
        Messages()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Message_settings()


def Set():
    print(f"""  
        **Set**
                1. Message centre number
                2. Messages sent as
                3. Message validity
                0.Back """)
    user_input = input("select a number ")
    if user_input == "0":
        Message_settings()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Message_settings()


def Common():
    print(f""" 
        **Common**
                1. Delivery reports
                2. Reply via same centre
                3. Character support 
                0.Back """)
    user_input = input("select a number ")
    if user_input == "0":
        Message_settings()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Message_settings()


def Chat():
    print("Type a message\n 0.Back")
    user_input = input("select a number ")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Chat()


def Call_register():
    print(f"""  
    **Call_register**
                1.Missed calls
                2.Received calls
                3.Dialled numbers
                4.Erase recent call lists
                5.Show call duration
                6.Show call costs
                7.Call cost settings
                8.Prepaid credit
                3.Back """)
    user_input = input("select a number ")
    if user_input == "5":
        Show_call_duration()
    elif user_input == "6":
        Show_call_cost()
    elif user_input == "7":
        Call_cost_settings()
    elif user_input == "3":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Call_register()


def Show_call_duration():
    print(f"""  
    **Show_call_duration**
                1. Last call duration
                2. All calls’ duration
                3. Received calls’ duration
                4. Dialled calls’ duration
                5. Clear timers 
                3.Back """)
    user_input = input("select a number")
    if user_input == "3":
        Call_register()
    else:
        print("INVALID   INPUT")
        menu()


def Show_call_cost():
    print("""   1. Last call cost
                2. All calls’ cost
                3. Clear counters 
                0.Back """)
    user_input = input("select a number")
    if user_input == "0":
        Call_register()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        menu()


def Call_cost_settings():
    print(f"""  1. Call cost limit
                2. Show costs in 
                3.Back """)
    user_input = input("select a number")
    if user_input == "3":
        Call_register()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        menu()


def Tones():
    print(f"""  
    **Tones**
                1. Ringing tone
                2. Ringing volume
                3. Incoming call alert
                4. Composer
                5. Message alert tone
                6. Keypad tones
                7. Warning and game tones
                8. Vibrating alert
                9. Screen saver
                3.Back """)
    user_input = input("select a number ")
    if user_input == "3":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Tones()


def Settings():
    print(f"""  
    **Settings**
                1.Call settings
                2.Phone settings
                3.Security settings
                4.Restore factory settings 
                0.Back """)
    user_input = input("select a number ")
    if user_input == "1":
        Call_settings()
    elif user_input == "2":
        Phone_settings()
    elif UserWarning == "3":
        Security_settings()
    elif user_input == "4":
        Restore_factory_settings()
    elif user_input == "0":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Settings()


def Call_settings():
    print(f"""  1. Automatic redial
                2. Speed dialling
                3. Call waiting options
                4. Own number sending=
                5. Phone line in use
                6. Automatic answer
                3.Back""")
    user_input = input("select a number ")
    if user_input == "3":
        Settings()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Call_settings()


def Phone_settings():
    print(f"""  
    **Phone_settings**
                1. Language
                2. Cell info display
                3. Welcome note
                4. Network selection
                5. Lights2
                6. Confirm SIM service actions
                0.Back""")
    user_input = input("select a number ")
    if user_input == "0":
        Settings()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Call_settings()


def Security_settings():
    print(f"""  
    **Security_settings**
                1. PIN code request
                2. Call barring service
                3. Fixed dialling
                4. Closed user group
                5. Phone security
                6. Change access codes
                3.Back""")
    user_input = input("select a number ")
    if user_input == "3":
        Settings()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Call_settings()


def Restore_factory_settings():
    print(f"""  1.Restore factory settings
                2.Back""")
    user_input = input("select a number ")
    if user_input == "1":
        Restore_factory_settings()
    elif user_input == "2":
        Settings()
    else:
        print("INVALID   INPUT")
        Restore_factory_settings()


def Call_divert():
    print(F"""0.Back""")
    user_input = input("select 0 to go back")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Call_divert()


def Games():
    print(F"""0.Back""")
    user_input = input("select 0 to go back")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Games()


def Calculator():
    print(F"""0.Back""")
    user_input = input("select 0 to go back")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")


def Reminders():
    print(F"""0.Back""")
    user_input = input("select 0 to go back")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Reminders()


def Clock():
    print(f"""  
        **Clock**
                1. Alarm clock
                2. Clock settings
                3. Date setting
                4. Stopwatch
                5. Countdown timer
                6. Auto update of date and time 
                0.Back """)
    user_input = input("select a number ")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT, PLEASE TRY AGAIN")
        Clock()


def Profiles():
    print(F"""0.Back""")
    user_input = input("select 0 to go back")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT")
        Profiles()


def SIM_services():
    print(F"""0.Back""")
    user_input = input("select 0 to go back")
    if user_input == "0":
        menu()
    else:
        print("INVALID   INPUT")
        SIM_services()


menu()
