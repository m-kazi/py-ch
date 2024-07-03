import requests


def public_stocks():
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        stocks_data = data["data"]
        stock_name_0 = stocks_data["data"][0]["Name"]
        stock_symbol_0 = stocks_data["data"][0]["Symbol"]
        stock_name_1 = stocks_data["data"][1]["Name"]
        stock_symbol_1 = stocks_data["data"][1]["Symbol"]
        return stock_name_0, stock_symbol_0, stock_name_1, stock_symbol_1
    else:
        raise Exception("Failed to fetch the data!")


def main():
    try:
        stock_name_0, stock_symbol_0, stock_name_1, stock_sumbol_1 = public_stocks()
        print(f"{stock_name_0} : {stock_symbol_0} \n{stock_name_1} : {stock_sumbol_1}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
