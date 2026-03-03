from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import declarative_base
import dotenv
import os

dotenv.load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database_name = os.getenv("DB_NAME")

url = f"postgresql://{user}:{password}@{host}:{port}/{database_name}"
engine = create_engine(url)
Base = declarative_base()

class Cryptos(Base):
    __tablename__ = 'cryptos'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    symbol = Column(String(255))
    infinite_supply = Column(Boolean)
    max_supply = Column(Numeric(20,2)) # Há algumas coins com frações de supply.


class Monitoring(Base):
    __tablename__ = 'monitoring'

    # Os números de precisão parecem aleatórios, mas há um motivo. Usar 25 como máximo de precisão vem do fato que
    # em vários testes o manior número de casas decimais foi 20, logo, uso 25 para ter uma segurança. Price usa 20
    # de escala pois há algumas "memecoins" que chegam a 18 casas decimais após a vírgula. O demais que usam 2 é devido
    # ao fato que as casas decimais não são tão relevantes.
    id = Column(Integer, primary_key=True)
    crypto_id = Column(Integer, ForeignKey('cryptos.id'))
    price = Column(Numeric(25,20), nullable=False)
    rank = Column(Integer)
    circulating_supply = Column(Numeric(25,2))
    market_cap = Column(Numeric(25,2))
    volume_24h = Column(Numeric(25,2))
    percent_change_24h = Column(Numeric(5,2))
    timestamp = Column(DateTime, nullable=False)

Base.metadata.create_all(engine)