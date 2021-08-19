import pandas as pd

def compute_moral_loading(data):
    #The function computes the moral loadings of every user 
    #based on the given data. Here data is a dataframe containg 
    #set of morally loaded tweets and their correspondings details
    
    #Extract the userids of all unique users
    users=list(set(data['user_id'].values))
    
    #Extract number of unique users
    num_users=len(set(data['user_id'].values))
    
    #for each user compute their moral loadings based on the moral
    #labels of the tweets, where label denotes the moral dimension
    #represented in a given tweet
    
    users_ml={}
    for i in range(num_users):
        user=users[i]
        data_user=data[data['user_id']==user]
        user_ml=[]
        for dim in range(5):
            user_ml.append(data_user[data_user['label']==dim].shape[0])/(data_user['label'].shape[0])
        
        users_ml[user]=user_ml
    return users_ml
 
#************************English*******************************

#Loading English tweets dataset
data=pd.read_csv('eng_tweets.csv')
#Compute moral loadings of English users
eng_users_ml=compute_moral_loading(data)


#************************Japanese*******************************

#Loading Japanese tweets dataset
data=pd.read_csv('jp_tweets.csv')
#Compute moral loadings of Japanese users
jp_users_ml=compute_moral_loading(data)    
    
