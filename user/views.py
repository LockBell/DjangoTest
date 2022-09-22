import json
import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from user import models
from user.models import Member


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data['id']
        password = data['password']
        user = Member.objects.filter(Q(login_id=user_id) & Q(password=password))
        if len(user) == 0:
            raise ValidationError('비밀번호 또는 아이디가 틀렸습니다.')
        else:
            response = HttpResponse("로그인 완료")
            response.set_cookie('token', user[0].id)
        return redirect('blogs')

    def get(self, request):
        return render(request, 'login.html')


@method_decorator(csrf_exempt, name='dispatch')
class SingUp(View):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data['id']
        password = data['password'].strip()
        password_check = data['password-check'].strip()
        email = data['email'].strip()
        # 비밀번호, 이메일 유효성 검증
        if not email:
            raise ValidationError('이메일이 공백으로 존재할 수 없습니다.')
        elif password_check != password:
            raise ValidationError('비밀번호가 일치하지 않습니다.')
        elif not password:
            raise ValidationError('비밀번호를 공백으로 사용할 수 없습니다.')
        elif not re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$").match(email):
            raise ValidationError('이메일의 형식이 일치하지 않습니다.')
        else:
            user = User.objects.create(username=user_id, password=password)
            member = models.Member(user=user, email=email, login_id=user_id, password=password)
            member.save()
        # return redirect('login')
        return JsonResponse({"member": member}, status=201)

    def get(self, request):
        return render(request, 'singup.html')
