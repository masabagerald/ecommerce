from catalog.models import Category
from Leather_shop import settings

def leather_shop(request):
    return {

        'active_categories':Category.objects.filter(is_active =True),
        'site_name': settings.SITE_NAME,
        'meta_keybords':settings.META_KEYWORDS,
        'meta_description':settings.META_DESCRIPTION,
        'request':request



    }

