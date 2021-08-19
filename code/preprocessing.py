import pandas as pd
import re
import MeCab
from bs4 import BeautifulSoup
from html import unescape
from nltk.corpus import stopwords


def clean_eng_tweets(tweet,stopwords):
    '''
    This function is used to clean tweets written in English.
    The cleaning process includes removing urls,@mentions, etc..
    '''
    #remove urls and usernames
    tweet = re.sub(r"(?:\@|http?\://)\S+", "", tweet) 
    tweet = re.sub(r"(?:\@|https?\://)\S+", "", tweet)
    #remove escaped tags
    tweet=BeautifulSoup(unescape(tweet)).text
    #remove unwanted characters
    tweet = re.sub(r'[\',#,•,",“,.,...,;,:,=,!,@,#,$,%,^,&,*,+,/,?,_,\[, \],\\, ~,-,_,£,(,)]'," ", tweet)
    #remove characters which are not letters
    tweet= re.sub('[^A-z]', ' ', tweet)
    #remove morality and immorality keywords
    keywords=['morality','immorality']
    combined = "(" + ")|(".join(keywords) + ")"   
    tweet = re.sub(combined, '' , tweet) 
    #remove morality and immorality keywords
    keywords=['moral','immoral']
    combined = "(" + ")|(".join(keywords) + ")"   
    tweet = re.sub(combined, '' , tweet) 
    #remove trailing and leading whitespaces
    tweet.strip()
    #remove stopwords
    tweet=tweet.split()
    tweet = [word for word in tweet if word not in stopwords]
    #combining words into string
    tweet = " ".join(tweet)
    return tweet

def WordSeg(tweet):
    
    m = MeCab.Tagger()
    segmented_str = ''

    m.parse('')
    node = m.parseToNode(tweet)
    while node:
        word = node.surface
        word = re.sub('[、,。]', '', word) # remove special character
        if word != '':
            segmented_str += word + ' '
        node = node.next
    return segmented_str 

def clean_jp_tweets(tweet):
    '''
    This function is used to clean tweets written in Japanese.
    The cleaning process includes removing urls,@mentions, etc..
    '''
    #remove urls and usernames
    tweet = re.sub(r"(?:\@|http?\://)\S+", "", tweet) 
    tweet = re.sub(r"(?:\@|https?\://)\S+", "", tweet) 
    #remove escaped tags
    tweet=BeautifulSoup(unescape(tweet)).text
    #tweet = tweet.lower() # converts any english word in lower case
    tweet = re.sub(r"\W"," ",tweet) # removing any non-words characters which include special characters, comma, punctuation
    tweet = re.sub(r"\d"," ",tweet) # removing any digits
    tweet = re.sub(r"\s+",' ',tweet) # removing any extra spaces in middle 
    tweet = re.sub(r"^\s",' ',tweet) # removing any extra spaces in beginning
    tweet = re.sub(r"\s$",' ',tweet) # removing any extra spaces in end
    #remove compound_keywords relted to morality and immorality
    compound_keywords=['非道徳', '負道徳', '反道徳','不道徳','道徳の']
    combined = "(" + ")|(".join(compound_keywords) + ")"   
    tweet = re.sub(combined, '' , tweet)
    #remove keywords related to morality and immorality
    keywords=['背徳', '道徳','道義']
    combined = "(" + ")|(".join(keywords) + ")"   
    tweet = re.sub(combined, '' , tweet)   
    tweet = WordSeg(tweet).split()
    #remove stopwords 
    tweet = WordSeg(tweet).split()
    tweet=[word for word in tweet if word not in stopwords]
    tweet = " ".join(tweet)
    return tweet
 

#************************English*******************************

#Loading English tweets dataset
data=pd.read_csv('eng_tweets.csv')
#Preprocess English tweets
tweets=list(data.text.values)
eng_stopwords = stopwords.words("english")
cl_tweets=[clean_eng_tweets(tweet,eng_stopwords) for tweet in tweets]
data['cleaned_text']=cl_tweets
data.to_csv('eng_tweets.csv')


#************************Japanese*******************************

#Loading Japanese tweets dataset
data=pd.read_csv('jp_tweets.csv')
#Preprocess Japanese tweets
tweets=list(data.text.values)
jp_stopwords=["あそこ","あっ","あの","あのかた","あの人","あり","あります","ある","あれ","い","いう","います","いる","う","うち","え","お","および","おり","おります","か","かつて","から","が","き","ここ","こちら","こと","この","これ","これら","さ","さらに","し","しかし","する","ず","せ","せる","そこ","そして","その","その他","その後","それ","それぞれ","それで","た","ただし","たち","ため","たり","だ","だっ","だれ","つ","て","で","でき","できる","です","では","でも","と","という","といった","とき","ところ","として","とともに","とも","と共に","どこ","どの","な","ない","なお","なかっ","ながら","なく","なっ","など","なに","なら","なり","なる","なん","に","において","における","について","にて","によって","により","による","に対して","に対する","に関する","の","ので","のみ","は","ば","へ","ほか","ほとんど","ほど","ます","また","または","まで","も","もの","ものの","や","よう","より","ら","られ","られる","れ","れる","を","ん","何","及び","彼","彼女","我々","特に","私","私達","貴方","貴方方"]
cl_tweets=[clean_jp_tweets(tweet,jp_stopwords) for tweet in tweets]
data['cleaned_text']=cl_tweets
data.to_csv('jp_tweets.csv')   
    
