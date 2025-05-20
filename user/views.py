from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

import user
from user.form import UserForm
from user.models import User


# Create your views here.
# fbv
def user_list(request):

    users = user.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'user/user_list.html', context)

def user_detail(request, pk):
    users= User.objects.get(id=pk)

    return render(request, 'user/user_detail.html', {'users': users})


def user_post(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('user_list')

        else:
            return render(request, 'user/user_post.html', {'form': form})


# cbv_views
# 사용자 목록
class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'


# 사용자 상세페이지
class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'
    paginate_by = 10



# 사용자 작성
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_post.html'
    success_url = reverse_lazy('user_list')  # 작성 후 리디렉션 위치
