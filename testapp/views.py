from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.forms import PasswordChangeForm
from listings.models import listing_model
from .filters import UserFilter
#from .models import Signup

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form=UserRegisterForm()
    return render(request,'signup.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Password updated successfully')
            my_view(request)
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct below error')
    else:
        form=PasswordChangeForm(request.user)
    return render(request, 'password_update.html', {'form': form})

# Password update email
def my_view(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
        send_mail('Password', 'Your Password has been updated.', 'pallavikancharla158@gmail.com', [email], fail_silently=False)
        return HttpResponse('Mail send')
    
#search and printing all the details
def home(request):
    tasks = listing_model.objects.all()
    user_filter = UserFilter(request.GET, queryset=tasks)
    tasks= user_filter.qs
    context={'user_filter': user_filter, 'tasks': tasks}
    return render(request, 'home.html', context)

# contact info
