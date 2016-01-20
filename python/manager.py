import sys

class Strings:
    usage = "\nUsage:\nhelp\tPrints this usage screen.\nexit\tExits the program.\n"
    uncmd = "Error: Unrecognized command.\n"

class Subsidiary:
    def exit(self):
        prompt = input("Are you sure?:[y/n] >> ")
        if(prompt == 'y'):
            print("\nGoodbye...")
            sys.exit()
        elif(prompt == 'n'):
            prog.main()
        else:
            print("Please type 'y' or 'n'.\n")
            self.exit()

class Program:
    def main(self):
        task = input(" >> ")
        if(task == "help"):
            print(exscr.usage)
        elif(task == "exit"):
            sub.exit()
        elif(task == ''):
            self.main()
        else:
            print(exscr.uncmd)

exscr = Strings()
sub = Subsidiary()
prog = Program()

i = 1
while i == 1:
    prog.main()
