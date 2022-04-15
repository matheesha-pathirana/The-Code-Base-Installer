import json
import psycopg2
import requests
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(BASE_PATH+'/config.json') as json_data_file:
    data = json.load(json_data_file)

#api_config = data['api_data']
#redshift = data['redshift']
s3_config = data['s3']

#x = print(api_config.get('request_url'))

class ApiResponse:
    #api response
    def api_data(self, api_config):
        print("starting api_data")
        try:
            self.ApiResponse = requests.post(api_config['request_url'], api_config['post_data'], api_config['my_headers'])
            data_1 = self.ApiResponse
            #data = json.dump(self.ApiResponse)
            print("API Result Response")
            print(())
            print(self.ApiResponse)
            return (self.ApiResponse)

        except Exception:
            print("response not found")
            return False

    def redshift_connect(self, redshift):
        try:
            # Amazon Redshift connect string
            self.con = psycopg2.connect(
                host=redshift['host'],
                user=redshift['user'],
                port=redshift['port'],
                password=redshift['password'],
                dbname=redshift['db'])
            print(self.con)
            return self.con
        except Exception:
            print("Error in Redshift connection")
            return False
def main():
    c1 = ApiResponse()
    api_config = data['api_data']
    redshift = data['redshift']
    c1.api_data(api_config)
    c1.api_data(data)
    c1.redshift_connect(redshift)

if __name__=='__main__':
    main()