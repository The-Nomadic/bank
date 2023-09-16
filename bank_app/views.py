from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import District, Branch, UserData


# Create your views here.

def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('bank_app:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "User created")
                return redirect('bank_app:login')
        else:
            messages.info(request, "Password doesn't match")
            return redirect('bank_app:register')

    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, "Success")
            return redirect('bank_app:welcome')
        else:
            messages.info(request, "Username or Password is wrong")
            return redirect('bank_app:login')

    return render(request, 'login.html')


def form(request):
    districts = District.objects.all()

    if request.method == "POST":
        name = request.POST.get('name', '')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        phone = request.POST.get('phone_number', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        district_id = request.POST['district']
        branch_id = request.POST['branch']
        account_type = request.POST.get('account_type', '')
        material = request.POST.get('material_provided', '')

        district = District.objects.get(pk=district_id)
        branch = Branch.objects.get(pk=branch_id)

        user_data = UserData(name=name, dob=dob, age=age, gender=gender, phone=phone, email=email, address=address,
                             district=district, branch=branch, account_type=account_type, material=material)
        user_data.save()
        messages.info(request, "Form created")

    return render(request, 'form.html', {'districts': districts})


def get_branches_by_district(request, district_id):
    try:
        district = District.objects.get(pk=district_id)
        branches = Branch.objects.filter(district=district)
        data = [{'id': branch.id, 'name': branch.name} for branch in branches]
        return JsonResponse(data, safe=False)
    except District.DoesNotExist:
        return JsonResponse([], safe=False)


def welcome(request):
    return render(request, 'welcome.html')


def logout(request):
    auth.logout(request)
    return redirect('bank_app:home')
