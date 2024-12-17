from fastapi import FastAPI

from app.presentation.api.controllers.routers import (
    add_address,
    add_social_netw_profile,
    change_bio,
    change_contacts,
    change_fullname,
    change_username,
    create_profile,
    create_user,
    delete_address,
    delete_profile,
    delete_social_netw_profile,
    get_profile_by_id,
    get_user_by_id,
    get_user_profiles,
)


def setup_roters(app: FastAPI) -> None:
    app.include_router(add_address.router, tags=["Profile"])
    app.include_router(add_social_netw_profile.router, tags=["Profile"])
    app.include_router(change_bio.router, tags=["Profile"])
    app.include_router(change_contacts.router, tags=["User"])
    app.include_router(change_fullname.router, tags=["Profile"])
    app.include_router(change_username.router, tags=["User"])
    app.include_router(create_profile.router, tags=["Profile"])
    app.include_router(create_user.router, tags=["User"])
    app.include_router(delete_address.router, tags=["Profile"])
    app.include_router(delete_profile.router, tags=["Profile"])
    app.include_router(delete_social_netw_profile.router, tags=["Profile"])
    app.include_router(get_profile_by_id.router, tags=["Profile"])
    app.include_router(get_user_by_id.router, tags=["User"])
    app.include_router(get_user_profiles.router, tags=["Profile"])
