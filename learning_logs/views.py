from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')#revers ordered
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    
    if request.method != 'POST':
        form = TopicForm()#an empty form
    else:
        form = TopicForm(request.POST)#form filled with data from the request
        
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()#an empty form
    else:
        form = EntryForm(request.POST)#form filled with data from the request
        
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, topic_id, entry_id):
    topic = Topic.objects.get(id=topic_id)
    entry = Entry.objects.get(id=entry_id)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
        form.initial['text'] = entry.text
    else:
        form = EntryForm(request.POST, instance=entry)

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)