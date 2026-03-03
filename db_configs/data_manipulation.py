from connection import Base, engine, Session
from tables import Cryptos, Monitoring

Base.metadata.create_all(engine)