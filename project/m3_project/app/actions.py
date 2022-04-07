from .models import ContentType, User, Group, Permission
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from . import ui


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_to_meny = True

    edit_window = add_window = ModelEditWindow.fabricate(model)

    columns = [
        {
            'data_index': 'name',
            'sortable': True,
            'sort_fields': ('name', 'codename',)

        },
        {
            'data_index': 'content_type',
            'sortable': True,
            'sort_fields': ('content_type',)
        },
        {
            'data_index': 'codename',
            'sortable': True,
            'sort_fields': ('codename',)
        }
    ]


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_to_meny = True

    edit_window = add_window = ModelEditWindow.fabricate(model)

    columns = [
        {
            'data_index': 'name',
            'sortable': True,
            'sort_fields': ('name', 'codename',)

        },
        {
            'data_index': 'content_type',
            'sortable': True,
            'sort_fields': ('content_type',)
        },
        {
            'data_index': 'codename',
            'sortable': True,
            'sort_fields': ('codename',)
        }
    ]


class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_to_meny = True

    edit_window = add_window = ModelEditWindow.fabricate(model)

    columns = [
        {
            'data_index': 'name',
            'sortable': True,
            'sort_fields': ('name', 'codename',)

        },
        {
            'data_index': 'content_type',
            'sortable': True,
            'sort_fields': ('content_type',)
        },
        {
            'data_index': 'codename',
            'sortable': True,
            'sort_fields': ('codename',)
        }
    ]


class UserPack(ObjectPack):
    model = User
    add_window = ui.UserAddWindow
    edit_window = ui.UserEditWindow
    add_to_desktop = True
    add_to_meny = True
    columns = [
        {
            'data_index': 'name',
            'sortable': True,
            'sort_fields': ('name', 'codename',)

        },
        {
            'data_index': 'content_type',
            'sortable': True,
            'sort_fields': ('content_type',)
        },
        {
            'data_index': 'codename',
            'sortable': True,
            'sort_fields': ('codename',)
        }
    ]
