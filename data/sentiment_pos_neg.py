exec(open("../projectX/topics.py").read(), globals())
from textblob import TextBlob
from nltk.tokenize import sent_tokenize, word_tokenize 
import pickle
import pandas as pd 

fileObject = open("preprocessing_",'r')  
df_tablet = pickle.load(fileObject)  

df_sentiment = pd.DataFrame(columns=['pos topic', 'neg topic']) 

def sentiment_pos_neg():
    for i in range(0, 1257):
        sentences = sent_tokenize(df_tablet['review'][i])

        display = []
        sound = []
        os = []
        security = []
        hardware = []
        battery = []
        bug = []
        price = []
        cs = []
        wifi = []
        accesory = []
        app = []
        compatible = []
        usable = []
        duplicate_list = []

        for sentence in sentences:
            if (any(word in word_tokenize(sentence) for word in topic_display) and sentence not in duplicate_list):
                display.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_sound) and sentence not in duplicate_list):
                sound.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_os) and sentence not in duplicate_list): 
                os.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_security) and sentence not in duplicate_list):
                security.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_hardware) and sentence not in duplicate_list):
                hardware.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_battery) and sentence not in duplicate_list):
                battery.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_bug) and sentence not in duplicate_list):
                bug.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_price) and sentence not in duplicate_list):
                price.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_cs) and sentence not in duplicate_list):
                cs.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_wifi) and sentence not in duplicate_list):
                wifi.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_accesory) and sentence not in duplicate_list):
                accesory.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_app) and sentence not in duplicate_list): 
                app.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_compatible) and sentence not in duplicate_list): 
                compatible.append(sentence), duplicate_list.append(sentence)
            if (any(word in word_tokenize(sentence) for word in topic_usable) and sentence not in duplicate_list):
                usable.append(sentence), duplicate_list.append(sentence)

        pos_topic = 0
        neg_topic = 0

        if TextBlob(" ".join(display)).sentiment[0] >= 0.2: pos_topic += 1
        elif TextBlob(" ".join(display)).sentiment[0] <= -0.2: neg_topic +=1
        if TextBlob(" ".join(sound)).sentiment[0] >= 0.2: pos_topic +=1 
        elif TextBlob(" ".join(sound)).sentiment[0] <= -0.2: neg_topic +=1
        if TextBlob(" ".join(os)).sentiment[0] >= 0.2: pos_topic +=1
        elif TextBlob(" ".join(os)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(security)).sentiment[0]>= 0.2: pos_topic +=1
        elif TextBlob(" ".join(security)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(hardware)).sentiment[0] >= 0.2: pos_topic +=1
        elif TextBlob(" ".join(hardware)).sentiment[0] <= -0.2: neg_topic +=1
        if TextBlob(" ".join(battery)).sentiment[0] >= 0.2: pos_topic +=1
        elif TextBlob(" ".join(battery)).sentiment[0] <= -0.2: neg_topic +=1
        if TextBlob(" ".join(bug)).sentiment[0]>= 0.2: pos_topic +=1
        elif TextBlob(" ".join(bug)).sentiment[0] <= -0.2: neg_topic +=1
        if TextBlob(" ".join(price)).sentiment[0] >= 0.2: pos_topic +=1
        elif TextBlob(" ".join(price)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(cs)).sentiment[0]>= 0.2: pos_topic +=1
        elif TextBlob(" ".join(cs)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(wifi)).sentiment[0] >= 0.2: pos_topic +=1
        elif TextBlob(" ".join(wifi)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(accesory)).sentiment[0] >= 0.2: pos_topic +=1
        elif TextBlob(" ".join(accesory)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(app)).sentiment[0]>= 0.2: pos_topic +=1
        elif TextBlob(" ".join(app)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(compatible)).sentiment[0] >= 0.2: pos_topic +=1
        elif TextBlob(" ".join(compatible)).sentiment[0]<= -0.2: neg_topic +=1
        if TextBlob(" ".join(usable)).sentiment[0]>= 0.2: pos_topic +=1
        elif TextBlob(" ".join(usable)).sentiment[0]<= -0.2: neg_topic +=1

        df_sentiment.loc[len(df_sentiment)] = [pos_topic, neg_topic]