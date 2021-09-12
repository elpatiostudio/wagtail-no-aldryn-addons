from django.db.models import TextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class HomePage(Page):
    pass


class TestPage(Page):

    body = TextField()

    content_panels = Page.content_panels + [FieldPanel('body')]
