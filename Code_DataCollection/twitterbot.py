# Author: Himarsha R. Jayanetti 
# Description: Script to collect data from X using Selenium
# Built using https://github.com/Prateek93a/selenium-twitter-bot/tree/master


from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
from seleniumwire.utils import decode as sw_decode
import brotli
import random
import zstandard
import gzip
import base64


import time, os
 
class Twitterbot:
 
    def __init__(self, email, password):
 
        """Constructor
 
        Arguments:
            email {string} -- registered twitter email
            password {string} -- password for the twitter account
        """
 
        self.email = email
        self.password = password
        # initializing chrome options
        chrome_options = Options()
        
        chrome_options.add_argument('--headless')

 
        # adding the path to the chrome driver and 
        # integrating chrome_options with the bot
        self.bot = webdriver.Chrome(
            # executable_path = os.path.join(os.getcwd(), 'chromedriver'),
            options = chrome_options,
            # service=Service
        )
 
    def login(self, hashtag):
        """
            Method for signing in the user 
            with the provided email and password.
        """
 
        bot = self.bot
        # fetches the login page
        bot.get('https://twitter.com/i/flow/login')
        # adjust the sleep time according to your internet speed
        time.sleep(10)
 
        # email = bot.find_element("xpath",'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')


        # # sends the email to the email input
        # email.send_keys(self.email)
        # # # executes RETURN key action
        # # email.send_keys(Keys.RETURN)

        # # time.sleep(10)

        # password = bot.find_element("xpath",'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]')

        # # sends the password to the password input
        # password.send_keys(self.password)
        # # executes RETURN key action
        # password.send_keys(Keys.RETURN)
        username = WebDriverWait(bot, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
        # time.sleep(10)
        username.send_keys(self.email)
        username.send_keys(Keys.ENTER)

        # time.sleep(10)
        password = WebDriverWait(bot, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

        time.sleep(2)
 
        # With time specified
        # bot.get(
        #      'https://twitter.com/search?q=%23' + \
        #      hashtag+'until%3A2024-10-27%20since%3A2024-10-21&&src=typed_query&f=live')

        bot.get(
             'https://twitter.com/search?q=%23' + \
             hashtag+'&src=typed_query&f=live')

        last_height = bot.execute_script("return document.body.scrollHeight")
        while True:

            # Scroll down to the bottom.
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load the page.
            random_number1 = random.uniform(1, 10)
            time.sleep(random_number1)
            
            # Calculate new scroll height and compare with last scroll height.
            new_height = bot.execute_script("return document.body.scrollHeight")

            if new_height == last_height:

                break

            last_height = new_height

        random_number2 = random.uniform(1, 10)
        time.sleep(random_number2)   

        content = bot.page_source
        # BellevueHill_Sydney
        # keyword = keyword.replace(" ", "")
        with open(f"{hashtag}.html","w") as f:
            f.write(content)        

        #logged in-----------------------------------------------

        # Fetching and saving SearchTimeline responses
        # graphql_responses = [req for req in bot.requests if 'api/graphql' in req.path]

        i=0
        for req in bot.requests:
            # print(req)
            # SearchTimeline?variables
            req_1 = req.path
            # print(req_1)
            # if 'SearchTimeline?variables' in req_1:  
            if 'api/graphql' in req_1:          
                # print(req, req_1)      
                # print("here1")
                compressed_Encoding = req.response.headers['Content-Encoding']
                compressed_data = req.response.body
                
                # print(compressed_Encoding)

                try:

                    if compressed_Encoding == "gzip":
                        decoded_bytes = gzip.decompress(compressed_data)
                        decoded_string = decoded_bytes.decode('utf-8')   


                    if compressed_Encoding == "zstd":
                        print("Encoding = zstd")
                        dctx = zstandard.ZstdDecompressor()
                        with dctx.stream_reader(compressed_data) as reader:
                            decoded_bytes = reader.read()
                        decoded_string = decoded_bytes.decode('utf-8')   

                    if compressed_Encoding == "brotli":
                        print("Encoding = brotli")
                        brot = brotli.decompress(compressed_data)
                        decoded_string = brot.decode('utf-8')   

                except Exception as e:
                    print("Exception")
                    try:
                        print("base64")
                        decoded_string = base64.b64decode(compressed_data)
                        # print(decoded_string)    
                    except Exception as ex:
                        print("binascii")
                        decoded_string = binascii.unhexlify(compressed_data)
                        # print(decoded_string)    
                    print(e)
                # print(req.url)
                # print(req.headers)
                # brot = brotli.decompress(req.response.body)
                # # print(brot)
                # decoded_string = brot.decode('utf-8')

                print(decoded_string)    

                if decoded_string.startswith('{"data":{"search_by_raw_query":{"search_timeline"'):  
                    print("here2")
                    with open(f"TwitterPosts/SearchTimeline/SearchTimeline_response_{i}.json", "w") as f:
                        # print(response.response.body.decode('utf-8'))
                        # json.dump(json.loads(req.response.body.decode("latin-1")), f)
                        f.write(decoded_string)
                i=i+1

