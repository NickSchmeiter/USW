# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    import time

    from selenium import webdriver
    from statistics import mean


    d = webdriver.Chrome('C:\\Users\\nicks\Downloads\chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
    x=1
    pricelist = []
    for x in range(1,4):
        url = 'https://www.ebay.de/b/Damenkleider/63861/bn_1619088?_pgn='+str(x)
        d.get(url)
        d.implicitly_wait(5)
        i=1
        while i<49:
              result = d.find_element_by_xpath('//*[@id="s0-29_1-9-0-1[0]-0-0"]/ul/li['+str(i)+']/div/div[2]/div/div[1]/span')
              pricestringwitheur=result.get_attribute('innerHTML')
              pricestring=pricestringwitheur.replace('EUR ', '')
              pricestring=pricestring.replace(',','.')
              if '<span class="DEFAULT">' in pricestring:
                  pricestring=pricestring[-6:]
                  if '>' in pricestring:
                      pricestring = pricestring.replace('>', '')
                  if 'n' in pricestring:
                      pricestring = pricestring.replace('n', '')
              elif '<span class="ITALIC">' in pricestring:
                  pricestring = pricestring[-12:-7]

              price=float(pricestring)
              pricelist.append(price)
              i += 1;
        x+=1;
    mean=mean(pricelist)
    print(mean)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
