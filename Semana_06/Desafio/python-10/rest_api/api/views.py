from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from collections import Counter



@api_view(['POST'])
def lambda_function(request):
    request_data = request.data.get('question')
    counter = Counter()
    for numero in request_data:
        counter[numero] += 1

    result = []

    for item in Counter(counter).most_common():
        for contador in range(item[1]):
            result.append(item[0])
    return Response({"Result": result})
