from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantsListSerializer


# Complete me! I should be your APIListView
class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()    #queryset should NOT change here.
	serializer_class = RestaurantsListSerializer

