from vue.common import Common
from exceptions import ResourceNotFound, Error, InvalidData

class MemberVue:
    """
    Member Vue
    Members interface features
    """

    def __init__(self, member_controller):
        self._common = Common()
        self._member_controller = member_controller
        self.member = None

    def add_member(self):
        # Show subscription formular
        data = {}
        print("BDS Subscription")
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname")
        data['lastname'] = self._common.ask_name(key_name="lastname")
        data['email'] = self._common.ask_email()
        print()
        return self._member_controller.create_member(data)

    def show_member(self, member: dict):
        print("Member profile: ")
        print("\t" + member['firstname'].capitalize(), member['lastname'].capitalize())
        print("\temail:", member['email'])
        print("\tsport ", member['sports'])
        s = "No"
        if member['coach']:
                s = "Yes sport coached %s" %(member['coached'])
        print("\tis coach", s)

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_members(self):

        members = self._member_controller.list_members()

        print("Members: ")
        for member in members:
            s = "No"
            if member['coach']:
                s = "Yes"
            c = ""
            if member['coached'].__len__() > 0:
                c = "sport coached:["
                for i in member['coached']:
                    c+= i
                    if(member['coached'].index(i) < member['coached'].__len__()-1):
                        c += ", "
                c += "]"
            print("* %s %s (%s)\n\tsport:%s\n\tcoach:%s %s" % (member['firstname'].capitalize(),
                                                  member['lastname'].capitalize(),
                                                  member['email'], member['sports'], s, c))


    def search_member(self):
        firstname = self._common.ask_name('firstname')
        lastname = self._common.ask_name('lastname')
        member = self._member_controller.search_member(firstname, lastname)
        return member

    def update_member(self):
        member = self.search_member()
        data = {}
        print("Update Member")
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname", default=member['firstname'])
        data['lastname'] = self._common.ask_name(key_name="lastname", default=member['lastname'])
        data['email'] = self._common.ask_email(default=member['email'])
        print()
        return self._member_controller.update_member(member['id'], data)
    
    def update_self_member(self):
        member = self.member
        data = {}
        print("Update Member")
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname", default=member['firstname'])
        data['lastname'] = self._common.ask_name(key_name="lastname", default=member['lastname'])
        data['email'] = self._common.ask_email(default=member['email'])
        print()
        self.member = self._member_controller.update_member(member['id'], data)
        return self.member

    def delete_member(self):
        member = self.search_member()
        self._member_controller.delete_member(member['id'])
        self.succes_message()
        return
    
    def add_sport_to_member(self):
        member = self.search_member()
        sport = self._common.ask_name(key_name="sport name")
        self._member_controller.add_sport(member, sport)
        return

    def remove_sport_to_member(self):
        member = self.search_member()
        sport = self._common.ask_name(key_name="sport name")
        self._member_controller.remove_sport(member, sport)
        return

    def add_coach_to_sport(self):
        sport = self._common.ask_name(key_name="sport name")
        member = self.search_member()
        self._member_controller.add_coach(member, sport)
        return
    
    def remove_coach_to_sport(self):
        sport = self._common.ask_name(key_name="sport name")
        member = self.search_member()
        self._member_controller.remove_coach(member, sport)
        return
    
    def add_self_sport(self):
        sport = self._common.ask_name(key_name="sport name")
        self._member_controller.add_sport(self.member, sport)
        return

    def remove_self_sport(self):
        sport = self._common.ask_name(key_name="sport name")
        self._member_controller.remove_sport(self.member, sport)
        return