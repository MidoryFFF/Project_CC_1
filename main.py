import os
isRunning = True
username = os.getlogin()
pathFromMainRunner = "<path>"
while isRunning:
    terminalInput = input(f"{username}:{pathFromMainRunner} ")
    command = terminalInput.split()[0]
    match command:
        case "exit":
            isRunning = False
        case "echo":
            print(terminalInput[5:])
        case "ls":
            print("ls")
        case "cd":
            print("cd <path>")
        case _:
            print("Command not found")

def FindArgsInBrackets(_string):
    if (_string.find('"').count() == 2):
        return _string[1::-1].split()
    else:
        return ""
