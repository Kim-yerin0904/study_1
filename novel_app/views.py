from django.shortcuts import  redirect,render

# Create your views here.
def my_novel(request, character1, character2):
    context = {"char_1": character1, "char_2":character2 }
    return render(request, 'novel_html.html', context)

