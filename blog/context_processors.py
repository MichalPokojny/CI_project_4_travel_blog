from .models import Category


def categories(request):
    return {'cat_items': Category.objects.all()}