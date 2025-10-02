import os
import socket

username = os.getlogin()
hostname = socket.gethostname()
pathToMainRunner = os.path.abspath(__file__)
pathToVFSDerectory = os.path.dirname(__file__) + "\\VFS"
corretPath = pathToMainRunner

def PathTransformer():
    #Если файл в котором находиться пользователь основной, то он будет отображаться как ~$
    if (corretPath == pathToMainRunner):
        return "~$"
    else:
        return corretPath

def FindArgsInBrackets(_string):
    if (_string.find('"').count() == 2):
        return _string[1::-1].split()
    else:
        return ""

def main():
    isRunning = True
    print("Path to VFS: " + pathToVFSDerectory)
    print("Path to main: " + pathToMainRunner)
    while isRunning:
        path = PathTransformer()
        terminalInput = input(f"{username}@{hostname}:{path} ")
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

if (__name__ == "__main__"):
    main()
