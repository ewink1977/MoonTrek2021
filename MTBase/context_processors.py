def loadStories(request):
    from MoonTrekStories.models import MoonTrekStories
    return { 'allStories': MoonTrekStories.objects.all() }