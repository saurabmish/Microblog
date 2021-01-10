from django.shortcuts import render

posts = [
    {
        'name': 'Adam',
        'title': 'Blog Post 1',
        'content': 'Post 1 content',
        'published': 'January 9, 2021'
    },
    {
        'name': 'Eve',
        'title': 'Blog Post 2',
        'content': 'Post 2 content',
        'published': 'January 9, 2021'
    }
]

def homepage(request):
    context = {
        'posts': posts
    }
    return render(request, 'static/home.html', context)

def about(request):
    return render(request, 'static/about.html', {'title': 'About'})
