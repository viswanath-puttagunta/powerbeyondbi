import pandas as pd
import pandas as pd
import requests

dataset = pd.DataFrame(data=dataset,columns = ['id','text','language'] )

d = {'documents':[]}

for index,row in dataset.iterrows():
    d['documents'].append({'id': row[0], 'language': row[2], 'text': row[1]})

subscription_key = "Your_API_Key_Here"

sentiment_url ='https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment'

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_url, headers=headers, json=d)
sentiments = response.json()
sentiments = sentiments['documents']
sentiments = pd.DataFrame(data=sentiments)

sentiments = pd.merge(dataset, sentiments, on="id", how="inner")
