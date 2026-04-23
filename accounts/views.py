from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bienvenue {user.get_full_name()} !')
            return redirect('dashboard')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bon retour {user.get_full_name()} !')
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté.')
    return redirect('login')


@login_required
def dashboard_view(request):
    user = request.user

    if user.is_teacher:
        from projects.models import Project
        from applications.models import Application

        my_projects = Project.objects.filter(teacher=user)
        total_projects = my_projects.count()
        open_projects = my_projects.filter(status='open').count()
        total_applications = Application.objects.filter(
            project__teacher=user
        ).count()
        pending_applications = Application.objects.filter(
            project__teacher=user,
            status='pending',
        ).count()
        recent_applications = Application.objects.filter(
            project__teacher=user
        ).select_related('student', 'project').order_by('-applied_at')[:5]

        context = {
            'total_projects': total_projects,
            'open_projects': open_projects,
            'total_applications': total_applications,
            'pending_applications': pending_applications,
            'recent_applications': recent_applications,
            'my_projects': my_projects[:5],
        }
        return render(request, 'accounts/dashboard_teacher.html', context)

    if user.is_student:
        from applications.models import Application
        from projects.models import Project

        my_applications = Application.objects.filter(
            student=user
        ).select_related('project', 'project__teacher')

        total_applications = my_applications.count()
        accepted = my_applications.filter(status='accepted').count()
        pending = my_applications.filter(status='pending').count()
        rejected = my_applications.filter(status='rejected').count()
        available_projects = Project.objects.filter(status='open').count()

        context = {
            'my_applications': my_applications[:5],
            'total_applications': total_applications,
            'accepted': accepted,
            'pending': pending,
            'rejected': rejected,
            'available_projects': available_projects,
        }
        return render(request, 'accounts/dashboard_student.html', context)

    return redirect('admin:index')