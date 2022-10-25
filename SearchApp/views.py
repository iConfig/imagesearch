from django.shortcuts import render, redirect 
from .forms import searchForm
from django.contrib import messages 
import requests 

API_URL = "https://rapidapi.p.rapidapi.com/api/Search/ImageSearchAPI"
HEADERS = {
    'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
    'x-rapidapi-key': " YOUR RAPID API KEY GOES HERE "
}

# Create your views here.

def searchView(request):
    if request.method == "POST":
        form = searchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            safe_search = form.cleaned_data['safe_search']
            try:
                q = name 
                page_number = 1 
                page_size = 10
                auto_correct = True 
                safe_search = safe_search

                querystring = {"q": q,
                                "pageNumber": page_number,
                                "pageSize":page_size,
                                "autoCorrect": auto_correct,
                                "safeSearch": safe_search
                                }

                response = requests.get(API_URL, headers=HEADERS, params=querystring).json()

                totalCount = response["totalCount"]

                for image in response["value"]:
                    image_url = image["url"]
                    image_title = image["title"]
                    image_name = image["name"]

                    context = {
                        "image_name":image_name,
                        "image_title":image_title,
                        "image_url":image_url
                    }

                    return render(request, "home.html", context)
            except:
                messages.error(request, "can't find image")
                return redirect("home") 

    form = searchForm()
    return render(request, "home.html", {"form":form})

