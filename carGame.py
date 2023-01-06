current_state = ''
while True:
    user_command = input(">")
    latest_command = user_command
    match user_command.lower():
        case "start":
            if current_state != 'started':
                current_state = 'started'
                print("Car started...Ready to go!")
            else:
                print("Car is already going.")
        case "stop":
            if current_state != 'stopped':
                current_state = 'stopped'
                print("Car stopped.")
            else:
                print("Car already stopped.")
        case "quit":
            break
        case _:
            print("I don't understand that...")

    # if user_command.lower() == "start":
    #     print("Car started...Ready to go!")
    # elif user_command.lower() == "stop":
    #     print("Car stopped.")
    # elif user_command.lower() == "quit":
    #     break
    # else:
    #     print("I don't understand that...")
