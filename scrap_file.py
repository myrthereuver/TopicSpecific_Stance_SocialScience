import praw 
from pushshift_py import PushshiftAPI
import datetime
import pandas as pd
import requests
import json


# TO DO: 
#   praw_ini_file: https://asyncpraw.readthedocs.io/en/stable/getting_started/configuration/prawini.html#praw-ini 

r = praw.Reddit(client_id = "Cd0HX_wVbjRGDZ4Fcns-Ag", 
                client_secret = "RvSrlKVRD1L_Er1DZZSY91iSSCO_bg", 
                redirect_uri = "https://www.reddit.com/r/europeanunion/", 
                user_agent = "malomori", 
                
                username = "malomori", 
                password = "Lieverdood86!")


api = PushshiftAPI(r)
type(r)














# Specify time range 
start_epoch= int(datetime.datetime(2017, 1, 1).timestamp())
stop_epoch = int(datetime.datetime(2022,12,10).timestamp())


after = start_epoch 
before = stop_epoch


author_flair_text = "news"
# “filter”: Column names we want to retrieve (suggested: ‘id’, ‘author’, ‘created_utc’, ‘domain’, ‘url’, ‘title’, ‘num_comments’)

# Goal: Obtain the comments for a single submission 
gen = api.search_submissions(q='climate change', subreddit='europe')
cache = []    
for c in gen:
    cache.append(c)



    
help(api.search_submissions)

keyword = "climate change"




"""PUSHSHIFT APPROACH"""

keywords = ["climate change", "climate goals ","climate activists", "climate top", "climate target", "climate crisis", 
            "climate crises ", "climate protesters", "sustainable", "sustainability", "carbon emissions", "co2 emissions",
            "green energy", "green shift ", "green energy", "global warming", "global temperature", "circular economy", 
            "recycling", "recycle", "recyclables", "recyclable", "e-waste", "waste disposal", "landfills", "landfilling", 
            "landfill", "carbon neutrality", "carbon neutral", "biodiversity", "biodiversity conservation", 
            "biodiversity loss", "deforestation", "desertification", "renewable energy", "ecology threats", 
            "ecology protection", "ecology-friendly"]

subreddits = ["europe", "europeanunion", "europes"]


### POSTS
posts_df = pd.DataFrame()
comments_df = pd.DataFrame()


def get_pushshift_data(sub, keyword, time):
    url = "https://api.pushshift.io/reddit/search/submission/?q="+str(keyword)+"&subreddit="+str(sub)+"&after="+str(time)+"&sort=asc&limit=1000000000000000"
    print(url)
    r = requests.get(url)
    data = json.loads(r.text, strict=False)
    full_data = data['data']
    
    return full_data


post_data = get_pushshift_data(sub= 'europe', keyword = 'climate change', time = "365d")


def extract_relevant_info(post_data):
    df_per_keyword = pd.DataFrame()
    
    post_ids = []
    title = []
    body = []
    num_comments = []
    date_created = []
    permalinks = []
    subreddit = []
    award_types = []
    awards_total = []
    score = []
    upvote_ratio = []
    num_crossposts = []
    flair = []
    
    for post in post_data: 
        post_ids.append(post['id'])
        title.append(post['title'])
        #body.append(post['selftext'])
        num_comments.append(post['num_comments'])
        date_created.append(post['created_utc'])
        permalinks.append(post["permalink"])
        subreddit.append(post['subreddit'])
        #award_types.append(post['all_awardings'])
        #awards_total.append(post['total_awards_received'])
        score.append(post['score'])
        #upvote_ratio.append(post['upvote_ratio'])
        #num_crossposts.append(post['num_crossposts'])        
        
        try: 
            award_types.append(post['all_awardings'])
        except: 
            award_types.append("NA")
            
        try: 
            awards_total.append(post['total_awards_received'])
        except: 
            awards_total.append("NA")
                             
        try: 
            upvote_ratio.append(post['upvote_ratio'])
        except: 
            upvote_ratio.append("NA")
        
        try: 
            num_crossposts.append(post['num_crossposts'])
        except: 
            num_crossposts.append("NA")   
            
        try: 
            body.append(post['selftext'])
        except: 
            body.append("NA")
        
        try: 
            flair.append(post['link_flair_richtext'])
        except: 
            flair.append("NA")
            

    df_per_keyword['post_id'] = post_ids
    df_per_keyword['title'] = title
    df_per_keyword['body'] = body
    df_per_keyword['num_comments'] = num_comments
    df_per_keyword['subreddit'] = subreddit
    df_per_keyword['date_created'] = date_created    
    df_per_keyword['flair'] = flair
    df_per_keyword['upvote_ratio'] = upvote_ratio
    df_per_keyword['num_crossposts'] = num_crossposts
    df_per_keyword['permalink'] = permalinks
    df_per_keyword['awards_total'] = awards_total
    df_per_keyword['award_types'] = award_types
    df_per_keyword['score'] = score
    
    posts_df.append(df_per_keyword, ignore_index = True)
    return df_per_keyword
    
    



### COMMENTS
"""
def get_comments(data): 
    post_ids = []
    for submission in data: 
        post_id = submission["id"]
        post_ids.append(post_id)
    return post_ids

ids = get_comments(post_data)
"""

def get_comment_dict(ids):
    comment_dict = {}
    for sub_id in ids: 
        submission = r.submission(id=sub_id)
        sub_comment = []
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            sub_comment.append(comment.body)
            
        comment_dict[sub_id] = sub_comment
    return comment_dict

    

#post_ids = posts_df['post_id'].tolist()
#comment_dict = get_comment_dict(post_ids)


def scrape_reddit(sub, keyword, time="50d"): 
    # obtain pd DataFrame with post info: title, body, 
    post_data = get_pushshift_data(sub=sub, keyword=keyword, time=time)
    # clean post data
    extract_relevant_info(post_data)
    
    # extract corresponding comments
    post_ids = posts_df['post_id'].tolist()
    comment_dict = get_comment_dict(post_ids)
    
    return comment_dict
    

comments = scrape_reddit(sub = 'europe', keyword = 'climate change', time = '365d')

for pid, cmnts in comments.items(): 
    for cmnt in cmnts:
        print(pid)
        print(cmnt)
        comments_df['id'] = pid
        comments_df['comment'] = cmnt


hot_posts = r.subreddit('all').new(limit=10)
for post in hot_posts:
    print(post.title)
    


datetime.datetime(2017,10,12).timestamp()







"""REDDIT API APPROACH"""

# Get all posts with keywords in title 
posts = []
subreddit = r.subreddit('europe')
for post in subreddit.new(limit = None):
    for keyword in keywords: 
        if keyword in post.title.lower():  
            dt = datetime.datetime.utcfromtimestamp(post.created).timestamp()
            if dt > datetime.datetime(2017,10,12).timestamp():
                posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])



#print(posts)

# Get comments from a specific post
# necessary: submission ids 
submission_ids = posts['id'].tolist()


submission_dict = {}
for sub_id in submission_ids: 
    submission = r.submission(id=sub_id)
    sub_comment = []
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        sub_comment.append(comment.body)
        
    submission_dict[sub_id] = sub_comment

# TO DO: filter on time 