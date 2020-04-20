def count(request):
    text=request.GET['text']
    words=text.split()
    dictionary={}
    for w in words:
        if w in dictionary:
            dictionary[w]+=1
        else:
            dictionary[w]=1
    #sortedwords=sorted(dictionary.items(),key=take_second,reverse=True)
    sortedwords=sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{
        'text':text,
        'count':len(words),
        'sortedwords':sortedwords,
        })