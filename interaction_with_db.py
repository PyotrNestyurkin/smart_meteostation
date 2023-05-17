import sqlalchemy as db
from sqlalchemy.orm import Session

engine = db.create_engine("sqlite:///users.db")

metadata = db.MetaData()
users = db.Table('users', metadata,
                 autoload_with=engine)

conn = engine.connect()


def insertion(id, region):
    query = db.update(users).values(region=region).where(users.c.tg_id == id)
    conn.execute(query)
    if not (conn.execute(users.select().where(users.c.tg_id == id)).fetchall()):
        query = db.insert(users).values(tg_id=id, region=region)
        conn.execute(query)
    # output = conn.execute(users.select()).fetchall()
    # print(output)
    print(1)
    with Session(engine) as session:
        session.commit()
    print(2)


def check_if_in_table(id):
    output = conn.execute(users.select()).fetchall()
    print(output)
    try:
        conn.execute(users.select().where(users.c.tg_id == id)).fetchall()

        return True
    except Exception:
        return False


def get_second_part(id):
    try:
        var1 = conn.execute(users.select().where(users.c.tg_id == id)).fetchone()
        output = conn.execute(users.select()).fetchall()
        print(output)
        print(var1)
        return var1[1]
    except Exception as e:
        return e
# insertion(123, 'mos')
# output = conn.execute(division.select()).fetchall()
# print(output)
# stmt = insert('users.db').values(name="spongebob", fullname="Spongebob Squarepants")
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()
