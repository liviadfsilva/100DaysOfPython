from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager().update_price()
print(data)