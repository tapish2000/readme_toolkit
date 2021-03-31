from django.shortcuts import render

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
    return render(request, 'readme_form/home.html', context)

def installation(request):
    return render(request, 'readme_form/installation.html')

def usage(request):
    return render(request, 'readme_form/usage.html')
