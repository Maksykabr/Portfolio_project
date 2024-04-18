from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class GetHomePage(APIView):
    def get(self, request, format=None):

        return render(request, 'portfolio_project/index.html')
