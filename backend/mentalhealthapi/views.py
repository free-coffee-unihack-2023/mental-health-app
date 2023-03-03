from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
import json


class MusicAPI(APIView):
     def post(self, request, *args, **kwargs):
        sentiment = request.data.get('sentiment')
  
        try: 
            result = {"song": "Sample song for sentiment: " + sentiment}
            response = HttpResponse(json.dumps(result), content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename=export.json'
            return response
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

