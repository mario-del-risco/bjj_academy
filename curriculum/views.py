from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Technique, Category, Checkpoint

class TechniqueListView(ListView):
    model = Technique
    template_name = 'templates/technique_list.html'
    context_object_name = 'techniques'
    paginate_by = 10

    def get_queryset(self):
        queryset = Technique.objects.select_related('category', 'init_checkpoint', 'out_checkpoint')
        
        # Filter by category if provided
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__name=category)
        
        # Filter by belt level if provided
        belt_level = self.request.GET.get('belt_level')
        if belt_level:
            queryset = queryset.filter(belt_level=belt_level)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['belt_levels'] = Technique.objects.values_list('belt_level', flat=True).distinct()
        return context

class TechniqueDetailView(DetailView):
    model = Technique
    template_name = 'templates/technique_detail.html'
    context_object_name = 'technique'

    def get_queryset(self):
        return Technique.objects.select_related(
            'category', 
            'init_checkpoint', 
            'out_checkpoint'
        ).prefetch_related(
            'key_points', 
            'common_mistakes'
        )

def checkpoint_detail(request, pk):
    checkpoint = get_object_or_404(Checkpoint, pk=pk)
    
    # Get techniques starting from this checkpoint
    starting_techniques = Technique.objects.filter(init_checkpoint=checkpoint)
    
    # Get techniques ending at this checkpoint
    ending_techniques = Technique.objects.filter(out_checkpoint=checkpoint)
    
    context = {
        'checkpoint': checkpoint,
        'starting_techniques': starting_techniques,
        'ending_techniques': ending_techniques
    }
    
    return render(request, 'techniques/checkpoint_detail.html', context)