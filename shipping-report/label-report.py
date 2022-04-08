
import requests
import shopify
import math
import re



# Store credentials

access_token = "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"

shop_url = 'nf-t-his.myshopify.com'
API_key = '13489aba6b8cb90de345d24f678f0d06'
API_secret = 'a34b2c3e1a98f85b91dd925dd92738cc'
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
            
            

