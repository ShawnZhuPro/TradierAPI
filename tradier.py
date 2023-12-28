import config, requests, json

# Send an authenticated request to the Tradier API for getting quotes
# Documentation: https://documentation.tradier.com/brokerage-api/markets/get-quotes
quote_url = f"{config.API_BASE_URL}markets/quotes"

headers = {
  'Authorization': 'Bearer {}'.format(config.ACCESS_TOKEN), 
  'Accept': 'application/json'
}
response = requests.get(quote_url,
    # The 'AAPL' symbol is used to get quotes from Apple
    params={'symbols': 'AAPL'},
    headers=headers
)
# JSON response
print(response.json())


# Send an authenticated request to the Tradier API for getting option chains
# Documentation: https://documentation.tradier.com/brokerage-api/markets/get-options-chains
option_chain_url = f"{config.API_BASE_URL}markets/options/chains"
response = requests.get(option_chain_url,
    # Contains options data from Tesla on the exact date of Dec 28, 2023
    params={'symbol': 'TSLA', 'expiration': '2023-12-28'},
    headers=headers
)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON response
    json_response = response.json()

    # Pretty-print the JSON data
    formatted_json = json.dumps(json_response, indent=4)

    # Save the formatted JSON to a text file
    with open('tsla.txt', mode='wt') as file:
        file.write(formatted_json)


# Send an authenticated request to the Tradier API for placing an option order
# Documentation: https://documentation.tradier.com/brokerage-api/trading/place-option-order
order_url = f"{config.API_BASE_URL}accounts/{config.ACCOUNT_ID}/orders"

response = requests.post(order_url,
    # Change params as needed
    # Note that 'option_symbol' has the specific option with a specific date (you can find this info in the formated JSON above)
    data={'class': 'option', 'symbol': 'SPY', 'option_symbol': 'SPY140118C00195000', 'side': 'buy_to_open', 'quantity': '10', 'type': 'market', 'duration': 'day', 'price': '1.00', 'stop': '1.00', 'tag': 'my-tag-example-1'},
    headers=headers
)


# Send an authenticated request to the Tradier API for getting account orders
# Documentation: https://documentation.tradier.com/brokerage-api/accounts/get-account-orders
orders = requests.get(order_url, headers=headers)
