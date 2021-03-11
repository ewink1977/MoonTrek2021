# FUNCTION FOR FINDING A RANDOM ARTICLE TO DISPLAY!
# def randomArticle():
#         fromModel = random.randint(1, 3)
#         if fromModel == 1:
#             last = Character.objects.all().count()
#             randIndex = random.randint(1, last)
#             randomArticle = Character.objects.get(id = randIndex)
#         if fromModel == 2:
#             last = Ship.objects.all().count()
#             randIndex = random.randint(1, last)
#             randomArticle = Ship.objects.get(id = randIndex)
#         if fromModel == 3:
#             last = PlacesAndItems.objects.all().count()
#             randIndex = random.randint(1, last)
#             randomArticle = PlacesAndItems.objects.get(id = randIndex)
#         return randomArticle