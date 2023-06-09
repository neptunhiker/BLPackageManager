from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, create_engine, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BLCrew(Base):
    __tablename__ = "BLCrew"

    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String)
    first_name = Column("FirstName", String)
    last_name = Column("LastName", String)
    email = Column("Email", String)
    phone = Column("Phone", String)
    description = Column("Description", String)

    def __init__(
        self, id, title, first_name, last_name, email, phone, description
    ) -> None:
        self.id = id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description

    def __str__(self) -> str:
        return f"BeginnerLuft Mitarbeiter:In {self.title} {self.first_name} {self.last_name}"


class Coach(Base):
    __tablename__ = "coaches"

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    title = Column("Title", String)
    first_name = Column("FirstName", String)
    last_name = Column("LastName", String)
    email = Column("Email", String)
    description = Column("Description", String)
    web_link = Column("WebsiteLink", String)

    def __init__(
        self, title, first_name, last_name, email, description, web_link
    ) -> None:
        self.id = self.id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.description = description
        self.web_link = web_link

    def __str__(self) -> str:
        return f"Coach {self.title} {self.first_name} {self.last_name}"


class Module(Base):
    __tablename__ = "modules"

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    name = Column("Name", String)
    description = Column("Description", String)
    order = Column("Order", String)

    def __init__(self, name, description, order) -> None:
        self.id = self.id
        self.name = name
        self.description = description
        self.order = order

    def __str__(self) -> str:
        return f"Module: {self.name} - {self.description}"


class Package(Base):
    __tablename__ = "packages"

    id = Column("ID", Integer, primary_key=True)
    name = Column("Title", String)
    duration_in_weeks = Column("DurationInWeeks", Integer)
    ues = Column("UEs", Integer)
    sessions_per_week = Column("SessionsPerWeek", Integer)
    ues_per_week = Column("UEsPerWeek", Integer)
    total_sessions = Column("TotalSessions", Integer)
    description = Column("Description", String)
    ues_coach = Column("UEsCoach", Integer)
    ues_bl = Column("UEsBL", Integer)

    def __init__(
        self,
        id,
        name,
        duration_in_weeks,
        ues,
        sessions_per_week,
        ues_per_week,
        total_sessions,
        description,
        ues_coach,
        ues_bl,
    ) -> None:
        self.id = id
        self.name = name
        self.duration_in_weeks = duration_in_weeks
        self.ues = ues
        self.sessions_per_week = sessions_per_week
        self.ues_per_week = ues_per_week
        self.total_sessions = total_sessions
        self.description = description
        self.ues_coach = ues_coach
        self.ues_bl = ues_bl

    def __str__(self) -> str:
        return f"Package {self.name}. Dauer: {self.duration_in_weeks} Wochen. UEs Coach: {self.ues_coach}"


class Participant(Base):
    __tablename__ = "participants"

    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String)
    first_name = Column("FirstName", String)
    last_name = Column("LastName", String)
    email = Column("Email", String)
    phone = Column("Phone", String)
    description = Column("Description", String)

    def __init__(
        self, id, title, first_name, last_name, email, phone, description
    ) -> None:
        self.id = id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description

    def __str__(self) -> str:
        return f"Teilnehmer:In {self.title} {self.first_name} {self.last_name}"


def create_db(path: str) -> None:
    """
    Create a database from scratch with some example entries
    :param path: the path to the database
    """
    engine = create_engine(f"sqlite:///{path}", echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # BL Crew
    session.add(
        BLCrew(
            id=1,
            title="Frau",
            first_name="Beata",
            last_name="Rozwadowska",
            email="beata@testemail.com",
            phone="12312234234",
            description="Beata ist Co-Gründerin von BeginnerLuft",
        )
    )
    session.add(
        BLCrew(
            id=2,
            title="Frau",
            first_name="Lea",
            last_name="Bergmann",
            email="lea@testemail.com",
            phone="3485304",
            description="Lea ist Co-Gründerin von BeginnerLuft",
        )
    )

    # Coaches
    session.add(
        Coach(
            title="Herr",
            first_name="Paul",
            last_name="Matthes",
            email="paul@testmail.com",
            description="Paul ist ein erfahrener Coach, der sich auf systemisches Coaching spezialisiert hat.",
            web_link="wwww.paul.de",
        )
    )
    session.add(
        Coach(
            title="Frau",
            first_name="Anna",
            last_name="Hohmann",
            email="anna@testmail.com",
            description="Anna ist zertifizierte Coach seit 2021.",
            web_link="wwww.anna.de",
        )
    )

    # Modules
    session.add(
        Module(
            name="Erstgespräch & Matching",
            description="Erstgespräch zwischen Teilnehmer:In und BeginnerLuft inkl. Matching mit einem erfahrenen und passenden Coach.",
            order="Beginn"
        )
    )

    session.add(
        Module(
            name="Zielbeschreibung",
            description="Ergründung des Coaching Ziels.",
            order="Ende"
        )
    )

    # Packages
    session.add(
        Package(
            id=1,
            name="A",
            duration_in_weeks=8,
            ues=52,
            sessions_per_week=2,
            ues_per_week=4,
            description="Plan A hat eine vorgesehen Dauer von 8 Wochen und 52 UEs.",
            ues_coach=32,
            ues_bl=20,
        )
    )
    session.add(
        Package(
            id=2,
            name="B",
            duration_in_weeks=8,
            ues=52,
            sessions_per_week=1,
            ues_per_week=3,
            description="Plan B hat eine vorgesehen Dauer von 8 Wochen und 52 UEs.",
            ues_coach=24,
            ues_bl=28,
        )
    )

    session.add(
        Package(
            id=3,
            name="C",
            duration_in_weeks=12,
            ues=52,
            sessions_per_week=2,
            ues_per_week=4,
            description="Plan C hat eine vorgesehen Dauer von 12 Wochen und 52 UEs.",
            ues_coach=48,
            ues_bl=4,
        )
    )

    session.add(
        Package(
            id=4,
            name="D",
            duration_in_weeks=12,
            ues=52,
            sessions_per_week=1,
            ues_per_week=3,
            description="Plan D hat eine vorgesehen Dauer von 12 Wochen und 52 UEs.",
            ues_coach=36,
            ues_bl=16,
        )
    )

    session.commit()


class DataBase:

    def __init__(self, path: str = "databases/bl_db.db") -> None:
        self.engine = create_engine(f"sqlite:///{path}", echo=False)
        self.Session = sessionmaker(bind=self.engine)

    def get_coaches(self) -> list:
        """
        Get all coaches from database
        :return list of coach objects
        """
        session = self.Session()
        return session.query(Coach).all()

    def get_crew_members(self) -> list:
        """
        Get all crew members from database
        :return list of crew member objects
        """
        session = self.Session()
        return session.query(BLCrew).all()

    def get_modules(self) -> list:
        """
        Get all modules from database
        :return list of module objects
        """
        session = self.Session()
        return session.query(Module).all()

    def get_packages(self) -> list:
        """
        Get all packages from database
        :return list of package objects
        """
        session = self.Session()
        return session.query(Package).all()

    def get_participants(self) -> list:
        """
        Get all participants from database
        :return list of participant objects
        """
        session = self.Session()
        return session.query(Participant).all()


if __name__ == "__main__":
    # create_db(path="databases/test_db.db")

    db = DataBase(path="databases/test_db.db")

    for crew_member in db.get_crew_members():
        print(crew_member)

    for module in db.get_modules():
        print(module)

    for package in db.get_packages():
        print(package)

    for participant in db.get_participants():
        print(participant)
