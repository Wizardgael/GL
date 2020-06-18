
from model.database import DatabaseEngine
from controller.member_controller import MemberController
from vue.user_vue import UserVue
from exceptions import Error


def main():
    print("Welcome of BDS Association")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()
    admin_controller = MemberController(database_engine)
    UserVue(admin_controller).user_shell()


if __name__ == "__main__":
    main()
