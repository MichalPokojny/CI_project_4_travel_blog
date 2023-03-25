from .models import Category


def categories(request):
    """
    Define a method that takes a request object and return a dictrionary
    containing all the category objects in the database.
    This will be availible as context processor to all templates
    """
    return {'cat_items': Category.objects.all()}
