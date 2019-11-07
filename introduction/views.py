from django.shortcuts import render
import requests
from matplotlib import pyplot as plt

# Create your views here.
def about_me(request):
    URL = "https://codeforces.com/api/user.rating"
    PARAMS = {'handle':'Ghost0fSparta'}
    cf_ratings = requests.get(url = URL, params = PARAMS).json()
    rating = []
    contest_id = []
    if(cf_ratings['status'] == 'OK'):
        results = cf_ratings['result']
        contest_id = [d['contestId'] for d in results]
        rating = [d['newRating'] for d in results]
        plt.plot(contest_id, rating)
        plt.savefig('static/img/cf_ratings.png')
        plt.clf()
    context = {}
    return render(request, "about_me.html", context)
