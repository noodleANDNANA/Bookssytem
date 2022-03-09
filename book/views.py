from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from book.models import BookInfo
from people.models import PeopleInfo
# Create your views here.
def selectall(request):
    book_all = BookInfo.objects.all()
    book_one = BookInfo.objects.get(id=1)
    book_add = BookInfo.objects.create(name="云边有个小米卖部", pub_date='2022-03-01')
    # 更新数据
    book_update = BookInfo.objects.filter(id=1).update(readcount=50)
    # 删除数据
    book_delete = BookInfo.objects.filter(id=4).delete()
    # 查询名字包含 水的 书籍
    book_sel_name = BookInfo.objects.filter(name__contains="水")
    # 查询名字以 义 字结尾的书籍
    book_end_name = BookInfo.objects.filter(name__endswith="义")
    """
    gt   大于
    get   大于等于
    lt   小于
    lte   小于等于
    """
    # 查询id数据库中ID编号小于3 的数据
    book_gt_value = BookInfo.objects.filter(id__lt=3)
    # 查询书籍ID 不为3的图书
    book_id_not = BookInfo.objects.exclude(id=3)
    # 查询当前阅读总量
    book_readcount = BookInfo.objects.aggregate(Sum('readcount'))
    """
    1.书籍和人物的关系是1：n的
    2.书籍里面没有任何关于人物的字段
    3.人物表中是有关于数据的字段 book 外键
    利用关联查询：
    （1）已知 主表数据 关联查询从表数据
    主表模型.关联模型表类目小写_set.all()
     (2)已知 按照 从表数据查询 主表数据
     从表模型.外键
    """
    book_value = BookInfo.objects.get(id=1)
    book_peoplevalue= book_value.peopleinfo_set.all()

    """
    关联查询的筛选：
    
    """
    bookname = BookInfo.objects.filter(peopleinfo__name='刘玄德')
    booknames = PeopleInfo.objects.filter(book_id__name="三国演义")
    return render(request, "index.html", {"bookall": book_all})
# 设置cookie信息
def setcookie(request):
    value = request.GET.get("name")
    httpresponse = HttpResponse("set_cookie")
    httpresponse.set_cookie("name", value)
    return httpresponse

# 读取cookie
def getcookie(request):
    cookievalue = request.COOKIES.get("name")
    return HttpResponse(cookievalue)

# 设置session信息
def setsession(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    user = {}
    user["username"] = username
    user["password"] = password
    request.session["users"] = user
    return HttpResponse(user)
# 读取session信息
def getsession(request):
    user = request.session.get("users")
    return HttpResponse(user["username"])
