from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseForbidden, HttpResponse

roles = list(RoleGroup.objects.all().values_list('name', flat=True))
role_context = {
    'roles': roles
}
def index(request):
    return render(request, 'register/register.html', role_context)
    

def register(request):
    # errors = User.objects.validator(request.POST)
    
    # if len(errors):
    #     for tag, error in errors.iteritems():
    #         messages.error(request, error, extra_tags=tag)
    #     return redirect('/')
    
    form = RegistrationForm(request.POST)
    if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
        if not User.objects.filter(email=request.POST['email']).exists():
        
            hashed_password = make_password(request.POST['password'])


            user = User.objects.create(name=request.POST['name'],
                                    email=request.POST['email'],
                                    mobile=request.POST['mobile'],
                                    country=request.POST['country'], 
                                    nationality=request.POST['nationality'], 
                                    password=hashed_password)
            
            user.save()

            user  = User.objects.get(email=request.POST['email'])
            role = RoleGroup.objects.get(name=request.POST['role'])
            
            user_group = UserGroup.objects.create(user=user,
                                    role_group=role)
                                    
            user_group.save()
            request.session['id'] = user.name
            
            string = str(user.name) + ' ' + 'has been registered succesfully. Please Login.'
            messages.success(request, string)
            return redirect('/login_page')
        
        # elif User.objects.filter(email=request.POST['email']).exists():
        #     user_id  = User.objects.get(email=request.POST['email']).user_id
        #     role_id = RoleGroup.objects.get(name=request.POST['role']).role_id
        #     if not UserGroup.objects.filter(user=user_id).filter(role_group=role_id).exists():
        #         hashed_password = make_password(request.POST['password'])


        #         user = User.objects.create(name=request.POST['name'],
        #                                 email=request.POST['email'],
        #                                 mobile=request.POST['mobile'],
        #                                 country=request.POST['country'],
        #                                 nationality=request.POST['nationality'], 
        #                                 password=hashed_password)
        #         user.save()
        #         user_group = UserGroup.objects.create(user=user_id,
        #                                 role_group=role_id)
                                        
        #         user_group.save()
        #         request.session['id'] = user.user_id
        #         return redirect('/success')
    
    elif form.data['password'] != form.data['confirm_password']:
        form.add_error('password', 'The passwords do not match.')
        err = '<html><body>' + str(form.errors) + '</html></body>'
        return HttpResponse(err)
    else:
        err = '<html><body>' + str(form.errors) + '</html></body>'
        return HttpResponse(err)
    


def login(request):

    if (User.objects.filter(email=request.POST['login_email']).exists()):

        user = User.objects.get(email=request.POST['login_email'])
        role_id = RoleGroup.objects.get(name = request.POST['role']).role_id
        
        if not UserGroup.objects.filter(user=user).filter(role_group = role_id).exists():
            string = 'You are not allowed to login as ' + request.POST['role'] + '. Choose another role for login.'
            messages.success(request, string)
            return redirect('/login_page')

        if  check_password(request.POST['login_password'],user.password):

            request.session['id'] = user.user_id
            request.session['role'] = request.POST['role']
            
            # if request.POST['role'] == 'admin':
            #     return render(request, 'register/admin.html', context)
                
            # elif request.POST['role'] == 'staff':
            #     return render(request, 'register/staff.html', context)
        
            # elif request.POST['role'] == 'editor':
            #     return render(request, 'register/editor.html', context)
            
            # elif request.POST['role'] == 'student':
            #     return render(request, 'register/student.html', context)
            return redirect('/dashboard')
        else:
            
            string = 'Incorrect Password. Please Try Again.'
            messages.success(request, string)
            return redirect('/login_page')
    else:
            string = 'User does not Exist. Please Register.'
            messages.success(request, string)
            return redirect('/')
    



def success(request):
    context = {
        "user": request.session['id']
    }
    return render(request, 'register/success.html', context)

def login_page(request):
    return  render(request, 'register/login.html', role_context)
        
def dashboard(request):
    user = User.objects.get(user_id=request.session['id'])
    context= {
                    'name': user.name,
                    'email':user.email,
                    'phone': user.mobile,
                    'country':user.country,
                    'role':request.session['role'].capitalize()
                }
    if request.session['role']  == 'admin':
        return render(request, 'register/admin.html', context)
                
    elif request.session['role']  == 'staff':
        return render(request, 'register/staff.html', context)
        
    elif request.session['role']  == 'editor':
        return render(request, 'register/editor.html', context)
            
    elif request.session['role']  == 'student':
        return render(request, 'register/student.html', context)


def failed(request):
    context = {
        "error": None
    }
    return render(request, 'register/failed.html', context)


       