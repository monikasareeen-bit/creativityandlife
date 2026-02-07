from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Video, OnlineClass, Enquiry
from django.contrib import messages

def home(request):
    categories = Category.objects.all()
    context = {
        'site_name': 'Creativity and Life',
        'categories': categories,
        'assurance_message': 'You are at the right place to explore your creativity!'
    }
    return render(request, 'content/home.html', context)

def category_videos(request, slug):
    category = get_object_or_404(Category, slug=slug)
    videos = Video.objects.filter(category=category)
    context = {
        'category': category,
        'videos': videos,
    }
    return render(request, 'content/category_videos.html', context)

def online_classes(request):
    classes = OnlineClass.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'classes': classes,
        'categories': categories,
    }
    return render(request, 'content/online_classes.html', context)

def enquiry_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        class_id = request.POST.get('interested_class')
        message_text = request.POST.get('message')
        
        enquiry = Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            interested_class_id=class_id if class_id else None,
            message=message_text
        )
    
        messages.success(request, 'Your enquiry has been submitted successfully!')
        return redirect('enquiry_form')
    
    classes = OnlineClass.objects.filter(is_available=True)
    context = {'classes': classes}
    return render(request, 'content/enquiry_form.html', context)
def about_us(request):
    return render(request, 'content/about_us.html')

def contact_us(request):
    return render(request, 'content/contact_us.html')