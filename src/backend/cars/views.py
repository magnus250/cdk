from rest_framework.response import Response
from rest_framework.views import APIView


class CarListApi(APIView):

    def get(self, request):
        print('123123123123')
        return Response(
            data={'ok?': 'jest ok'}
        )
