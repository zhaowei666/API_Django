# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import operator
import json
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QUOTES_DIR = os.path.join(BASE_DIR, 'movie/data_collection/quotes.json')



@csrf_exempt
def quotes(request):

    with open(QUOTES_DIR, 'r') as f:
        quotes_list = json.load(f)

    query = request.GET.get('query').lower().split(' ')
    #.lower.split(' ')
    query_words = [w for w in query if w]
    quote_hits = []
    print query_words
    # TODO Spelling isoform finding is required
    # TODO Hit ranking (TFIDF)
    for quote in quotes_list:
        quote_words = quote['text'].lower().split(' ')
        score = 0
        for word in query_words:
            if word in quote_words:
                score += 1
        if score:
            quote['score'] = score / len(query_words)
            quote_hits.append(quote)
    quote_hits.sort(key=operator.itemgetter('score'), reverse=True)
    print quote_hits

    return HttpResponse(json.dumps(quote_hits), status=200)