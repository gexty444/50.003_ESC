from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView

from ..decorators import student_required
from ..forms import StudentSignUpForm
from ..models import Student, User


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        userdetail = form.save(commit=False)
        userdetail.phase = 1
        userdetail = form.save()
        login(self.request, userdetail)
        return redirect('students:student_main')


@method_decorator([login_required, student_required], name='dispatch')
class StudentMainView(TemplateView):
    template_name = 'classroom/students/student_main.html'

