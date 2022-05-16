from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://coinmarketcap.com/"

headers = {
     "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

def searchCurrency(coin: str, DF):
    results = DF[DF.eq(coin).any(1)]
    if(not results.empty):
        return results
    else:
        return 'Error: Not found'

def currencies():
    html = requests.get(URL, headers=headers).text
    sup = BeautifulSoup(html, "html.parser")
    body = sup.tbody
    currencies = body.find_all("tr")[0:10]
    currencyList = list()

    for currency in currencies:
        pTags = currency.find_all("p")
        spanTags = currency.find_all("span")
        currencyInfo = {'Name': pTags[1].text, 'price': spanTags[2].text, 'market_cap': spanTags[8].text}
        currencyList.append(currencyInfo)

    frame = pd.DataFrame(currencyList)
    print(frame)
    frame.to_csv('ExcelParsing.csv')

    while True:

            print("\n" 'Enter the title: ', end=" ")
            print(searchCurrency(str(input()), frame))

currencies()