from django.urls import URLResolver, URLPattern
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_all_methods(request, **kwargs):
    from .urls import urlpatterns
    urls = []
    for url_obj in urlpatterns:
        if isinstance(url_obj, URLResolver):
            for url in url_obj.url_patterns:
                urls.append({str(url.name): str(url_obj.pattern) + str(url.pattern)})
        else:
            url_line = url_obj.pattern
            urls.append({url_line.name: str(url_line)})
    return Response(data=urls, status=200)
