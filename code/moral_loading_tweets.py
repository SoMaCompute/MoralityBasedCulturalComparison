import pandas as pd

def load_mfd_dict(dict_filename):
    '''
    This function loads the given MFT dictionary
    '''
    dictref = {'01': 'HarmVirtue', '02': 'HarmVice', '03':'FairnessVirtue', '04':'FairnessVice', '05':'IngroupVirtue',
               '06':'IngroupVice', '07':'AuthorityVirtue', '08': 'AuthorityVice', '09': 'PurityVirtue', '10':'PurityVice', 
               '11':'MoralityGeneral'}


    MFTDict = {k: [] for k in dictref.keys()}

    f = open(dict_filename,'r',encoding="utf8")
    lines = f.readlines()[14:]    

    for line in lines:
        splitLine = re.split(r'\t+', line)
        splitLine = list(map(lambda s: s.strip(), splitLine))
        word = splitLine[0]

        for val in splitLine[1:]:  
            try:
                MFTDict[val].append(word)
            except KeyError:
                continue   
    return MFTDict

eng_MFTDict=load_mfd_dict('../dataset/eng_mfd.dic')
jp_MFTDict=load_mfd_dict('../dataset/jp_mfd.dic')

def compute_moral_loadings_tweets(tweets,MFTDict):
    '''
    This function compute moral loading of all tweets 
    with respect to five moral foundations 
    using the given dictionary
    '''
    mft_keys=list(MFTDict.keys())
    num_tweets=len(tweets)
    score_mat=np.zeros((num_tweets,5))
    searching_exactwords=[]
    searching_asteriks_combined=[]
    for j in range(0,10,2):
        searching_words=MFTDict[mft_keys[j]]+MFTDict[mft_keys[j+1]]
        searching_asteriks=[word[:-1] for word in searching_words if word[-1]=='*']
        searching_exactwords.append([word for word in searching_words if word[-1]!='*'])
        searching_asteriks_combined.append( "(" + ")|(".join(searching_asteriks) + ")") 
    for i in range(num_tweets):
        tweet_class_prop=[0 for j in range(5)]
        tweet=tweets[i]
        tokens=tweet.split()
        for j in range(5):
            for k in range(len(tokens)):
                if tokens[k] in searching_exactwords[j]:
                    tweet_class_prop[j]+=1
                elif re.match(searching_asteriks_combined[j],tokens[k]):
                    tweet_class_prop[j]+=1

       
        num_words=len(tokens) 
        score_mat[i]=np.array(tweet_class_prop)/num_words
    return score_mat


#************************English*******************************

#Loading English tweets dataset
data=pd.read_csv('eng_tweets.csv')
#Extracting tweets
tweets=list(df['cleaned_text'].values)
#Loading MFD
eng_MFTDict=load_mfd_dict('eng_mfd.dic')
#Compute moral loadings of English tweets
eng_loadings=compute_moral_loading(tweets,eng_MFTDict)


#************************Japanese*******************************

#Loading Japanese tweets dataset
data=pd.read_csv('jp_tweets.csv')
#Extracting tweets
tweets=list(df['cleaned_text'].values)
#Loading MFD
jp_MFTDict=load_mfd_dict('jp_mfd.dic')
#Compute moral loadings of Japanese tweets
jp_loadings=compute_moral_loading(tweets,jp_MFTDict)