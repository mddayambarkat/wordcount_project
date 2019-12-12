#from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html',{"name":"hii thire dayam"})

def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    list_len=len(word_list)

    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html', {"fulltext": data,"word":list_len,"worddictionary":worddictionary,"worddictionary":sorted_list})

#challengees accepetred

def about(request):
    return render(request,'about.html')