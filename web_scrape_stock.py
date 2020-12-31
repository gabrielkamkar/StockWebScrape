# The purpose of this practice example is to create a stock price monitoring program. To keep track of the fluxuations
# of Amazon from Yahoo finance. Only one stock becuase the process is basically the same for all the stock companies.
# Amazon: https://finance.yahoo.com/quote/AMZN?p=AMZN


# Importing all the packages I need
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Start by requesting the html code from yahoo and then make it readable.
amzn_page = requests.get('https://finance.yahoo.com/quote/AMZN?p=AMZN')

amzn_page.status_code # If access code starts with 2 it worked well

amzn_soup = BeautifulSoup(amzn_page.content, 'html.parser')

# Now I'm gonna read and parse through the html to get the name, closing value, change, opening value, and prev close
amzn_header = amzn_soup.find(id= 'quote-header-info')

amzn_name = amzn_header.find(class_='D(ib) Fz(18px)').get_text() # got name

amzn_price = amzn_header.find(class_='My(6px) Pos(r) smartphone_Mt(6px)')

amzn_prices = amzn_price.find_all('span')

amzn_values = [ap.get_text() for ap in amzn_prices]

# get closing and change values
amzn_close = amzn_values[0]
amzn_close_perc = amzn_values[1]

# the next to values (open value, and prev close) were in a different part of the webpage.
amzn_quote = amzn_soup.find(id='quote-summary')

amzn_info = amzn_quote.find_all(class_='Ta(end) Fw(600) Lh(14px)')

amzn_open_close = [ai.get_text() for ai in amzn_info]

amzn_prev_close = amzn_open_close[0]
amzn_open = amzn_open_close[1]


# Now compile a dataframe and add the values to their respective names.
amzn = pd.DataFrame({
    'Name':amzn_name,
    'Price':amzn_close,
    'Change':amzn_close_perc,
    'Open':amzn_open,
    'Previous Close':amzn_prev_close
    }
    , index=[1]
)
pd.set_option('colheader_justify', 'center') # center names

print(amzn)




