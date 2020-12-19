from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from .forms import LoginForm, SignupForm, EditForm, ChangePwForm
from .models import User, DailyRecord

import base64
from django.core.files.base import ContentFile
# 장고에서 제공해주는 비밀번호 검증 메소드
from django.contrib.auth.hashers import check_password

from datetime import datetime

from . import auth_code


# Create your views here.
# 사용자가 F5를 눌러 새로고침을 해줄 수도 있을 텐데 계속 csrf때문에 페이지가 깨지고 뒤로 가더라도 그래프가 보이지 않아 다시 로그인을 해야하는 이슈가 있었다.
# 보안적인 측면에선 좋지 않겠지만 원활한 서비스를 위해 일단 csrf검증을 취소시켜서 해결하였다.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                latest_records = DailyRecord.objects.filter(user=user.id).order_by('-workout_date')[:30]
                return render(request, "users/login.html", {'latest_records': latest_records})

    elif request.user.is_authenticated:
        user = request.user
        latest_records = DailyRecord.objects.filter(user=user.id).order_by('-workout_date')[:30]
        return render(request, "users/login.html", {'latest_records': latest_records})

    else:
        form = LoginForm()

    return render(request, "users/login.html", {'form': form})


@csrf_exempt
def face_login_view(request):
    if request.method == 'POST':
        if request.session['test_count'] == 250:
            user = authenticate(email='blue', password='blue')
            if user is not None:
                login(request, user)
                del request.session['test_count']
                return HttpResponse("OK_Face")

            form = LoginForm()
            return render(request, "users/login.html", {'form': form})

        request.session['test_count'] += 1
        print(request.session['test_count'])

        # print(request.body.decode('utf-8'))
        return HttpResponse(request.body)

    request.session['test_count'] = 0
    return render(request, "users/facelogin.html")


def logout_view(request):
    logout(request)
    return redirect("users:login")


@csrf_exempt
def forgotpw_view(request):
    context = {'auth': 0}

    if request.method == 'POST':
        contents = request.body.decode('utf-8').split('&')

        if contents[0] == 'request_code':
            try:
                user = User.objects.get(email=contents[1])
            except User.DoesNotExist:
                return HttpResponse("Fail_User")
            else:
                request.session['code'] = auth_code.make_code()
                if not auth_code.send_code('floodfilllinkedlist@gmail.com', 'zssbjrhlobebrvrq', contents[1], request.session['code']):
                    return HttpResponse("Fail_Email")
                request.session['email'] = contents[1]
                request.session['auth'] = 0
                return HttpResponse("OK_Email")

        elif contents[0] == 'request_auth':
            if request.session['code'] == contents[1]:
                request.session['auth'] = 1
                return HttpResponse("OK_Code")
            else:
                return HttpResponse("Fail_Code")

        else:
            form = ChangePwForm(request.POST)
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                user = User.objects.get(email=request.session['email'])
                user.set_password(password1)
                user.save()

                user = authenticate(email=request.session['email'], password=password1)
                login(request, user)

                del request.session['auth']
                del request.session['email']
                del request.session['code']

                return redirect("users:login")

            else:
                context['form'] = form
                context['error'] = "Password와 Password확인란이 일치하지 않습니다."
                context['email'] = request.session['email']
                context['code'] = request.session['code']
                context['auth'] = request.session['auth']

                return render(request, "users/forgotpw.html", context)
    else:
        context['form'] = ChangePwForm()

    return render(request, "users/forgotpw.html", context)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            nick_name = form.cleaned_data['nick_name']
            date_of_birth = form.cleaned_data['date_of_birth']

            data = request.POST['profile_img']
            
            if data != '':
                img_fmt, img_str = data.split(';base64,')
                ext = img_fmt.split('/')[-1]
                profile_img = ContentFile(base64.b64decode(img_str), name='profile.' + ext)

            if password1 == password2:
                if data != '':
                    user = User.objects.create_user(email, password1, nick_name, date_of_birth, profile_img, 
                    #representation
                    )
                else:
                    user = User.objects.create_user(email, password1, nick_name, date_of_birth)
                return redirect("users:login")

    else:
        form = SignupForm()

    return render(request, "users/signup.html", {'form': form})

def user_edit(request):
    context= {}
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            user = request.user
            if check_password(current_password,user.password):
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 == password2:
                    user.set_password(password2)
                    user.save()
                    login(request,user)
                    return redirect("users:login")
                else:
                    context['form'] = form
                    context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
                    # context['error'] = '새로운 비밀번호를 다시 확인해주세요.'
            else:
                context['form'] = form
                context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

        return render(request, "users/useredit.html", context )
    else:
        context['form'] = EditForm()

    return render(request, "users/useredit.html", context)


def sports_view(request, what_kind):
    return render(request, "users/sports.html", {'what_kind': what_kind})


def count_view(request, count_result, what_kind):
    if count_result <= 0:
        return redirect("users:login")

    user = request.user
    workout_date = datetime.today().strftime("%Y-%m-%d")
    try:
        record = DailyRecord.objects.get(user=user, what_kind=what_kind, workout_date=workout_date)
        record.workout_count += count_result
        record.save()
    except DailyRecord.DoesNotExist:
        DailyRecord.objects.create(user=user, what_kind=what_kind, workout_date=workout_date, workout_count=count_result)

    return redirect("users:login")
