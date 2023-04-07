from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class BLRep(Base):
    __tablename__ = "BLCrew"

    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String)
    first_name = Column("FirstName", String)
    last_name = Column("LastName", String)
    email = Column("Email", String)
    phone = Column("Phone", String)
    description = Column("Description", String)

class Coach(Base):
    __tablename__ = "coaches"

    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String)
    first_name = Column("FirstName", String)
    last_name = Column("LastName", String)
    email = Column("Email", String)
    description = Column("Description", String)
    web_link = Column("WebsiteLink", String)

class Module(Base):
    __tablename__ = "modules"

    id = Column("ID", Integer, primary_key=True)
    name = Column("Title", String)
    description = Column("Description", String)
    min_ues = Column("MinUEs", Integer)
    max_ues = Column("MaxUEs", Integer)
    default_owner = Column("DefaultOwner", String)


class Package(Base):
    __tablename__ = "packages"

    id = Column("ID", Integer, primary_key=True)
    name = Column("Title", String)
    duration_in_weeks = Column("DurationInWeeks", Integer)
    ues = Column("UEs", Integer)
    sessions_per_week = Column("SessionsPerWeek", Integer)
    ues_per_week = Column("UEsPerWeek", Integer)
    description = Column("Description", String)
    ues_coach = Column("UEsCoach", Integer)
    ues_bl = Column("UEsBL", Integer)

class Participant(Base):
    __tablename__ = "participants"

    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String)
    first_name = Column("FirstName", String)
    last_name = Column("LastName", String)
    email = Column("Email", String)
    phone = Column("Phone", String)
    description = Column("Description", String)




if __name__ == "__main__":

    engine = create_engine("sqlite:///bl_db.db", echo=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
    print("Test")
