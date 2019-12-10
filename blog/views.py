from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'jhon doe',
        'title': 'Blog Post 1',
        'content': '1st post',
        'date_posted': ' August 27, 2018'
    },
    {
        'author': 'doe kkio',
        'title': 'Blog Post 2',
        'content': '2nd post',
        'date_posted': ' August 27, 2018'
    },
    {
        'author': 'agdum bagdum',
        'title': 'Blog Post 3',
        'content': '3rd post',
        'date_posted': ' August 27, 2018'
    }
]

def home(request):

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})