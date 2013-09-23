# coding: utf-8
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.auth.decorators import login_required

from apps.photo.models import Gallery
from apps.photo.models import Image


def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    return "text/plain"


@csrf_exempt
@login_required(login_url='/admin/')
def image_create(request, gallery_pk):

    gallery = get_object_or_404(Gallery, pk=int(gallery_pk))

    if request.method == "POST":
        f = request.FILES.get('image')

        legend = request.POST.get('legend') or gallery.title
        description = request.POST.get('description', '')

        instance = Image(
            legend=legend,
            image=f,
            gallery=gallery,
        )

        instance.save()

        data = [{'name': f.name,
                 'url': "%s" % instance.image.url,
                 "delete_url": "",
                 "delete_type": "DELETE"}]
        response = JSONResponse(data, {}, response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
    else:
        return render(request, 'fileupload/image_form.html',
                      {'gallery': gallery})


class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self, obj='', json_opts={}, mimetype="application/json",
                 *args, **kwargs):
        content = simplejson.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)
