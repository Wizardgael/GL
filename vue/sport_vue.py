from vue.common import Common
from exceptions import ResourceNotFound, Error, InvalidData

class Sportvue:
    """
    Member Vue
    Members interface features
    """

    def __init__(self, sport_controller):
        self._common = Common()
        self.sport_controller = sport_controller

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def search_sport(self):
        name = self._common.ask_name('name')
        member = self.sport_controller.search_sport(name)
        return member

    def add_sport(self):
        data = {}
        data['name'] = self._common.ask_name(key_name="name")
        data['description'] = self._common.ask_name(key_name="description")
        print()
        return self.sport_controller.create_sport(data)
    
    def update_sport(self):
        sport = self.search_sport()
        data = {}
        print("Update Member")
        print()
        data['name'] = self._common.ask_name(key_name="name", default=sport['name'])
        data['description'] = self._common.ask_name(key_name="description", default=sport['description'])
        print()
        return self.sport_controller.update_sport(sport['id'], data)
    
    def delete_sport(self):
        sport = self.search_sport()
        self.sport_controller.delete_sport(sport['id'])
        self.succes_message()
        return
    
    def show_sports(self):
        sports = self.sport_controller.list_sports()

        print("Sports: ")
        for sport in sports:
            print("* %s :%s" % (sport['name'],sport['description']))

    