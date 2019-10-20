# File created by my own

''' Code for video no 6

def index(request):
    return HttpResponse("<h1>Hello Karan</h1> <a href = https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9> Code with Python </a> <br> <a href = https://codewithharry.com> Code With Harry </a>")
def about(request):
    return HttpResponse("Hello Karan Kaushal")

    '''
from django.http import HttpResponse
from django.shortcuts import render
def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))
def index(request):
    #params = {'name': 'Karan Kaushal', 'place': 'Hoshiarpur'}
    return render(request, 'index.html')
    # return HttpResponse("<h1>Home</h1>")

def analyze(request):
    #Get the text from user
    djText = request.POST.get('text', 'default')
    # Checking checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(removepunc) #Required for development Purposes
    print(djText) #Required for development Purposes
    if removepunc == 'on':
    # Analyze the text
        punctuation_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        #analyzed = djText
        analyzed = ""
        for char in djText:
            if char not in punctuation_list:
                analyzed += char
        params = {'purpose': 'Remove punctuation', 'analyzed_Text': analyzed}
        return render(request, 'Analyze.html', params)
    elif fullcaps == 'on':
        analyzed = ""
        for char in djText:
            analyzed += char.upper()
        params = {'purpose': 'Changing to Uppercase', 'analyzed_Text': analyzed}
        return render(request, 'Analyze.html', params)
    elif extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djText):
            if not(djText[index]==" " and djText[index+1]==" "):
                analyzed += char
        params = {'purpose': 'Extra Space Remover', 'analyzed_Text': analyzed}
        return render(request, 'Analyze.html', params)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djText:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
'''
def Capitalize_First(request):
    return HttpResponse("<h1>Capitalize first</h1>")
def new_line_remove(request):
    return HttpResponse("<h1>New line remove</h1>")
def charCount(request):
    return HttpResponse("<h1>Character count</h1>")
def spaceRemove(request):
    return HttpResponse("<h1>Space remove</h1><a href='/'>Back</a>")
'''
