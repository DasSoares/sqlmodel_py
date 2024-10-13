from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///orm.db")
Session = sessionmaker(bind=engine)
