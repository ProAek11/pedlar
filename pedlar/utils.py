"""pedlar utility functions."""

def calc_profit(order, bid: float, ask: float, leverage: float = 100):
  """Compute the profit of a given order, return closing price and profit."""
  # BIG ASSUMPTION, account currency is the same as base currency
  # Ex. GBP account trading on GBPUSD since we don't have other
  # exchange rates streaming to us to handle conversion
  isbuy = order.type == "buy"
  closep = bid if isbuy else ask # The closing price of the order
  diff = closep - order.price if isbuy else order.price - closep # Price difference
  profit = diff*leverage*order.volume*1000*(1/closep)
  return closep, round(profit, 2)
