from blog.models import PostCategory
from account.models import User
from django.db.models import Count
import random
def categories_processor(request):
   footer_categories = PostCategory.objects.all()[:7]   
   popular_categories = list(PostCategory.objects.annotate(posts_count=Count('post')).all())   
   random_categories = random.sample(popular_categories, 7)
   random_item = random.choice(popular_categories)
   author_requests = User.objects.filter(usersettings__request_author_access=True).count()
   context = {
      'footer_categories': footer_categories,
      'popular_categories': random_categories,
      'author_requests': author_requests,      
   }
   return context