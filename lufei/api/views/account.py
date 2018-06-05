from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
import uuid


class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000}

        username = request.data.get('user')
        password = request.data.get('pwd')
        print(555555555555555555555555555555555555555,username,password)
        user = models.Account.objects.filter(username=username,password=password).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserAuthToken.objects.update_or_create(user=username,defaults={'token':uid})
            ret['token'] = uid
        return Response(ret)