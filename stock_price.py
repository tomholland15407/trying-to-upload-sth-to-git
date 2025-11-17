import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
> #### SIMPLE 
### STOCK PRICE APP
# BY THOMAS

---

Shown are the stock ***closing price*** and ***volume*** of Microsoft!

---

1. Closing price
2. Volume

---

- Stock
- Price
- App

---

[cheat sheet available here](https://www.markdownguide.org/cheat-sheet/)

---

| MICROSOFT STOCK | VALUES |
| :-: | :-: |
| Number 1 | CLosing Price |
| Number 2 | Volume |

---

##### CLOSING PRICE

''')

tickerSymbol = 'MSFT'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(start='2024-5-31', end='2025-11-16')

st.line_chart(tickerDf.Close)

st.write('''

---

##### VOLUME

''')

st.line_chart(tickerDf.Volume)




