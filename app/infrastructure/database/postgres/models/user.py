from sqlalchemy import Table, UUID, Column, Integer, String


user_table = Table(
    'users',
    Column('user_id', UUID, primary_key=True),
    Column('email', String(255), unique=True, nullable=True),
    Column('phone_number', Integer, unique=True, nullable=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('status', String(255), nullable=False),
)