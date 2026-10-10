from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from wagtail.models import Page


def search(request):
    search_query = request.GET.get("query", "").strip()
    page_number = request.GET.get("page", 1)

    if search_query:
        search_results = Page.objects.live().public().search(search_query)
    else:
        search_results = Page.objects.none()

    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page_number)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(
        request,
        "flavissima/search.html",
        {"search_query": search_query, "search_results": search_results},
    )
