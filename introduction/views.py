from django.shortcuts import render
import requests
from requests.exceptions import HTTPError
from matplotlib import pyplot as plt

# Create your views here.
def about_me(request):
    URL = "https://codeforces.com/api/user.rating"
    PARAMS = {'handle':'Ghost0fSparta'}
    try:
        cf_ratings = requests.get(url = URL, params = PARAMS).json()
    except HTTPError as http_error:
        print('HTTP error occured: {http_error}')
    except Exception as err:
        print('Other Exception: {err}')
    else :
        rating = []
        contest_id = []
        if(cf_ratings['status'] == 'OK'):
            results = cf_ratings['result']
            contest_id = [d['contestId'] for d in results]
            rating = [d['newRating'] for d in results]
            contest_id, rating = zip(*sorted(zip(contest_id, rating)))
            plt.plot(contest_id, rating,marker='o',color='r')
            plt.savefig('introduction/static/img/cf_ratings.png')
            plt.clf()
    context = {}
    return render(request, "about_me.html", context)
