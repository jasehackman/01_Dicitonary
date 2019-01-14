# Instructions
# A block of publicly traded stock has a variety of attributes. Let's look at a few of them.
# A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

# Example
# stockDict = { 'GM': 'General Motors',
#  'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

stocks = {
  'GM': 'General Motors',
  "Cat": "Caterpillar",
  "ATT": "AT&T",
  "ABC": "AmerisourceBergen Corporation",
  "ABM": "ABM Industries Incorporated"
  }


# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

# Example
# purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
#  ( 'CAT', 100, '1-apr-1999', 24 ),
#  ( 'GE', 200, '1-jul-1998', 56 ) ]

buys = [("GM", 100, '10-aug-2002', 34), ("Cat", 145, '10-aug-2002', 23), ("ATT", 100, '10-aug-2002', 34), ("ABC", 100, '10-aug-2002', 34),("ABM", 100, '10-aug-2002', 34),("ABM", 100, '10-aug-2002', 34),("ATT", 100, '10-aug-2002', 34)]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.
priceANdName = [(buy[1]*buy[3], [v for (k,v) in stocks.items() if k == buy[0]]) for buy in buys]

print(priceANdName)
# Example output for one block: I purchased General Electric stock for $4800

for each in priceANdName:
  print(f"I purchased {each[1][0]} for {each[0]}")

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE.
# These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased.
# The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

stocdic = dict()


for buy in buys:
  if buy[0] not in stocdic:
    stocdic[buy[0]] = [buy]
  else:
    stocdic[buy[0]].append(buy)



print(stocdic)


for k,v in stocdic.items():
  print(f"--------------{k}-------------")
  for y in v:
    print(y)

# Example output:

# ------ GE ------
#     ('GE', 100, '10-sep-2001', 48)
#     ('GE', 200, '1-jul-1998', 56)
# Total value of stock in portfolio: $16000