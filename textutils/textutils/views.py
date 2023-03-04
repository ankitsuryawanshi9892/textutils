
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #GEt and analyze the text
    print(request.GET.get('text','default'))
    djtext=request.POST.get('text','default')

    #Check checkbox value
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover = request.POST.get("newlineremover",'off')
    charcounter = request.POST.get("charcounter",'off')
    if removepunc=='on' and fullcaps=='on':
        analyzed= ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char.upper()
                params = {'purpose': 'Removing Punctuation and Capitalizing text','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif removepunc=='on' and newlineremover=='on':
        analyzed=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations and char!='/n':
                analyzed+=char
                params = {'purpose': 'Removing Punctuation and removing newline','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    if removepunc=="on":
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
                params = {'purpose': 'Remove Punctuations','analyzed_text':analyzed}
    #Analyze the text
        return render(request,'analyze.html',params)
    elif fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed= analyzed+char.upper()
            params = {'purpose': 'Change to Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif newlineremover=='on':
        analyzed=''
        for char in djtext:
            if char!='\n':
                analyzed= analyzed+char
                params = {'purpose': 'Remove Newline Character','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif charcounter=="on":
        analyzed=0
        for char in djtext:
            if char!=' ':
                analyzed+=1
                params = {'purpose': 'Character counter','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")

