# coding=utf-8
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from forms import ContactForm


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            # cd['subject'],
            # cd['message'],
            # cd.get('email', '237434857@qq.com'),
            #     recipient_list=['237434857@qq.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I lobe your site!'}
        )
    return render_to_response('contact_form.html', {'form': form})


def contact_thanks(request):
    return render_to_response('contact_form.html')


# def object_list(request, model):
# list = model.objects.all()
# template_name = 'books/%s_list.html' % model.__name__.lower()
# return render_to_response(template_name, {'list': list})


def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404


def some_page_get(request):
    assert request.method == 'GET'
    return HttpResponseRedirect('/abb/')


def some_page_post(request):
    assert request.method == 'POST'
    return HttpResponseRedirect('/someurl/')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                                      {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

