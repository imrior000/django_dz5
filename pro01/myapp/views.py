import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed.')
    http='''
<h1>Первая страница на Django.</h1>
<p>Это Моя первая страница на Django.</p>
'''
    return HttpResponse(http)

def about(request):
    logger.info('About page accessed.')
    http='''
<h1>О себе.</h1>
<p>Да чтор это, я, все о себе, да о себе....</p>
'''
    return HttpResponse(http)