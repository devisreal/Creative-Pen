from blog.models import PostCategory
from django.db.models import Count
import random
def categories_processor(request):
   footer_categories = PostCategory.objects.all()[:1]   
   popular_categories = list(PostCategory.objects.annotate(posts_count=Count('post')).all())
   random_categories = random.sample(popular_categories, 1)
   random_item = random.choice(popular_categories)   
   context = {
      'footer_categories': footer_categories,
      'popular_categories': random_categories
   }
   return context

