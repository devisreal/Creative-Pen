from blog.models import PostCategory
def categories_processor(request):
   footer_categories = PostCategory.objects.all()[:8]
   popular_categories = PostCategory.objects.all()[:5]
   context = {
      'footer_categories': footer_categories,
      'popular_categories': popular_categories
   }
   return context

