from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from pages.models import ContactDetail, Subscriber
from account.models import User, UserSettings
from datetime import datetime
from blog.models import PostCategory, Post
from blog.forms import AddCategoryForm
from django.db.models import Count

# ! Staffs
@login_required
def staffs(request, slug):
   if not request.user.is_superuser:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      staffs = User.objects.filter(is_staff=True).exclude(is_superuser=True)
      context = {
         'staffs': staffs
      }
      return render(request, 'pen_admin/staffs.html', context)

@login_required
def staff_single(request, slug, username):
   if not request.user.is_superuser:
      messages.warning(request, 'You are not authorized to access that page')      
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:
      staff = User.objects.filter(is_staff=True).get(username=username)
      context = {
         'staff': staff
      }
      return render(request, 'pen_admin/single_staff.html', context)

@login_required
def block_staff(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      staff = User.objects.get(username=username)      
      staff.is_active = False
      staff.save()
      messages.success(request, f"Staff {staff.username} blocked!")
      return redirect('users:staffs', slug=slug)

@login_required
def unblock_staff(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      staff = User.objects.get(username=username)      
      staff.is_active = True
      staff.save()
      messages.success(request, f"Staff {staff.username} unblocked!")
      return redirect('users:staffs', slug=slug)
      
@login_required
def revoke_staff_access(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      staff = User.objects.get(username=username)      
      staff.is_staff = False
      staff.save()
      messages.success(request, f"Staff {staff.username} access revoked!")
      return redirect('users:staffs', slug=slug)


# ! Authors
@login_required
def authors(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:            
      authors = User.objects.filter(is_author=True).exclude(is_staff=True).annotate(posts_count=Count('post')).order_by('-date_joined')
      # categories = PostCategory.objects.annotate(posts_count=Count('post')).all().order_by('name')   
      reader_requests = User.objects.filter(usersettings__request_author_access=True)
      context = {
         'authors': authors,
         'reader_requests': reader_requests
      }
      return render(request, 'pen_admin/authors.html', context)

@login_required
def author_single(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')      
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:
      try:
         author = User.objects.filter(is_author=True).get(username=username)
         author_posts = Post.objects.filter(post_author=author)
      except User.DoesNotExist:
         return redirect('error_page')      
      context = {
         'author': author,
         'author_posts': author_posts
      }
      return render(request, 'pen_admin/single_author.html', context)

@login_required
def verify_author(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      author = User.objects.get(username=username)            
      author_settings = UserSettings.objects.get(user__username=username)
      author_settings.is_verified = True
      author_settings.save()
      messages.success(request, f"Author {author.username} verified!")
      return redirect('users:authors', slug=slug)

@login_required
def un_verify_author(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      author = User.objects.get(username=username)            
      author_settings = UserSettings.objects.get(user__username=username)
      author_settings.is_verified = False
      author_settings.save()
      messages.success(request, f"Author {author.username} unverified!")
      return redirect('users:authors', slug=slug)

@login_required
def block_author(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      author = User.objects.get(username=username)      
      author.is_active = False
      author.save()
      messages.success(request, f"Author {author.username} blocked!")
      return redirect('users:authors', slug=slug)

@login_required
def unblock_author(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      author = User.objects.get(username=username)      
      author.is_active = True
      author.save()
      messages.success(request, f"Author {author.username} unblocked!")
      return redirect('users:authors', slug=slug)

@login_required
def accept_author_access(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))   
   else:     
      reader_request = UserSettings.objects.get(user__username=username)
      user = User.objects.get(username=username)
      if reader_request.user.is_author:
         messages.warning(request, f'Reader {reader_request.user.username} is already an author!')
         return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/')) 
      else:         
         reader_request.request_author_access = False
         reader_request.requested_date = None
         user.is_author = True
         reader_request.accepted_date = datetime.now()
         reader_request.save()
         user.save()
         messages.success(request, f"Reader {reader_request.user.username} author access Accepted!")
         return redirect('users:authors', slug=slug)

@login_required
def reject_author_access(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      reader_request = UserSettings.objects.get(user__username=username)
      reader_request.request_author_access = False
      reader_request.requested_date = None
      reader_request.save()
      messages.success(request, f"Reader {reader_request.user.username} author access Rejected!")
      return redirect('users:authors', slug=slug)

# ! Readers
@login_required
def readers(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      readers = User.objects.exclude(is_author=True).order_by('date_joined')
   
      context = {
         'readers': readers
      }
      return render(request, 'pen_admin/readers.html', context)
      
@login_required
def reader_single(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:   
      reader = User.objects.filter(is_author=False).get(username=username)      
      context = {
         'reader': reader         
      }
      return render(request, 'pen_admin/single_reader.html', context)

@login_required
def block_reader(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      reader = User.objects.get(username=username)      
      reader.is_active = False
      reader.save()
      messages.success(request, f"Reader {reader.username} blocked!")
      return redirect('users:readers', slug=slug)

@login_required
def unblock_reader(request, slug, username):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      reader = User.objects.get(username=username)      
      reader.is_active = True
      reader.save()
      messages.success(request, f"Reader {reader.username} unblocked!")
      return redirect('users:readers', slug=slug)

# ! Subscribers
@login_required
def subscribers(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      subscribers = Subscriber.objects.all().order_by('-date_subscribed')
      context = {
         'subscribers': subscribers
      }
      return render(request, 'pen_admin/subscribers.html', context)

@login_required
def delete_subscriber(request, slug, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      subscriber = Subscriber.objects.get(id=id)
      subscriber.delete()
      messages.success(request, 'Subscriber deleted!')
      return redirect('users:subscribers', slug=slug)

# ! Enquiries
@login_required
def enquiries(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      enquiries = ContactDetail.objects.all()
      context = {
         'enquiries': enquiries
      }
      return render(request, 'pen_admin/enquiries.html', context)

@login_required
def single_enquiry(request, slug, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      enquiry = ContactDetail.objects.get(id=id)
      context = {
         'enquiry': enquiry
      }
      return render(request, 'pen_admin/single_enquiry.html', context)

@login_required
def delete_enquiry(request, slug, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      enquiry = ContactDetail.objects.get(id=id)
      enquiry.delete()
      messages.success(request, 'Enquiry deleted!')
      return redirect('users:enquiries', slug=slug)


# ! Categories
@login_required
def categories(request, slug):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:  
      categories = PostCategory.objects.annotate(posts_count=Count('post')).all().order_by('name')   
            
      if request.method == 'POST':
         add_category_form = AddCategoryForm(request.POST or None, request.FILES)
         if add_category_form.is_valid():
            add_category_form.save()
            messages.success(request, f'New category added')
            return redirect('users:categories', slug=slug)
         else:
            messages.error(request, 'An error occured!')
            return redirect('users:categories', slug=slug)
      else:
         add_category_form = AddCategoryForm()
      context = {
         'categories': categories,         
         'add_category_form': add_category_form
      }
      return render(request, 'pen_admin/categories.html', context)


@login_required
def edit_category(request, slug, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:  
      category = PostCategory.objects.get(id=id)
      if request.method == 'POST':
         edit_category_form = AddCategoryForm(request.POST or None, request.FILES, instance=category)
         if edit_category_form.is_valid():
            edit_category_form.save()
            messages.success(request, f'Category change successful')
            return redirect('users:categories', slug=slug)
         else:
            messages.error(request, 'An error occured!')
            return redirect('users:categories', slug=slug)
      else:
         edit_category_form = AddCategoryForm(instance=category)
      context = {
         'category': category,  
         'edit_category_form': edit_category_form
      }
      return render(request, 'pen_admin/edit_category.html', context)

@login_required
def delete_category(request, slug, id):
   if not request.user.is_staff:
      messages.warning(request, 'You are not authorized to access that page')
      return HttpResponseRedirect(request. META. get('HTTP_REFERER', '/'))
   else:      
      category = PostCategory.objects.get(id=id)
      category.delete()
      messages.success(request, 'Category deleted!')
      return redirect('users:categories', slug=slug)
