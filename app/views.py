
from rest_framework.views import APIView
from rest_framework.response import Response
from ai_utils.utils import get_vision_statement
from django.core.mail import send_mail


class MainView(APIView):

    def post(self, request):

        data = request.data
        print('////////////////////////////////////////////////////////////////////')
        print(data)

        # vision_statement = get_vision_statement(data)
        vision_statement = data
        send_mail(
            'Your Vision Statement',
            vision_statement['data'],
            'markosmuche2018@gmail.com',
            ['markos@mindlink.space'],
            fail_silently=False,
        )

        return Response(vision_statement)
        