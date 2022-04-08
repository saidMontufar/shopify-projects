
import requests
import shopify
import math
import re



# Store credentials

access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

shop_url = 'YOUR-STORE-NAME.myshopify.com'
API_key = 'xxxxxxxxxxxxxxxxxxx'
API_secret = 'xxxxxxxxxxxxxxxxxx'
API_version = '2022-01'

url = 'https://{shop_url}.myshopify.com/admin/api/{API_version}/{resource}.json'


# Activates Session
session = shopify.Session(shop_url, API_version, access_token)
shopify.ShopifyResource.activate_session(session)



# Retreives all orders
all_orders = shopify.Order.find(created_at = 'any')

# Returns list of events for label purchases

# List of cost for each label
count = list()

# Searches for events where a label was created then adds the cost of each label in a specific time frame.

def labels_total():

    for order in all_orders:
        for event in order.get('events'):
            if event['verb'] == "shipping_label_created_success":
                s = [float(s) for s in re.findall(r'-?\d+\.?\d*', event['description'])]
                count.append(s[0])
    return f'Total spent on shipping labels: ${round(sum(count),2)} CAD'

labels_total()
            
            

