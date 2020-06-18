
import sys
from vue.member_vue import MemberVue
from exceptions import ResourceNotFound, Error, InvalidData


class UserVue(MemberVue):
    """
    Admin Vue
    Admin specific interfaces
    """

    def __init__(self, member_controller):
        super().__init__(member_controller)

    def connexion(self):
        print("Connexion")
        try:
            self.member = self.search_member()
        except:
           print("Unknown user")
           exit() 
        pass


    def help(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

    def ask_command(self, commands):

        command = input('command > ').lower().strip()
        while command not in commands.keys():
            print("Unknown command")
            command = input('command >').lower().strip()

        return command

    def user_shell(self):

        self.connexion()

        commands = {
            "exit": "Quit the Shell",
            "profile": "show profile member",
            "add sport": "List association members",
            "remove sport": "Show member profile",
            "update profile": "Delete a member",
            "help": "Show this help"
        }

        self.help(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'profile':
                    self.show_member(self.member)
                elif command == 'add sport':
                    self.show_members()
                elif command == 'remove sport':
                    member = self.search_member()
                    self.show_member(member)
                elif command == 'update profile':
                    self.delete_member()
                elif command == 'help':
                    self.help(commands)
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
