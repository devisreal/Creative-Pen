from blog.models import PostCategory
def categories_processor(request):
   footer_categories = PostCategory.objects.all()[:8]
   
   context = {
      'footer_categories': footer_categories
   }
   return context

