from glob import glob
from tkinter.messagebox import NO
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt


nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'view is ..'},
    {'id':3, 'title':'model', 'body':'model is ..'}
]

def HTMLTemplate(articleTag, id=None): 
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>        
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f''' 
            <html>
            <body>
                <h1><a href="/">Django</a></h1>
                <ol>
                    {ol}
                </ol>   
                {articleTag}   
                <ul>
                    <li><a href="/create/">create</a></li>
                    {contextUI}
                </ul>  
            </body>
            </html>  
            ''';


# Create your views here.
def index(request):
    article = '''
    <h2>welcome</h2>
    hello, django
    '''
    return HttpResponse(HTMLTemplate(article));

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form actions="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':        
        title = request.POST['title']
        body = request.POST['title']
        newTopic = {"id":nextId, "title": title, "body":body}
        url = '/read/' + str(nextId)
        nextId = nextId +1
        topics.append(newTopic)
        return redirect(url)
    

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')
    
    
@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectTopic = {
                    "title":topic['title'],
                    "body": topic['body']
                }
        article = f'''
            <form actions="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectTopic["body"]}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')
  
    