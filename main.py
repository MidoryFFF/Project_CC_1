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

def FindArgs(_string):
    return _string.split()

def main():
    isRunning = True
    print("Path to VFS: " + pathToVFSDerectory)
    print("Path to main: " + pathToMainRunner)
    while isRunning:
        path = PathTransformer()
        terminalInput = input(f"{username}@{hostname}:{path} ")
        command = terminalInput.split()[0]
        args = terminalInput.split()[1:]
        match command:
            case "exit":
                isRunning = False
            case "echo":
                print(terminalInput[5:])
            case "ls":
                print(*FindArgs("ls " + ' '.join(args)))
            case "cd":
                print(*FindArgs("cd " + ' '.join(args)))
            case _:
                print("Command not found")


#Во избежание ошибок при импорте в тесты
if (__name__ == "__main__"):
    main()
