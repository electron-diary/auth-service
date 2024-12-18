from dishka import Provider, Scope, provide

from app.application.commands.add_address import AddAddress
from app.application.commands.add_social_netw_profile import AddSocialNetwProfile
from app.application.commands.chanage_fullname import ChangeFullname
from app.application.commands.change_bio import ChangeBio
from app.application.commands.change_contacts import ChangeContacts
from app.application.commands.change_username import ChangeUsername
from app.application.commands.create_profile import CreateProfile
from app.application.commands.create_user import CreateUser
from app.application.commands.delete_address import DeleteAddress
from app.application.commands.delete_profile import DeleteProfile
from app.application.commands.delete_social_netw_profile import DeleteSocialNetwProfile
from app.application.queries.get_profile_by_id import GetProfileById
from app.application.queries.get_user_by_id import GetUserById
from app.application.queries.get_user_profiles import GetUserProfiles


class HandlersProvider(Provider):
    scope = Scope.REQUEST

    add_address = provide(AddAddress)
    add_social_netw_profile = provide(AddSocialNetwProfile)
    change_fullname = provide(ChangeFullname)
    change_bio = provide(ChangeBio)
    change_contacts = provide(ChangeContacts)
    change_username = provide(ChangeUsername)
    create_profile = provide(CreateProfile)
    create_user = provide(CreateUser)
    delete_address = provide(DeleteAddress)
    delete_social_netw_profile = provide(DeleteSocialNetwProfile)
    delete_profile = provide(DeleteProfile)
    get_profile_by_id = provide(GetProfileById)
    get_user_by_id = provide(GetUserById)
    get_user_profiles = provide(GetUserProfiles)
