from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Autopost
from .forms import AutopostForm, AutopostCreateForm
from .crawl import autocrawl, testautocrawl

def autopost_crawling(request):
    targeturl="https://beomi.github.io/beomi.github.io_old/"
    args = {'obj': targeturl}
    return render(request, 'autopost/autopost_result.html', args)

def autopost_crawl_test(request, id):
    autopost = get_object_or_404(Autopost, id=id)
    data = testautocrawl(autopost.siteurl,autopost.posturl, autopost.selection, autopost.gettag)
    context = {
        'data': data,
        'autopost': autopost,
    }
    return render(request, 'autopost/autopost_crawl_test.html', context)
def autopost_crawl(request, id):
    autopost = get_object_or_404(Autopost, id=id)
    data = autocrawl(autopost.posturl, autopost.selection, autopost.gettag)
    context = {
        'data': data,
        'autopost': autopost,
    }
    return render(request, 'autopost/autopost_crawl.html', context)

def autopost_list(request):
    obj=Autopost.objects.all()
    args = {'obj': obj}
    return render(request, 'autopost/autopost_list.html', args)

def autopost_detail(request, id):
    autopost = get_object_or_404(Autopost, id=id)
    form = AutopostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.id = request.id
            form.instance.autopost = autopost
            form.save()
            return redirect(reverse("autopost/autopost_detail.html", kwargs={
                'id': id
            }))
    context = {
        'form': form,
        'autopost': autopost,
    }
    return render(request, 'autopost/autopost_detail.html', context)

def autopost_create(request):
    title="Auto Post URL Create"
    form = AutopostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            obj=Autopost.objects.all()
            args = {'obj': obj}
            return render(request, 'autopost/autopost_list.html', args)
    context = {
        'title' : title,
        'form': form
    }
    return render(request, "autopost/autopost_create.html", context)

def autopost_update(request, id):
    autopost = get_object_or_404(Autopost, id=id)
    form = AutopostForm(
        request.POST or None, 
        request.FILES or None, 
        instance=autopost)
   
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("autopost:autopost-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'form': form
    }
    return render(request, "autopost/autopost_update.html", context)

def autopost_delete(request, id):
    autopost = get_object_or_404(Autopost, id=id)
    autopost.delete()
    return redirect(reverse("autopost:autopost-list"))

