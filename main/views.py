from django.shortcuts import render ,redirect
from django.urls import reverse
from bs4 import BeautifulSoup as bs
from django.http import HttpResponseRedirect
import request, requests
from . models import *




# Create your views here.

def clear(request):
    News_data.objects.all().delete()
    return HttpResponseRedirect(reverse("xeber_panel"))


def xeber_panel(request):
    
    
    
    
    news = News_data.objects.all()
    count = News_data.objects.all().count()
    
    context = {
        
        'news': news,
        'count': count,
        
        
    }
    return render(request, "main/xeber_panel.html",context)



def news_bot(request):

    data = requests.get("https://lent.az")

    url = bs(data.text,"html.parser")

    soup = url.find("div",class_ = "all-news-wrapper")

    for x in soup:
        
        
        try:
            
            link = x["href"]
            
            data1 = requests.get(link)
            soup1 = bs(data1.text,"html.parser")
            
            category = soup1.find("div",class_ = "breadcrumb_row").find('h3').text
            
            date = soup1.find("div",class_ = "overlay").text.replace("(UTC +04:00)","")
            
            title = soup1.find("h1",class_ = "news_title").text
            
            text = soup1.find("div",class_ = "news_content").text
            # text = ''.join(map(str,text))

            
            image = soup1.find("div",class_ = "news_img").find("img")
            
            image = image["src"]
            
            
            
            weather = soup1.find("div",class_ = "top_section").find_all("li")[3].text            

            
            
        
            News_data(text=text,title=title,date=date,category=category,weather=weather,img=image).save()

        
        
       
            
           

       
        except:TypeError
        
        

    
    return HttpResponseRedirect(reverse("xeber_panel"))


def home(request):
    
    idman = News_data.objects.raw("SELECT * FROM main_news_data WHERE category == 'İDMAN' ")
    
    category = Test.objects.all().distinct()
    
    
    latest = News_data.objects.all()[3:7]
    news01 = News_data.objects.all()[0:1]
    news02 = News_data.objects.all()[1:3]
    news03 = News_data.objects.all()[7:8]
    news04 = News_data.objects.all()[8:9]
    news05 = News_data.objects.all()[9:13]
    news06 = News_data.objects.all()[13:14]
    news07 = News_data.objects.all()[10 :14]
    news08 = News_data.objects.all()[9:12]
    news09 = News_data.objects.all()[5:9]
    news10 = News_data.objects.all()[9:10]
    
    text1 = News_data.objects.all()[5:6]
    text2 = News_data.objects.all()[6:7]
    text3 = News_data.objects.all()[7:8]
    text4 = News_data.objects.all()[8:9]
    
    bigpost = News_data.objects.all()[1:2]
    
    new1 = News_data.objects.all()[1:2]
    new2 = News_data.objects.all()[2:3]
    new3 = News_data.objects.all()[3:4]
    new4 = News_data.objects.all()[4:5]
    sm = News_data.objects.all()[5:9]
    bigg = News_data.objects.all()[9:10]
    line = News_data.objects.all()[9:13]
    tree= News_data.objects.all()[9:12]


    data = News_data.objects.all()[0:4]
    context = {
        
        "data":data,            "bigpost":bigpost,
        'news01':news01,        "new1":new1,
        "news02":news02,        "new2":new2,
        "latest":latest,        "new3":new3,
        'category':category,    "new4":new4,
        "idman":idman,          "sm":sm,
        'news03':news03,        "bigg":bigg,
        'news04':news04,        "line":line,
        'news05':news05,        "tree":tree,
        'news06':news06,
        'news07':news07,
        "news08":news08,
        "news09":news09,
        "news10":news10,
        "text1":text1,
        "text2":text2,
        "text3":text3,
        "text4":text4,
        
        

        
    }
    return render(request,"main/home.html",context)


def news_single(request,id):
    news = News_data.objects.filter(id=id)
    
    context = {
        
        'news':news
        
    }
    return render(request,"main/news-single.html",context)


def about(request):
    return render(request,"main/about.html")



def contact(request):
    return render(request,"main/contact.html")