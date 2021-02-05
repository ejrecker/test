import ast #for converting bytes to dict
import urllib.request
#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

config = {
}

def get_data(symbol):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=5min&apikey=' + config['key']
    #req = urllib.request.urlopen(url)
    with urllib.request.urlopen(url) as req:
        #data = req.read()
        #data_dict =
        return req.read()


#Google Trends
#Reddit
#API rules: https://github.com/reddit-archive/reddit/wiki/API
#https://www.reddit.com/dev/api
#personal use script: Wq4YZbhppmHphw
#secret: h1GKfd9b5rpjOg3x-FHUdCXHfGqxMA

#instructions: https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c



#
#OAUTH
#
import requests

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('<CLIENT_ID>', '<SECRET_TOKEN>')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': '<USERNAME>',
        'password': '<PASSWORD>'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.twitter.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

#
#MAKING REQUESTS
#
res = requests.get("https://oauth.reddit.com/r/python/hot",
                   headers=headers)

print(res.json())  # let's see what we get






#
#M
#

# make a request for the trending posts in /r/Python
res = requests.get("https://oauth.reddit.com/r/python/hot",
                   headers=headers)

df = pd.DataFrame()  # initialize dataframe

# loop through each post retrieved from GET request
for post in res.json()['data']['children']:
    # append relevant data to dataframe
    df = df.append({
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'selftext': post['data']['selftext'],
        'upvote_ratio': post['data']['upvote_ratio'],
        'ups': post['data']['ups'],
        'downs': post['data']['downs'],
        'score': post['data']['score']
    }, ignore_index=True)
