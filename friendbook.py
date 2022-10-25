from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


# # # ###########################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///friendbook.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()
# # # ###########################################


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Foreignkeys
    language_id = Column(Integer, ForeignKey("languages.id"))


def initialize_database():
    """
    Initializes the database and creates all tables.
    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)


def database_add_friend(friend: Friend):
    """
    Database command to add a new friend.
    """
    session.add(friend)


def database_get_all_friends():
    """
    Database command to get all friends.
    """
    all_friends = session.query(Friend).all()
    print(all_friends)


# # # ###########################################
# # # Main
# # # ###########################################
if __name__ == "__main__":
    initialize_database()

    # Example to add a new friend
    new_friend = Friend(email="jack@example.com", first_name="Jack")
    database_add_friend(new_friend)

    # Example to list all friends
    database_get_all_friends()