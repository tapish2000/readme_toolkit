from django.shortcuts import render, redirect
from django.http import FileResponse
from readme_form.api_call import *
from readme_form.integrate import *
import os
import cloudinary
import cloudinary.uploader

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
        "readme_present" : False,
        "error" : False
    }
    if request.method == "POST":
        global details
        details = {
            'repo-link' : request.POST.get('repo-link')
        }

        try:
            details['meta-data'] = api_call(details['repo-link'])
        except:
            print("ERROR: Unable to access github API")
            context['error'] = True
            return render(request, 'readme_form/home.html', context)

        if details['meta-data']['community-profile']['files']['readme']:
            context['readme_present'] = True
            score_data, score = score_generator(details['repo-link'])
            print(score, score_data[0])
            context['score'] = score
            context['score_data'] = score_data
            profile = customize_profile(details['meta-data']['community-profile'])
            context['profile'] = profile
            context['repo_link'] = details['repo-link']
            return render(request, 'readme_form/home.html', context)
        return redirect('detail/') 
    return render(request, 'readme_form/home.html', context)

def detail(request):
    context = {
        "usecases" : usecases,
        "genres" : genres
    }
    if request.method == "POST":
        global details
        details['purpose'] = request.POST.get('purpose')
        details['license-name'] = request.POST.get('license-name')
        details['license-url'] = request.POST.get('license-url')
        details['usecase'] = request.POST.getlist('usecase[]')
        details['genre'] = request.POST.getlist('genre[]')
        details['images'] = None

        print('\n\nDetails: ' + str(details))

        return redirect('installation/')
    
    return render(request, 'readme_form/detail.html', context)

def installation(request):
    if request.method=="POST":
        description = request.POST.get('description')
        code = request.POST.get('code')
        if description != None and code != None:
            install_steps.append({'description': description,'code': code})
    return render(request, 'readme_form/installation.html', {'install_steps': install_steps})

def usage(request):
    if request.method=="POST":
        description = request.POST.get('description')
        code = request.POST.get('code')
        usage_steps.append({'description':description,'code':code})
    return render(request, 'readme_form/usage.html', {'usage_steps': usage_steps})

def output(request):
    if request.method == 'POST':
        global details
        length = request.POST.get('images-length')
        images = []
        for i in range(int(length)):
            images.append(cloudinary.uploader.upload(request.FILES.get('images' + str(i)))['url'])
        print(images)
        details['images'] = images
        raw_output, html_output = integrate(details, install_steps, usage_steps)
        profile = customize_profile(details['meta-data']['community-profile'])
        context = {
            "raw_output" : raw_output,
            "profile" : profile,
            "html_output" : html_output
        }
        # return render(request, 'readme_form/output.html', context)

    raw_output, html_output = integrate(details, install_steps, usage_steps)
    profile = customize_profile(details['meta-data']['community-profile'])
    context = {
        "raw_output" : raw_output,
        "profile" : profile,
        "html_output" : html_output
    }
    return render(request, 'readme_form/output.html', context)

def download(request):
    filename = 'output_README.md'
    readme_f = open(filename, 'r')
    response = FileResponse(readme_f.read(), content_type='file/markdown')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response