import requests
import pandas as pd
response = requests.get("https://api.nobelprize.org/2.1/nobelPrizes", params={})
data = response.json()
df = pd.DataFrame(data['nobelPrizes'])
df = df[['awardYear','category','prizeAmount']]
def extract_en_value(dictionary):
    return dictionary.get('en')
df['category'] = df['category'].apply(extract_en_value)
print(df)