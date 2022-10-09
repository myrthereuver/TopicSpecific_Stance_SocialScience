
import praw 


# TO DO: 
#   praw_ini_file: https://asyncpraw.readthedocs.io/en/stable/getting_started/configuration/prawini.html#praw-ini 

r = praw.Reddit(client_id = "Cd0HX_wVbjRGDZ4Fcns-Ag", 
                client_secret = "	RvSrlKVRD1L_Er1DZZSY91iSSCO_bg", 
                redirect_uri = "https://www.reddit.com/r/europeanunion/", 
                user_agent = "malomori", 
                
                username = "malomori", 
                password = "Lieverdood86!")

type(r)


europe = r.subreddit("europe")
europeanunion = r.subreddit("europeanunion")
europes = r.subreddit("europes")


# subreddits: /r/europe, europeanunion, europes 
keywords = ["climate change", "climate goals "," climate activists", "climate top", "climate target", "climate crisis", 
            "climate crises ", "climate protesters", "sustainable", "sustainability", "carbon emissions", "co2 emissions",
            "green energy", "green shift ", "green energy", "global warming", "global temperature", "circular economy", 
            "recycling", "recycle", "recyclables", "recyclable", "e-waste", "waste disposal", "landfills", "landfilling", 
            "landfill", "carbon neutrality", "carbon neutral", "biodiversity", "biodiversity conservation", 
            "biodiversity loss", "deforestation", "desertification", "renewable energy", "ecology threats", 
            "ecology protection", "ecology-friendly"]

subreddits = ["europe", "europeanunion", "europes"]


# Obtain the comments for a single submission 

for post in europe.new(limit=100):
    print(post.title)
    print()
