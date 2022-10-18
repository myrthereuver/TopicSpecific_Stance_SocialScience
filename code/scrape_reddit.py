import praw 
from pushshift_py import PushshiftAPI
import datetime
import pandas as pd
import requests
import json


# TO DO: 
#   praw_ini_file: https://asyncpraw.readthedocs.io/en/stable/getting_started/configuration/prawini.html#praw-ini 

r = praw.Reddit(client_id = "1rtLWKTkLHkFCnowRNiNXg", 
                client_secret = "7XbN2wa8beCO_ypWKGx9zqoqoP4vxA", 
                redirect_uri = "https://www.reddit.com/r/europeanunion/", 
                user_agent = "NLPiscool", 
                
                username = "NLPiscool", 
                password = "DistrustSustainable2022")


api = PushshiftAPI(r)
type(r)




keywords = ["climate change", "climate goals ","climate activists", "climate top", "climate target", "climate crisis", 
            "climate crises ", "climate protesters", "sustainable", "sustainability", "carbon emissions", "co2 emissions",
            "green energy", "green shift ", "green energy", "global warming", "global temperature", "circular economy", 
            "recycling", "recycle", "recyclables", "recyclable", "e-waste", "waste disposal", "landfills", "landfilling", 
            "landfill", "carbon neutrality", "carbon neutral", "biodiversity", "biodiversity conservation", 
            "biodiversity loss", "deforestation", "desertification", "renewable energy", "ecology threats", 
            "ecology protection", "ecology-friendly"]

subreddits = ["europe", "europeanunion", "europes"]

# ====================================================================================
# ================================== POSTS ===========================================
# ====================================================================================

posts_df = pd.DataFrame(columns = ["id", "subreddit", "title", "num_comments", 
                                   "upvote_ratio", "created_utc", "link_flair_text",  
                                   "num_crossposts", "selftext", 
                                   "all_awardings",  "total_awards_recieved", 
                                   "full_link", "score"])

def get_pushshift_data(sub, keyword, time):
    """
    
    
    """
    url = "https://api.pushshift.io/reddit/submission/search/?q="+str(keyword)+"&subreddit="+str(sub)+"&after="+str(time)+"&sort=asc&limit=1000000000000000"
    # print(url)
    r = requests.get(url)
    try:
        data = json.loads(r.text, strict=False)
        full_data = data['data']
    except: 
       full_data = None
    
    return full_data


post_data = get_pushshift_data(sub = 'europe', keyword = 'climate change', time = "30d")


def clean_dict(post_data): 
    to_be_kept = ["all_awardings", "created_utc", "full_link", "id", "link_flair_text", 
                  "num_comments", "num_crossposts", "selftext", "score", "subreddit", 
                  "title", "total_awards_recieved", "upvote_ratio"]
 
    for dictionary in post_data: 
        dictionary_keys = []
        for key in dictionary.keys(): 
            dictionary_keys.append(key)
        
        for k in dictionary_keys: 
            if k not in to_be_kept: 
                dictionary.pop(k)

    return post_data
    
cleaned_dict = clean_dict(post_data)

data = []

for sub in subreddits: 
    print("=============================================")
    print(f"================= /r/{sub} =================")
    print("=============================================")
    print()
    for keyword in keywords: 
        post_data = get_pushshift_data(sub = sub, keyword = keyword, time = '365d')
        if post_data != None: 
            
            cleaned_data = clean_dict(post_data)
            data.append(cleaned_data)
            print(f"retrieved {len(cleaned_data)} posts for '{keyword}' in /r/{sub}")
            print()
        else: 
            print(f"retrieved 0 posts for '{keyword}' in /r/{sub}")
            print()

for post in data: 
    for d in post: 
        posts_df = posts_df.append(d, ignore_index = True)


posts_df.rename(columns = {'id':'post_id', 'selftext':'body'}, inplace = True)

posts_df.to_csv("data/post_data.csv")

# ====================================================================================
# ================================ COMMENTS ==========================================
# ====================================================================================

comment_df = pd.DataFrame(columns = ["post_id", "comment_body"])
 
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

    
post_ids = posts_df['post_id'].tolist()
post_ids = post_ids[:25]
comment_dict = get_comment_dict(post_ids)



def create_comment_df(comments):
    id_post = []
    coms = []
    for pid, cmnts in comments.items(): 
        for cmnt in cmnts:
            id_post.append(pid)
            coms.append(cmnt)
    return id_post, coms

ids, comments = create_comment_df(comment_dict)

comment_df["post_id"] = ids
comment_df["comment_body"] = comments
        




# ===================================================================================
# ================================ SCRAP ============================================
# ===================================================================================


    
    comments_df['post_id'] = id_post
    comments_df['comment'] = coms




def scrape_reddit(sub, keyword, time): 
    # obtain pd DataFrame with post info: title, body, 
    post_data = get_pushshift_data(sub=sub, keyword=keyword, time=time)
    
    if post_data != None: 
        
        # clean post data
        # extract_relevant_info(post_data)
        keyword_dict = clean_dict(post_data)
        # posts_df = pd.concat([posts_df, keyword_df])
        
        ### Extract corresponding comments
        
        #ids_posts = posts_df['post_id'].tolist()
        #comment_dict = get_comment_dict(ids_posts)
        
        ### Create comment dataframe
        
        #create_comment_df(comment_dict)
        
        
    else: 
        print(f"--- '{keyword}' is not present in posts at /r/{sub} ---")
        print()

for sub in subreddits: 
    for keyword in keywords: 
        scrape_reddit(sub = sub, keyword = keyword, time = '365d')


