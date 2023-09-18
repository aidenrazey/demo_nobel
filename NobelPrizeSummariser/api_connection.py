import pandas as pd


class NobelApiConnection:
    api_uri: str

    def __init__(self, api_uri: str):
        self.api_uri = api_uri

    def read_data(self) -> pd.DataFrame:
        import requests
        #parameters to return all datapoints
        params = {
            "nobelPrizeYear": 'min',  # Replace with your desired start year
            "yearTo": 'max',  # Replace with your desired end year
            "limit": 999999
        }
        response = requests.get(self.api_uri, params=params)
        #check for OK request
        if response.status_code == 200:
            data = response.json()
            #isolate nested data
            df = pd.DataFrame(data['nobelPrizes'])
            #only use necessary columns
            df = df[['awardYear', 'category', 'prizeAmountAdjusted']]

            #function to pull english version of prize category
            def extract_en_value(dictionary):
                return dictionary.get('en')

            df['category'] = df['category'].apply(extract_en_value)
            df['awardYear'] = df['awardYear'].astype('int')
            return df

        #if request not OK, return status code for troubleshooting
        else:
            print(f'Failed to retrieve data. Error Status Code is: {response.status_code}')
            return None
