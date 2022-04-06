from wagtail.contrib.modeladmin.helpers import AdminURLHelper
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from home.models import TestPage


class DummyAdminURLHelper(AdminURLHelper):
    def index_url(self):
        return '/admin/pages/'


class DummyAdmin(ModelAdmin):
    model = TestPage
    menu_label = 'Simple Page'
    menu_icon = 'home'  # change as required
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    menu_order = 100  # will put in 4th place (000 being 1st, 100 2nd)

    def get_url_helper_class(self):
        return DummyAdminURLHelper


modeladmin_register(DummyAdmin)
