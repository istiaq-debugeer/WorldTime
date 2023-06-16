from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from website.models import Category,FlashNews,Slider,Card,BreakingNews,video

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['menus']=Category.objects.filter(is_menu=True,is_active=True)
        context['flashes']=FlashNews.objects.last()
        context['sliders']=Slider.objects.all()
        context['cards']=Card.objects.all()
        context['breakingnews']=BreakingNews.objects.all()
        context['videos']=video.objects.all()
        # context['articles']=Article.objects.filter(is_draft=False)

        return context
class ArticleDetailView(View):
        def get(self,request,article_id):
            article=BreakingNews.objects.get(id=article_id)
            context={
                'article':article
            }
            return render(request,'article-details.html',context=context)

