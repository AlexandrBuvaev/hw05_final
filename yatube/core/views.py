from django.shortcuts import render


def page_not_found(request, exception):
    template = 'core/404 page_not_found.html'
    return render(request, template, {'path': request.path}, status=404)


def csrf_failure(request, reason=''):
    template = 'core/403 permission_denied_view.html'
    return render(request, template)


def server_error(request):
    return render(request, 'core/500.html', status=500)
