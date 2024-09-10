from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Indah Cahya Puspitahati',
        'npm' : '2306245453',
        'class': 'PBP A',
        'brand': 'HOODIE-YAY✨',
    }

    return render(request, "main.html", context)