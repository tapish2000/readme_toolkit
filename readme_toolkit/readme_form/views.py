from django.shortcuts import render

install_steps = []
usage_steps = []
details = {}

usecases = [
    ["Developers", "Businesses", "Students"],
    ["Education", "Social Welfare", "Research"],
    ["Health", "Other"]
]

genres = [
    ["Frontend Development", "Backend Development", "AI"],
    ["Mobile App Development", "Database", "ML"],
    ["Data Visualization", "Devops", "Testing"],
    ["Backend as a Service", "Framework", "Software"],
    ["Static Site Generators", "Game Engines", "Automation"],
    ["Social Networking", "Other"]
]

def home(request):
    context = {
        "usecases": usecases,
        "genres": genres
    }
    if request.method == "POST":
        details = {
            'repoLink' : request.POST.get('repoLink'),
            'purpose' : request.POST.get('purpose'),
            'license-name' : request.POST.get('license-name'),
            'license-url' : request.POST.get('license-url'),
            'usecase' : request.POST.getlist('usecase[]'),
            'genre' : request.POST.getlist('genre[]')
        }
        return render(request, 'readme_form/installation.html',{'install_steps':install_steps}) 
    return render(request, 'readme_form/home.html', context)

def installation(request):
    if request.method=="POST":
        description = request.POST.get('description')
        code = request.POST.get('code')
        install_steps.append({'description':description,'code':code})
    return render(request, 'readme_form/installation.html',{'install_steps':install_steps})

def usage(request):
    if request.method=="POST":
        description = request.POST.get('description')
        code = request.POST.get('code')
        usage_steps.append({'description':description,'code':code})
    return render(request, 'readme_form/usage.html',{'usage_steps':usage_steps})
