import sqlalchemy as db

engine = db.create_engine('sqlite:///users.db')

metadata_obj = db.MetaData()

profile = db.Table(
    'users',
    metadata_obj,
    db.Column('tg_id', db.String, primary_key=True),
    db.Column('region', db.String)
)

metadata_obj.create_all(engine)