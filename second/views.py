from django.shortcuts import render, redirect
from second.forms import ThisISForm
from django.views import View
from second.models import Profile


class create(View):

    def get(self, request):

        form = ThisISForm()
        return render(request, 'dit/create.html', {'form':form})

    def post(self, request):

        form = ThisISForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'dit/create.html', {'form': form})


class index(View):

    def get(self, request):

        data = Profile.objects.all()
        return render(request, 'dit/index.html', {'data':data})


class update(View):

    def get(self, request, pk):

        data = Profile.objects.get(pk=pk)
        form = ThisISForm(instance=data)
        return render(request, 'dit/update.html', {'form': form})

    def post(self, request, pk):
        data = Profile.objects.get(pk=pk)
        form = ThisISForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'dit/update.html', {'form': form})


class delete(View):

    def get(self, request, pk):

        data = Profile.objects.get(pk=pk)
        data.delete()
        return redirect('index')

class view(View):

    def get(self, request, pk):

        data = Profile.objects.get(pk=pk)
        return render(request, 'dit/view.html', {'data':data})