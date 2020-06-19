
from controller.member_controller import MemberController
from controller.sport_controller import SportController
from model.database import DatabaseEngine
from vue.admin_vue import AdminVue


def main():
    print("Welcome of BDS Association")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()
    sport_controller = SportController(database_engine)
    admin_controller = MemberController(database_engine, sport_controller)
    AdminVue(admin_controller, sport_controller).admin_shell()
    

if __name__ == "__main__":
    main()
