from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# @api_view(['GET', 'POST'])
# def tests(request):

#     return JsonResponse({
#         "msg" : "successs"
#     })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tests(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})