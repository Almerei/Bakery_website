from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONECTTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


def load_bakers_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM bakery"))
    bakers = []
    for row in result.all():
      bakers.append(row)
    return bakers