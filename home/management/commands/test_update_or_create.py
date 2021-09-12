from django.core.management.base import BaseCommand
from wagtail.core.models import Site

from home.models import TestPage


class Command(BaseCommand):
    help = 'Import content from Wagtail Documents PDFs'

    # def add_arguments(self, parser):
    #     # Named (optional) arguments
    #     parser.add_argument(
    #         '--force',
    #         action='store_true',
    #         help='Force all events to be imported regardless of last time updated',
    #     )

    def handle(self, *args, **options):
        current_site = Site.objects.first()

        page_title = "This will be awesome"
        page_body = "yes indeed"
        test_page, created = TestPage.objects.update_or_create(
            defaults={'title': page_title},
            body=page_body)
        if created:
            current_site.root_page.add_child(instance=test_page)

        test_page.save_revision()
