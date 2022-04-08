from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from . import ui
from django.contrib.auth.models import User, ContentType, Group, Permission
from . import controller


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_to_meny = True
    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_to_meny = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Group)


class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_to_meny = True
    add_window = edit_window = ModelEditWindow.fabricate(model=Permission, model_register=controller.observer)


class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ui.UserAddWindow
