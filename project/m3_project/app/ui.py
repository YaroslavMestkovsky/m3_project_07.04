from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = ext.ExtStringField(
            label=u'content_type',
            name='content_type',
            allow_blank=False,
            anchor='100%')

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class UserEditWindow(BaseEditWindow):
    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = ext.ExtStringField(
            label=u'content_type',
            name='content_type',
            allow_blank=False,
            anchor='100%')

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'
