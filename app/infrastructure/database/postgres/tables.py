from sqlalchemy import UUID, Column, ForeignKey, Integer, MetaData, String, Table

metadata = MetaData()

user_table = Table(
    "users",
    Column("user_id", UUID, primary_key=True),
    Column("email", String(255), unique=True, nullable=True),
    Column("phone_number", Integer, unique=True, nullable=True),
    Column("username", String(255), unique=True, nullable=False),
    Column("status", String(255), nullable=False),
)

profile_table = Table(
    "profiles",
    Column("profile_id", UUID, primary_key=True),
    Column("profile_owner_id", UUID, ForeignKey("users.user_id")),
    Column("first_name", String(255), nullable=False),
    Column("last_name", String(255), nullable=True),
    Column("middle_name", String(255), nullable=True),
    Column("bio", String(255), nullable=False),
    Column("status", String(255), nullable=False),
)

social_netw_profile_table = Table(
    "social_netw_profiles",
    Column("social_netw_profile_id", UUID, primary_key=True),
    Column("social_netw_profile_owner_id", UUID, ForeignKey("profiles.profile_id")),
    Column("social_netw_profile_name", String(255), nullable=False),
    Column("social_netw_profile_link", String(255), nullable=False),
)

address_table = Table(
    "addresses",
    Column("address_id", UUID, primary_key=True),
    Column("address_owner_id", UUID, ForeignKey("profiles.profile_id")),
    Column("country", String(255), nullable=False),
    Column("city", String(255), nullable=False),
    Column("street", String(255), nullable=False),
    Column("house_number", Integer, nullable=False),
    Column("apartament_number", Integer, nullable=True),
    Column("postal_code", String(255), nullable=False),
)
