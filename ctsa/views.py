from django.shortcuts import render
from .ctsa import TwitterClient

def index(request):
    # creating object of TwitterClient Class
    api = TwitterClient()

    ctsa_data = []
    # market name
    # positive %
    # negative %
    # neutral %

    # calling function to get tweets
    market_name = 'LME Copper'
    tweets = api.get_tweets(query=market_name, count=100)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    positive_percent = round(100 * len(ptweets) / len(tweets), 2)
    negative_percent = round(100 * len(ntweets) / len(tweets), 2)
    neutral_percent = round(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets), 2)

    market_date = {
        'market': market_name,
        'positive_percent': positive_percent,
        'negative_percent': negative_percent,
        'neutral_percent': neutral_percent,
    }

    ctsa_data.append(market_date)

    market_name = 'LME Aluminium'
    tweets = api.get_tweets(query=market_name, count=100)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    positive_percent = round(100 * len(ptweets) / len(tweets), 2)
    negative_percent = round(100 * len(ntweets) / len(tweets), 2)
    neutral_percent = round(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets), 2)

    market_date = {
        'market': market_name,
        'positive_percent': positive_percent,
        'negative_percent': negative_percent,
        'neutral_percent': neutral_percent,
    }

    ctsa_data.append(market_date)

    context = {'ctsa_data': ctsa_data}
    return render(request, 'ctsa/ctsa.html', context)