#************************English*******************************


#Loading Vader Sentiment Analyzer
import vaderSentiment
analyzer = vaderSentiment.vaderSentiment.SentimentIntensityAnalyzer()
#Loading English dataset
data=pd.read_csv('eng_tweets.csv')
#Extracting English tweets
tweets=list(dfeng.cleaned_text.values)

#Finding emotional valence along with the labels
eng_emotion_labels=[]
scores=[]
for tweet in tweets:
    
    score=analyzer.polarity_scores(tweet)['compound']
    if score>0:
        eng_emotion_labels.append(1)
    elif score<0:
        eng_emotion_labels.append(-1)
    else:
        eng_emotion_labels.append(0)
    scores.append(score)
data['emotion_lb']=eng_emotion_labels
data['escore']=score
#Saving updated English dataset
data.to_csv('eng_tweets.csv')



#************************Japanese*******************************


#Loading Oseti
import oseti
analyzer = oseti.Analyzer()
#Loading Japanese dataset
data=pd.read_csv('jp_tweets.csv')
#Extracting Japanese tweets
tweets=list(data.cleaned_text.values)

#Finding emotional valence along with the labels
jp_emotion_labels=[]
scores=[]
for tweet in tweets:
    jp_emotion_labels.append(analyzer.analyze(tweet)[0])
    scores.append(np.average(analyzer.analyze(tweet)))
data['emotion_lb']=jp_emotion_labels
data['escore']=scores
#Saving updated English dataset
data.to_csv('jp_tweets.csv')
