from sqlalchemy import UUID, BigInteger, Column, ForeignKey, MetaData, String, Table

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("user_id", UUID, primary_key=True),
    Column("email", String(255), unique=True, nullable=True),
    Column("phone_number", BigInteger, unique=True, nullable=True),
    Column("username", String(255), unique=True, nullable=False),
    Column("status", String(255), nullable=False),
)

profile_table = Table(
    "profiles",
    metadata,
    Column("profile_id", UUID, primary_key=True),
    Column("user_id", ForeignKey("users.user_id")),
    Column("first_name", String(255), nullable=False),
    Column("last_name", String(255), nullable=True),
    Column("middle_name", String(255), nullable=True),
    Column("bio", String(255), nullable=False),
    Column("status", String(255), nullable=False),
)

social_netw_profile_table = Table(
    "social_netw_profiles",
    metadata,
    Column("social_netw_profile_id", UUID, primary_key=True),
    Column("profile_id", ForeignKey("profiles.profile_id", ondelete="CASCADE")),
    Column("social_netw_profile_name", String(255), nullable=False),
    Column("social_netw_profile_link", String(255), nullable=False),
)

address_table = Table(
    "addresses",
    metadata,
    Column("address_id", UUID, primary_key=True),
    Column("profile_id", ForeignKey("profiles.profile_id", ondelete="CASCADE")),
    Column("country", String(255), nullable=False),
    Column("city", String(255), nullable=False),
    Column("street", String(255), nullable=False),
    Column("house_number", String(255), nullable=False),
    Column("apartament_number", String(255), nullable=True),
    Column("postal_code", String(255), nullable=False),
)
