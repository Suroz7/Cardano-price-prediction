from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

# Your CoinMarketCap API Key
COINMARKETCAP_API_KEY = "88e17407-d0c9-4b62-9e9b-ff4a213291f3"

# Fetch ADA/USDT data from Binance
def fetch_binance_data():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=ADAUSDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': data['lastPrice'],
            'percent_change_24h': data['priceChangePercent'],
            'volume': data['volume'],
            'quote_volume': data['quoteVolume']
        }
    return None

# Fetch ADA/USDT data from CoinGecko
def fetch_coingecko_data():
    url = "https://api.coingecko.com/api/v3/coins/cardano"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'price': data['market_data']['current_price']['usd'],
            'market_cap': data['market_data']['market_cap']['usd'],
            'volume': data['market_data']['total_volume']['usd']
        }
    return None

# Fetch ADA/USDT data from CoinMarketCap
def fetch_coinmarketcap_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {"X-CMC_PRO_API_KEY": COINMARKETCAP_API_KEY}
    params = {"symbol": "ADA", "convert": "USD"}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        ada_data = data["data"]["ADA"]["quote"]["USD"]
        return {
            'price': ada_data['price'],
            'market_cap': ada_data['market_cap'],
            'volume': ada_data['volume_24h'],
            'percent_change_24h': ada_data['percent_change_24h']
        }
    return None

# Get ADA prediction from Ollama AI
def get_ada_prediction(model_data):
    ollama_url = "http://localhost:11434/api/generate"
    model_name = "deepseek-r1:1.5b"

    headers = {"Content-Type": "application/json"}
    instruction = (
        "You are an AI predicting ADA/USDT prices based on real-time data. "
        "Here is the latest market data. Analyze and predict the future price:"
    )

    payload = {
        "model": model_name,
        "prompt": f"{instruction}\n\nData: {json.dumps(model_data)}\n\nPredict ADA's price:",
        "stream": False
    }

    response = requests.post(ollama_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    return None

# Flask API Endpoint
@app.route('/api/ada-data', methods=['GET'])
def get_ada_data():
    binance_data = fetch_binance_data()
    coingecko_data = fetch_coingecko_data()
    coinmarketcap_data = fetch_coinmarketcap_data()

    if not binance_data or not coingecko_data or not coinmarketcap_data:
        return jsonify({"error": "Failed to fetch ADA data"}), 500

    combined_data = {
        "binance": binance_data,
        "coingecko": coingecko_data,
        "coinmarketcap": coinmarketcap_data
    }

    prediction = get_ada_prediction(combined_data)
    return jsonify({"live_data": combined_data, "prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
