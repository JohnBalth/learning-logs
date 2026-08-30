from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import models

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Página principal."""

    return render(
        request,
        "learning_logs/index.html"
    )


@login_required
def topics(request):
    """Mostra os tópicos do usuário e permite pesquisar."""

    query = request.GET.get('q', '').strip()

    topics = Topic.objects.filter(
        owner=request.user
    ).order_by('date_added')

    entry_count = 0

    if query:

        topics = topics.filter(
            models.Q(text__icontains=query) |
            models.Q(entry__text__icontains=query)
        ).distinct()

        for topic in topics:

            topic.search_entries = topic.entry_set.filter(
                text__icontains=query
            ).order_by('-date_added')

            entry_count += topic.search_entries.count()

    else:

        for topic in topics:
            topic.search_entries = []

    context = {
        'topics': topics,
        'query': query,
        'result_count': topics.count(),
        'entry_count': entry_count,
    }

    return render(
        request,
        "learning_logs/topics.html",
        context
    )


@login_required
def topic(request, topic_id):
    """Mostra um único tópico e suas anotações."""

    topic = get_object_or_404(
        Topic,
        id=topic_id,
        owner=request.user
    )

    entries = topic.entry_set.order_by('-date_added')

    context = {
        'topic': topic,
        'entries': entries,
    }

    return render(
        request,
        "learning_logs/topic.html",
        context
    )


@login_required
def new_topic(request):
    """Adiciona um novo tópico."""

    if request.method != 'POST':

        form = TopicForm()

    else:

        form = TopicForm(
            data=request.POST
        )

        if form.is_valid():

            new_topic = form.save(
                commit=False
            )

            new_topic.owner = request.user

            new_topic.save()

            return redirect(
                'learning_logs:topics'
            )

    context = {
        'form': form
    }

    return render(
        request,
        "learning_logs/new_topic.html",
        context
    )


@login_required
def edit_topic(request, topic_id):
    """Edita o título de um tópico."""

    topic = get_object_or_404(
        Topic,
        id=topic_id,
        owner=request.user
    )

    if request.method != 'POST':

        form = TopicForm(
            instance=topic
        )

    else:

        form = TopicForm(
            instance=topic,
            data=request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'learning_logs:topics'
            )

    context = {
        'topic': topic,
        'form': form
    }

    return render(
        request,
        "learning_logs/edit_topic.html",
        context
    )


@login_required
def delete_topic(request, topic_id):
    """Exclui um tópico."""

    topic = get_object_or_404(
        Topic,
        id=topic_id,
        owner=request.user
    )

    if request.method == 'POST':

        topic.delete()

        return redirect(
            'learning_logs:topics'
        )

    context = {
        'topic': topic
    }

    return render(
        request,
        "learning_logs/delete_topic.html",
        context
    )


@login_required
def new_entry(request, topic_id):
    """Adiciona uma nova anotação dentro de um tópico."""

    topic = get_object_or_404(
        Topic,
        id=topic_id,
        owner=request.user
    )

    if request.method != 'POST':

        form = EntryForm()

    else:

        form = EntryForm(
            data=request.POST
        )

        if form.is_valid():

            new_entry = form.save(
                commit=False
            )

            new_entry.topic = topic

            new_entry.save()

            return redirect(
                'learning_logs:topic',
                topic_id=topic.id
            )

    context = {
        'topic': topic,
        'form': form
    }

    return render(
        request,
        "learning_logs/new_entry.html",
        context
    )


@login_required
def edit_entry(request, entry_id):
    """Edita uma anotação existente."""

    entry = get_object_or_404(
        Entry,
        id=entry_id,
        topic__owner=request.user
    )

    topic = entry.topic

    if request.method != 'POST':

        form = EntryForm(
            instance=entry
        )

    else:

        form = EntryForm(
            instance=entry,
            data=request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'learning_logs:topic',
                topic_id=topic.id
            )

    context = {
        'entry': entry,
        'topic': topic,
        'form': form
    }

    return render(
        request,
        "learning_logs/edit_entry.html",
        context
    )


@login_required
def delete_entry(request, entry_id):
    """Exclui uma anotação existente."""

    entry = get_object_or_404(
        Entry,
        id=entry_id,
        topic__owner=request.user
    )

    topic = entry.topic

    if request.method == 'POST':

        entry.delete()

        return redirect(
            'learning_logs:topic',
            topic_id=topic.id
        )

    context = {
        'entry': entry,
        'topic': topic,
    }

    return render(
        request,
        "learning_logs/delete_entry.html",
        context
    )


def register(request):
    """Registra um novo usuário."""

    if request.method != 'POST':

        form = UserCreationForm()

    else:

        form = UserCreationForm(
            data=request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Conta criada com sucesso! '
                'Agora entre com seu usuário e senha.'
            )

            return redirect('login')

    context = {
        'form': form
    }

    return render(
        request,
        'registration/register.html',
        context
    )