from django.shortcuts import render,redirect,HttpResponse#render渲染,redirect重定向
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required#判断是否登录
# Create your views here.


@login_required(login_url='login')#判断是否登录,如果末登陆就重定向到登录
def home(request):
    if request.method == "POST":
        if request.POST["待办事项"] == '':
            content = {"清单": Todo.objects.filter(todouser=request.user),'警告':'请输入内容!'}
            return render(request,'todonow/home.html',content)
        else:
            # request.user.username

            a_row = Todo(todouser=request.user,todothing=request.POST['待办事项'])
            a_row.save()
            content={"清单":Todo.objects.filter(todouser=request.user),'信息':'添加成功!'}
            return render(request,'todonow/home.html',content)
    elif request.method == "GET":
        #content = {"清单": Todo.objects.all()}

        content = {"清单": Todo.objects.filter(todouser=request.user)}
        print(content)
        return render(request, 'todonow/home.html', content)


def about(request):
    return render(request,'todonow/about.html')


def edit(request,每一件事_id):

    if request.method == "POST":
        if request.POST["已修改事项"] == '':
            return render(request, 'todonow/edit.html', {'警告': '请输入内容!'})
        else:
            a = Todo.objects.get(id=每一件事_id)
            a.todothing = request.POST["已修改事项"]
            a.save()
            return redirect('todonow:主页')
    elif request.method == "GET":
        a = Todo.objects.get(id=每一件事_id)
        content = {"待修改事项": a.todothing}
        return render(request,'todonow/edit.html',content)



def delete(request,每一件事_id):
    a= Todo.objects.get(id=每一件事_id)
    a.delete()
    return redirect('todonow:主页')

def cross(request,每一件事_id):
    if request.POST['完成状态']=='已完成':
        a = Todo.objects.get(id=每一件事_id)
        a.tododone=True
    else:
        a = Todo.objects.get(id=每一件事_id)
        a.tododone = False
    a.save()
    return redirect('todonow:主页')

def timeing(request,每一件事_id):

    a= Todo.objects.get(id=每一件事_id)
    b= int(request.POST['计时状态'])
    if b>1051982140862:
        b=0
    print(a.todoworktime,'+',b)
    a.todoworktime += b
    wm = a.todoworktime

    s, w = divmod(wm, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    a.todogshm="%02d:%02d:%02d" % (h, m, s)
    a.save()
    # 1
    return redirect('todonow:主页')

