"""Example of Cryptocurrency Alerter in Python """

from crypto_data import get_coins, Coin


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!!TRIGGERED!!!')
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    alert('btc', bottom=60000, top=90000, coins_list=coins)
    alert('eth', bottom=2200, top=3500, coins_list=coins)
    alert('qnt', bottom=90, top=110, coins_list=coins)