from db_configs.connection import Session
from db_configs.tables import Cryptos, Monitoring


def insert_crypto(session, coin):
    crypto = session.query(Cryptos).filter_by(id=coin['id']).first()

    if not crypto:
        crypto = Cryptos(
            id=coin['id'],
            name=coin["name"],
            symbol=coin["symbol"],
            infinite_supply=coin["infinite_supply"],
            max_supply=coin["max_supply"],
        )
        session.add(crypto)
        session.flush()
    else:
        if crypto.infinite_supply != coin["infinite_supply"]:
            crypto.infinite_supply = coin["infinite_supply"]
        if crypto.max_supply != coin["max_supply"]:
            crypto.max_supply = coin["max_supply"]

    return crypto.id


def insert_monitoring(session, crypto_id, coin):
    monitoring = Monitoring(
        crypto_id=crypto_id,
        price=coin["price"],
        rank=coin["rank"],
        circulating_supply=coin["circulating_supply"],
        market_cap=coin["market_cap"],
        volume_24h=coin["volume_24h"],
        percent_change_24h=coin["percent_change_24h"],
        timestamp=coin["timestamp"],
    )
    session.add(monitoring)


def insert_all(data):
    with Session() as session:
        for coin in data:
            crypto_id = insert_crypto(session, coin)
            insert_monitoring(session, crypto_id, coin)

        session.commit()