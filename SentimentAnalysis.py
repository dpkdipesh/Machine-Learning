import tweepy,sys,csv
from textblob import TextBlob
import matplotlib.pyplot as plt

    
    
consumerKey = 'NZqIz0XtOzNPo7u3M702eJx3u'
consumerSecret = 'OtBFN0byJUIvcs03ynWhV6gzZk6mRyXaGzXUEW6fu3W1KkZwXf'
accessToken = '1082232245560037377-KbvnDjIVfd7uyE0Eqiz6hRR1f2udrQ'
accessTokenSecret = 'Eg4ROmC0dg2vYEYaZ2maBLdyAaQGD9x75mcSwFEV0PuKB'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


def percentage(count,total_count):
    return 100* float(count)/float(total_count)
        
# input for term to be searched and how many tweets to search
searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))
        
# searching for tweets
tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)

positive=0
negative=0
neutral=0
polarity=0


for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity+=analysis.sentiment.polarity

    if(analysis.sentiment.polarity==0.00):
        neutral+=1
    if(analysis.sentiment.polarity<0.00):
        negative+=1
    if(analysis.sentiment.polarity>0.00):
        positive+=1
    

neutral_per=percentage(neutral,NoOfTerms)
negative_per=percentage(negative,NoOfTerms)
positive_per=percentage(positive,NoOfTerms)
polarity_per=percentage(polarity,NoOfTerms)

neutral=format(neutral_per,'.2f')
negative=format(negative_per,'.2f')
positive=format(positive_per,'.2f')



if (polarity==0.00):
    print('Neutral')
elif(polarity<0.00):
    print('Negative')
elif(polarity>0.00):
    print('Positive')

labels=['Positive['+str(positive)+'%]', 'Neutral[' +str(neutral)+ '%]', 'Negative[' +str(negative)+ '%]']
sizes=[positive,neutral,negative]
colour=['yellowgreen','yellow','red']
patches,texts=plt.pie(sizes,colors=colour,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title("How people are reacting on #"+ searchTerm +   " by analysing " + str(NoOfTerms)+ " tweets." )

plt.axis('equal')
plt.tight_layout()
plt.show()
    

    
