from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
import secrets
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request,entry):
    entryName = util.get_entry(entry)
    if entryName:
        return render(request,"encyclopedia/entry.html",{
            "entry": markdown.markdown(entryName),
            "entryTitle": entry
        })
    else:
        return render(request,"encyclopedia/entry.Html",{
            "entryTitle":entry,
            
        })  

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title in util.list_entries():
            messages.error(request,"Already Exists")
            return render(request,'encyclopedia/create.html')
        else:    
            util.save_entry(title,content)
            return HttpResponseRedirect(reverse("display",kwargs={"entry":title}))
    return render(request,'encyclopedia/create.html')

def search(request):
        search = []
        query = request.GET.get("q")
        enteries =util.list_entries()
        for entry in enteries:
            if query in entry:
                search.append(entry)
        return render(request,'encyclopedia/search.html',{
                "entries":search
        })    

def random(request):
    entries = util.list_entries()
    randomPage = secrets.choice(entries)
    return HttpResponseRedirect(reverse("display",kwargs={"entry": randomPage}))
   
def editPost(request,entryTitle):
    content = util.get_entry(entryTitle)
    context = {
        "title":entryTitle,
        "content":content
    }
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        getTitle = util.list_entries()
        getContent = util.get_entry(title)
        if title in getTitle and content == getContent:
            messages.error(request,"Alreday exists")
            return render(request,'encyclopedia/edit.html',context)
        else:
            util.save_entry(title,content)
            return HttpResponseRedirect(reverse("display",kwargs={"entry":title}))
    return render(request,'encyclopedia/edit.html',context)

