from django.shortcuts import render

posts = [
    {
        'author': 'Adam',
        'title': 'Blog Post 1',
        'content': 'Post 1 content',
        'published': 'January 9, 2021'
    },
    {
        'author': 'Eve',
        'title': 'Blog Post 2',
        'content': 'Post 2 content',
        'published': 'January 9, 2021'
    }
]

def homepage(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})
