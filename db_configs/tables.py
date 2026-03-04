from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Numeric, DateTime
from db_configs.connection import Base


class Cryptos(Base):
    __tablename__ = 'cryptos'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    symbol = Column(String(255))
    infinite_supply = Column(Boolean)
    max_supply = Column(Numeric(20,2)) # Há algumas coins com frações de supply.


class Monitoring(Base):
    __tablename__ = 'monitoring'

    # Os números de precisão parecem aleatórios, mas há um motivo. Usar 20 como máximo de precisão vem do fato que
    # em vários testes o manior número de casas decimais foi 20. Price usa 18 de escala pois há algumas "memecoins" que
    # chegam a 18 casas decimais após a vírgula (por isso o aumento no total de dígitos também). Os demais que usam 2 é
    # devido ao fato que as casas decimais não são tão relevantes.

    id = Column(Integer, primary_key=True)
    crypto_id = Column(Integer, ForeignKey('cryptos.id'))
    price = Column(Numeric(36,18), nullable=False)
    rank = Column(Integer)
    circulating_supply = Column(Numeric(20,2))
    market_cap = Column(Numeric(20,2))
    volume_24h = Column(Numeric(20,2))
    percent_change_24h = Column(Numeric(5,2))
    timestamp = Column(DateTime, nullable=False)

