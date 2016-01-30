#################################
#                               #
#  Object Oriented Programming  #
#                               #
#################################
import sys
# To help keep things organized,
# classes should consist of two
# captialized words without spaces.

class ExtraMethods:
    def exit(self):
        chk = input("Are you sure?:[y/n] >> ")
        if(chk == "y"):
            print("Goodbye...")
            sys.exit()
        elif(chk == "n"):
            interface.main()
        else:
            print("Error: Please type 'y' or 'n'.")
            self.exit()
class ExtraStrings:
    error = "Error: Unrecognized command."
    usage = "Usage:\n\nexit:\tExits the program.\nhelp:\tDisplays this usage screen."

class CommandInterface:
    def main(self):

        cmd = input(" >> ")

        if(cmd == "exit"):
            methods.exit()
        elif(cmd == "help"):
            print(strings.usage + '\n')
        elif(cmd == ''):
            self.main()
        else:
            print(strings.error + '\n')

# Objects should be all lowercase,
# and should be the second word
# in the class.
methods = ExtraMethods()
strings = ExtraStrings()
interface = CommandInterface()

# Preset variables go here.
i = True

while i == True:
    interface.main()
