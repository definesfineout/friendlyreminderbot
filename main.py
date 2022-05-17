# Task: Open reminders.txt, which contains a list of reminders, and tweet a random one out.
import random
import tweepy

with open('reminders.txt', encoding="utf8") as f: lines = f.readlines()

# Select a random line from the reminders file.
line = lines[random.randint(0, len(lines) - 1)]
print(line.strip())

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Create Tweet

# The app and the corresponding credentials must have the Write permission

# Check the App permissions section of the Settings tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps

# Make sure to reauthorize your app / regenerate your access token and secret 
# after setting the Write permission

response = client.create_tweet(
    text=line.strip()
)
print(f"https://twitter.com/user/status/{response.data['id']}")