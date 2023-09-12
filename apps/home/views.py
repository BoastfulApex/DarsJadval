from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from apps.authentication.models import *
from apps.main.models import *
from apps.main.forms import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
import pandas as pd


@login_required(login_url="/login/")
def index(request):
    FILIAL = {
        "Institut": "Jismoniy tarbiya va sport bo'yicha mutaxassislari qayta tayyorlash va malakasini oshirish "
                    "instituti",
        "Nukus Filiali": "Jismoniy tarbiya va sport bo'yicha mutaxassislari qayta tayyorlash va malakasini oshirish "
                         "instituti Nukus Filiali",
        "Samarqand filiali": "Jismoniy tarbiya va sport bo'yicha mutaxassislari qayta tayyorlash va malakasini "
                             "oshirish instituti Samarqand filiali",
        "Farg'ona filali": "Jismoniy tarbiya va sport bo'yicha mutaxassislari qayta tayyorlash va malakasini oshirish "
                           "instituti Farg'ona filali"

    }

    teachers = Teacher.objects.all()
    study_groups = StudyGroup.objects.all()
    context = {
        'filial': request.user.filial,
        'filial_name': FILIAL[f'{request.user.filial}'],
        'segment': 'dashboard',
        'teachers_count': len(teachers),
        'study_groups_count': len(study_groups),
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def teachers(request):
    my_queryset = Teacher.objects.filter(filial=request.user.filial).all().order_by('id')
    search_query = request.GET.get('q')
    if search_query:
        my_queryset = my_queryset.filter(Q(name__icontains=search_query))
    paginator = Paginator(my_queryset, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'segment': 'teachers'
    }
    return render(request, 'home/teachers.html', context)


@login_required(login_url="/login/")
def teachers_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.filial = request.user.filial
            instance.save()
            return redirect('home-teachers')
    else:
        form = TeacherForm()

    return render(request,
                  'home/teacher_create.html',
                  {'form': form, 'segment': "teachers", 'filial': request.user.filial})


def teacher_detail(request, pk):
    teacher = Teacher.objects.get(id=pk)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home-teachers')
    else:
        form = TeacherForm(instance=teacher)

    return render(request,
                  'home/teacher_detail.html',
                  {'form': form, 'segment': 'teachers', 'filial': request.user.filial})


class TeacherDelete(DeleteView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('home-teachers')


def teachers_file_create(request):
    if request.method == 'POST':
        form = TeacherFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            print(uploaded_file)
            with open('temp.xls', 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            df = pd.read_excel('temp.xls')
            for i in df.index:
                name = df['Ismi'][i]
                zoom = df['Zoom Link'][i]
                desc = df['Izoh'][i]
                teacher = Teacher.objects.create(
                    name=name,
                    zoom_link=zoom,
                    description=desc,
                    filial=request.user.filial
                )
                teacher.save()
            return redirect('home-teachers')
    else:
        form = TeacherFileForm()

    return render(request,
                  'home/teacher_file_create.html',
                  {'form': form, 'segment': "teachers", 'filial': request.user.filial})


@login_required(login_url="/login/")
def study_groups(request):
    queryset = StudyGroup.objects.filter(filial=request.user.filial).all().order_by('id')
    search_query = request.GET.get('q')
    if search_query:
        queryset = queryset.filter(Q(name__icontains=search_query))
    paginator = Paginator(queryset, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'segment': 'study_group'
    }
    return render(request, 'home/teachers.html', context)
