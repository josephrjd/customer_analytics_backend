from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
import time
from customer_analytics_backend.user_decode import decodeUser

# Create your views here.
class First(APIView):
    def get(self, request, *args):
        print(decodeUser(request))
        time.sleep(10)
        return JsonResponse(None, status=status.HTTP_200_OK, safe=False)