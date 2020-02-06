from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .models import *
from .forms import StaffProfileForm, StaffEditProfileForm
from examcard.models import StudentProfile, Fee, Log, Report, Unit, StudentUnit
from examcard.forms import UserLoginForm, StudentProfileForm, UserRegisterForm, ReportForm, StudentUnitForm


# @login_required(login_url='examcard:login')
def staff_dashboard(request):
    try:
        staff_qs = Fee.objects.filter(profile_id = request.user.staffprofile.id)
        return render(request, 'staff/index.html', {'staff_qs':staff_qs})
    except ObjectDoesNotExist:
        return redirect('/staff/create_profile/')



@staff_member_required(login_url='admin:login')
@login_required(login_url='examcard:login')
def attendance_reg(request):
    register_qs = Report.objects.filter(user_id = request.user.id).order_by('-id')
    return render(request, 'staff/register.html', {'report_list_qs':register_qs})


@staff_member_required(login_url='admin:login')
@login_required(login_url='examcard:login')
def exam_card_scanner(request):
    context = {}
    try:
        if request.method == "POST":
            qs = request.POST['q'].split()[4:][0]
            # print(qs)
            profile_qs = StudentProfile.objects.get(adm_number = qs)
            fee_qs = Fee.objects.get(profile_id = profile_qs.id)
            log_save = Log.objects.create(
                user_id = request.user.id,
                profile_id = profile_qs.id,
                fee_id = fee_qs.profile_id,

            )
            log_save.save()
            # print(profile_qs.id)
            context['profile_qs'] = profile_qs
            context['fee_qs'] = fee_qs
            # create logs

            return render(request, 'staff/scanner.html', context)
        else:
            return render(request, 'staff/scanner.html', context)
    except:
        messages.success(request, f'Scanning error: NO QR Code Captured for scanning. Please capture again!!!')
        return render(request, 'staff/scanner.html', context)
    
@login_required(login_url='examcard:login')
def staff_create_profile(request):
    context = {}
    if request.method == 'POST':
        form = StaffProfileForm(request.POST, request.FILES)
        if form.is_valid():

            staff_qs =staff.objects.filter(user_id=request.user.id)
            if staff_qs.count() == 1:
                user = profile_qs.first()
                messages.success(
                    request, f'{request.user.staffprofile.first_name} Had Created Profile Successfully !')
                return redirect('/staff/create_profile/')
            else:
                obj = form.save(commit=False)
                obj.user_id = request.user.id
                obj.save()
                messages.success(
                    request, f'{request.user.staffprofile.first_name} Created Successfully !')
                return redirect('/staff/stafprofile')
        else:
            profileform = StudentProfileForm()
            context['profileform'] = profileform
            messages.success(
                request, f'{request.user.username} fill all the fields correctly!')
            return redirect('/staff/create_profile/')
    else:
        profileform = StudentProfileForm()
        context['profileform'] = profileform
    return render(request, 'staff/staffcreate_profile.html', context)

def staffprofile(request):
    if not request.user.is_authenticated:
       return render(request, 'pages/login.html')
    else:
        args = {'user': request.user}
        return render(request, "staff/staprofile.html", args)


    