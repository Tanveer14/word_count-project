from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    people=["silma","ria","saeem","naeem","maisha"]
    return render(request,'home.html',{'people':people})

'''def take_second(elem):
    return elem[1]'''

def count(request):
    intext=request.GET['text']
    wordlist=intext.split()
    worddict={}
    for w in wordlist:
        if w in worddict:
            worddict[w]+=1
        else:
            worddict[w]=1
    wordtuples=worddict.items()
    wordtuples=sorted(wordtuples,key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{
        'intext':intext,
        'total':len(wordlist),
        'words':wordtuples,
    })

def about(request):
    return render(request,'about.html')