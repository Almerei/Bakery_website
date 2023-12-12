from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['DB_CONECTTION_STRING']
print(f"DB Connection String: {db_connection_string}")

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

# ... rest of your code ...


def load_bakers_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM bakery"))
    bakers = []
    for row in result.all():
      bakers.append(row)
    return bakers


# ... (остальной код)


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM bakery WHERE id = :val").params(val=id))
    row = result.fetchone()

  if row is None:
    return None
  else:
    return row
