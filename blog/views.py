from django.shortcuts import render

posts = [
    {
        'author': 'Harold',
        'title' : 'Blog Post 1',
        'content' : 'First post contenct',
        'data_posted' : 'April 25, 2019'
    },
    {
        'author': 'John',
        'title' : 'Blog Post 2',
        'content' : 'Second post contenct',
        'data_posted' : 'April 26, 2019'
    },
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
