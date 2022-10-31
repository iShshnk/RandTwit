from os import access
import tweepy
import openai
import random

class twitterbot():
    api_key = "JJ61HMGdIyz6Vmw4irIoHEpW0"
    api_secret = "Vwplf1OYcy2YwoOpPEs0dNpWbEPFuT13oVTT3Ij9MmEe4XUCVo"
    access_key = "1586563005088530433-8ymjkSmAnguZ99C83Q0IplFWRpfFZr"
    access_key_secret = "TQSff2CkRasGCs1IMhCHJHdK0ca5Yy8qeWIlieEzzhPgl"
    openai_key = "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"

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token (access_key, access_key_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    openai.api_key = openai_key

    '''
    response = openai.Completion.create(engine= "text-davinci-001", prompt="tweet about killing kim jong-un", max_tokens=200)
    text = response.choices[0].text
    print(text)
    api.update_status(text) 
    '''
    prompts = [       {
                "hashtag": "#elonmusk",
                "text": "tweet something cool about elon musk aquiring twitter"
            },
            {
                "hashtag": "#quote",
                "text": "tweet a motivational quote"
            },
            {
                "hashtag": "#ai",
                "text": "tweet latest developments in artificial intelligence"
            },

            {
                "hashtag": "#startup",
                "text": "tweet about startups in India "
            }
    ]


    def __init__(self):
            error = 1
            while(error == 1):
                tweet = self.create_tweet()
                try:
                    error = 0
                    self.api.update_status(tweet)
                except:
                    error = 1
        
    def create_tweet(self):
            chosen_prompt = random.choice(self.prompts)
            text = chosen_prompt["text"]
            hashtags = chosen_prompt["hashtag"]

            response = openai.Completion.create(
                engine="text-davinci-001",
                prompt=text,
                max_tokens=200,
            )

            tweet = response.choices[0].text
            tweet = tweet + " " + hashtags
            return tweet

twitter = twitterbot()
twitter.create_tweet()
