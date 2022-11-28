import tweepy
import key

def api():
    auth = tweepy.OAuthHandler(key.api_key,key.api_secret)
    auth.set_access_token(key.access_token,key.access_token_secret)

    return tweepy.API(auth)

def tweet(api:tweepy.API,message = str):
    api.update_status(message)
    print("Done")



if __name__ == "__main__":
    api =api()
    tag = "\n \n #puns #jokes #memes"
    with open('bot/jokes.txt','r',encoding='utf8') as f:
        y = f.readline()
        data = f.read().splitlines(True)
    with open('bot/jokes.txt','w',encoding='utf8') as d:
        d.writelines(data[0:])
        x = y + tag    
    tweet(api,x)