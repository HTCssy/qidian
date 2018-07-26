from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render,redirect

from apps.book.models import Book, Nav, BookClass, BookClass1

from django.forms.models import model_to_dict
#导行
def nav(request):
    result = {}
    #获取导航
    nav0 = Nav.objects.values("nav_name")#返会的是querysetvalues的数据
    #转为列表
    nav1 = list(nav0)
    #添加到字典
    result.update(msg='success', status=200, nav=nav1)
    #返回json数据
    return HttpResponse(JsonResponse(result), content_type="application/json")

#一级分类
def book_class(request):
    result = {}
    #获取一级分类信息
    books = BookClass.objects.values("class_name", "class_url")
    #转为列表
    class_names = list(books)
    #添加到字典
    result.update(msg='success', status=200, class_names=class_names)
    #转换json数据返回
    return HttpResponse(JsonResponse(result), content_type="application/json")

#本周强推
#方法
def week_until(id):
    #查询一级分类
    bookclass = BookClass(book_class_id=id)
    #获取一级分类数据
    bookclass_name = BookClass.objects.filter(book_class_id=id).first()
    #获取书名
    bookname = Book.objects.filter(book_class_1_id=bookclass.book_class_id).first()
    classname = {
        'bookclass_name': model_to_dict(bookname),
        'bookname': model_to_dict(bookclass_name)
    }
    return classname
def week(request):
    result = {}
    add = {}
    #返回不同分类的书名
    xuanhuan = week_until(1)
    qihuan = week_until(2)
    xianshi = week_until(6)
    youxi = week_until(8)
    #添加到字典
    add.update(xuanhuan=xuanhuan, qihuan=qihuan, xianshi=xianshi, youxi=youxi)
    #添加到字典
    result.update(msg='success', status=200, data=add)
    #返回json数据
    return HttpResponse(JsonResponse(result), content_type="application/json")



#分类方法
def get_name(id):
    result = {}
    data = []
    test = {}
    # 查询二级分类信息
    class_name_list = BookClass1.objects.filter(book_class_id=id).values('book_class_1_id', 'class_name_1')
    for class_name_1 in class_name_list:
        data.append(class_name_1['book_class_1_id'])
        for id in data:
            # 返回书名信息
            booknames = Book.objects.filter(book_class_1_id=id).values('book_name',
                                                                       'book_img',
                                                                       'book_author',
                                                                       'book_text')
            if len(booknames):
                # 二级分类绑定书名信息
                test[class_name_1['class_name_1']] = list(booknames)
    # 添加到字典
    result.update(msg='success', status=200, data=test)
    # 转为json数据返回
    return result

#玄幻类
def xuanhuan(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def xuanhuan_name(request):
   result = get_name(1)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#奇幻类
def qihuan(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def qihuan_name(request):
   result = get_name(2)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#武侠
def wuxia(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def wuxia_name(request):
   result = get_name(3)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#仙侠
def xianxia(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def xianxia_name(request):
   result = get_name(4)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#都市
def dushi(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def dushi_name(request):
   result = get_name(5)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#现实
def xianshi(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def xianshi_name(request):
   result = get_name(6)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#军事
def junshi(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def junshi_name(request):
   result = get_name(7)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#历史
def lishi(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def lishi_name(request):
   result = get_name(8)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#游戏
def youxi(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def youxi_name(request):
   result = get_name(9)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#体育
def tiyu(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def tiyu_name(request):
   result = get_name(10)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#科幻
def kehuan(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def kehuan_name(request):
   result = get_name(11)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#灵异
def lingyi(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def lingyi_name(request):
   result = get_name(12)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#女生网
def nvshengwang(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def nvshengwang_name(request):
   result = get_name(13)
   return HttpResponse(JsonResponse(result), content_type="application/json")

#二次元
def erciyuan(request):
    #重定向html
    return redirect('/static/home/xuanhuan.html')
def erciyuan_name(request):
   result = get_name(2)
   return HttpResponse(JsonResponse(result), content_type="application/json")






def book_class_1(request):
    pass

def book_name_all(request):
    name = Book.objects.get(book_id=1)
    return HttpResponse('1111')


