import ccxt
import pandas as pd

exchange = ccxt.binance()

def pro_scanner():
    print("\n--- Pro Scanner: Searching for Money Flow ---")
    
    # 1. Saaray coins ka data uthao
    markets = exchange.fetch_tickers()
    
    # 2. Aik list banao takay hum check kar saken kon sa best hai
    coin_list = []
    
    for symbol, data in markets.items():
        if '/USDT' in symbol:  # Sirf USDT wale pairs
            change = data['percentage'] # 24h mein kitna % upar/niche gaya
            volume = data['quoteVolume'] # Kitna paisa (USDT) trade hua
            
            coin_list.append({
                'Symbol': symbol,
                'Change %': change,
                'Volume': volume
            })

    # 3. Data ko table mein convert karo
    df = pd.DataFrame(coin_list)
    
    # 4. Filter: Sirf wo coins jin mein 10 Million USDT se zyada volume ho (Pro Rule)
    df = df[df['Volume'] > 10000000]
    
    # 5. Sorting: Sab se zyada pump honay wale coins upar
    top_coins = df.sort_values(by='Change %', ascending=False).head(5)
    
    print(top_coins.to_string(index=False))
    print("\n--- In Coins mein 'Smart Money' move ho raha hai ---")

pro_scanner()