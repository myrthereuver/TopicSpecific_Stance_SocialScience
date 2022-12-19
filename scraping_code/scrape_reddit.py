import praw 
from pushshift_py import PushshiftAPI
import pandas as pd
import requests
import json

# Get access to the Reddit API by following the steps described in https://medium.com/information-expositions/reddit-api-3f9b67c38f19
# Fill in your information below 

r = praw.Reddit(client_id = "", 
                client_secret = "", 
                redirect_uri = "", 
                user_agent = "", 
                
                username = "", 
                password = "")


api = PushshiftAPI(r)
type(r)


"""

keywords = ["climate change", "climate goals ","climate activists", "climate top", "climate target", "climate crisis", 
            "climate crises ", "climate protesters", "sustainable", "sustainability", "carbon emissions", "co2 emissions",
            "green energy", "green shift ", "green energy", "global warming", "global temperature", "circular economy", 
            "recycling", "recycle", "recyclables", "recyclable", "e-waste", "waste disposal", "landfills", "landfilling", 
            "landfill", "carbon neutrality", "carbon neutral", "biodiversity", "biodiversity conservation", 
            "biodiversity loss", "deforestation", "desertification", "renewable energy", "ecology threats", 
            "ecology protection", "ecology-friendly"]

subreddits = ["europe", "europeanunion", "europes"]

"""

keywords = ['climate change']
subreddits = ['europe']




# ====================================================================================
# ================================== POSTS ===========================================
# ====================================================================================

posts_df = pd.DataFrame(columns = ["id", "subreddit", "title", "num_comments", 
                                   "upvote_ratio", "created_utc", "link_flair_text",  
                                   "num_crossposts", "selftext", 
                                   "all_awardings",  "total_awards_recieved", 
                                   "full_link", "score"])

def get_pushshift_data(sub, keyword, before, after):
    """
    
    """
    url = "https://api.pushshift.io/reddit/submission/search/?q="+str(keyword)+"&subreddit="+str(sub)+"&before="+str(before)+"&after="+str(after)+"&sort=asc&limit=1000000000000000"
    # print(url)
    r = requests.get(url)
    try:
        data = json.loads(r.text, strict=False)
        full_data = data['data']
    except: 
       full_data = None
    
    return full_data


#post_data = get_pushshift_data(sub = 'europe', keyword = 'climate change', before = "0d", after = "365d")


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
    
# cleaned_dict = clean_dict(post_data)

data = []

for sub in subreddits: 
    print("=============================================")
    print(f"================= /r/{sub} =================")
    print("=============================================")
    print()
    for keyword in keywords: 
        #post_data = get_pushshift_data(sub = sub, keyword = keyword, time = '365d')
        post_data = get_pushshift_data(sub = sub, keyword = keyword, before = "0d", after = "1825d")
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

posts_df = pd.read_csv("data/post_data.csv", index_col = 0)


comment_df = pd.DataFrame()
 
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
        parent_ids = []
        comment_ids = []
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            sub_comment.append(comment.body)
            comment_ids.append(comment.id)
            parent_ids.append(comment.parent_id)
            
            #print(sub_id)
            #print(comment.body)
            #print(comment.id)
            #print(comment.parent_id)
            #print()
            
        comment_dict[sub_id] = [sub_comment, parent_ids, comment_ids]
    return comment_dict

    
post_ids = posts_df['post_id'].tolist()
comment_dict = get_comment_dict(post_ids)


def create_comment_df(comments):
    id_post = []
    coms = []
    comment_id = []
    parent_id = []
    
    for pid, cmnts in comments.items(): 
        body = cmnts[0]
        parent = cmnts[1]
        comid = cmnts[2]
        
        for b in body: 
            coms.append(b)
            id_post.append(pid)
            
        for p in parent: 
            parent_id.append(p)
            
        for c in comid: 
            comment_id.append(c)
            
        #indeces = []
        # Create unique comment ids 

        # Take the index of the comment 
        # com_count = str(ent[0])
        # And concatenate it to the post_id 
        #com_id = str(pid) + "-" + com_count
        #comment_id.append(com_id)
    
        #comment_id.append(cmnts[2])
        #id_post.append(pid)
        #coms.append(cmnts[0])
        #parent_id.append(cmnts[1])
    

    return id_post, coms, comment_id, parent_id

id_post, coms, comment_id, parent_id = create_comment_df(comment_dict)

comment_df["post_id"] = id_post
comment_df["comment_id"] = comment_id
comment_df["parent_id"] = parent_id
comment_df["comment_body"] = coms



# ===================================================================================
# ============================= PREPROCESSING =======================================
# ===================================================================================

# --------------------------------- STEP 1 ----------------------------------
# Retrieve post information (subreddit and title) for each comment
# ---------------------------------------------------------------------------

# Extract post_ids from comments Dataframe
ids_per_comment = comment_df["post_id"].tolist()

# Create new Dataframe with the information we want to add to the comments Dataframe
extract_this = pd.DataFrame()
extract_this["post_id"] = posts_df["post_id"]
extract_this["subreddit"] = posts_df["subreddit"]
extract_this["title"] = posts_df["title"]

# Transpose the Dataframe and turn it into a lookup dictionary
lookup = extract_this.set_index('post_id').T.to_dict()

# Now look up the information 
subs = []
titles = []

# For the post id that each comment belongs to... 
for i in ids_per_comment: 
    # ... find the corresponding subreddit in the lookup dict
    sub = lookup[i]['subreddit']
    subs.append(sub)
    
    # ... and find the corresponding title in the lookup dict
    title = lookup[i]['title']
    titles.append(title)
    
# Add the info to the comments Dataframe 
comment_df["subreddit"] = subs
comment_df["post_title"] = titles



# --------------------------------- STEP 2 ----------------------------------
# Remove bots and deleted comments 
# Inspired by https://github.com/spaidataiga/RedditPoliticalBias/tree/main/python/Dataset%20Creation
# ---------------------------------------------------------------------------

# Drop columns with NaN as body text
comment_df = comment_df.dropna(subset=['comment_body'])

# Remove deleted/removed posts
comment_df = comment_df[~comment_df['comment_body'].str.contains("removed", na=False)]
comment_df = comment_df[~comment_df['comment_body'].str.contains(r"deleted", na=False)]
# Remove posts by bots 
comment_df = comment_df[~comment_df['comment_body'].str.contains(r"I'?( a)?m a bot")] 


# --------------------------------- STEP 3 ----------------------------------
# Remove duplicates
# ---------------------------------------------------------------------------
posts_df = posts_df.drop_duplicates(subset = ["post_id"])


# Save new comment Dataframe
comment_df.to_csv("data/comment_data.csv") 
posts_df.to_csv("data/post_data.csv")
