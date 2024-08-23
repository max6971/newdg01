from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> ЭТО ПЕРВАЯ СТРАНИЦА </h1>")
def data(request):
    html_content = """
    <html>
    <head>
        <title>Первая страница</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; text-align: center; }
            h1 { color: #333; }
            img { width: 300px; height: auto; margin-top: 20px; }
            p { color: #555; font-size: 18px; }
        </style>
    </head>
    <body>
        <h1>Это первая страница</h1>
        <img src="/static/myapp/image1.jpeg" alt="Пример изображения">
        <p>Добро пожаловать на первую страницу нашего сайта!</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def test(request):
    html_content = """
    <html>
    <head>
        <title>Вторая страница</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #e9f7ef; text-align: center; }
            h1 { color: #444; }
            img { width: 300px; height: auto; margin-top: 20px; }
            p { color: #666; font-size: 18px; }
        </style>
    </head>
    <body>
        <h1>Это вторая страница</h1>
        <img src="/static/myapp/image2.jpg" alt="Пример изображения">
        <p>На этой странице вы найдете много интересной информации.</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)




# Create your views here.
