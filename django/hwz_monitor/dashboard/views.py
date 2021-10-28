from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User,Topic,Post
from .forms import PostForm

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    postForm = PostForm()
    context = {'post_list': post_list, \
        'form': postForm}
    #return HttpResponse("Hello, world.")
    return render(request, 'show_post.html', context)

def uploadPost(request):
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = PostForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
