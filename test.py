
def test(mainCity):
    titleDict = {
        'design': '🥇 Web Design Agency in ' + mainCity + '. Web designers in ' + mainCity,
        'development': '🥇 Web Development Agency in ' + mainCity + '. Web developers in ' + mainCity,
        'magento': '🥇 Magento Web Development & eCommerce consulting agency in ' + mainCity,
        'shopify': '🥇 Shopify Development Agency in ' + mainCity + '. Web developers in ' + mainCity,
        'wordpress': '🥇 WordPress & WooCommerce Development Agency in ' + mainCity + '. Web developers in ' + mainCity
    }
    print(titleDict['design'])


cities = ['ONE', 'TWO', 'THREE']


for city in cities:
    test(city)