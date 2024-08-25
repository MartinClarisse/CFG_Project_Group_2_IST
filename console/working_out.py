# imports within python.
import pandas as pd
from datetime import date

# ------------------------------------------------------------
# imports from my the directory itself.
from trips_sql import View_trips, View_costs, View_contributions
from db import query_db
from dashboard import dashboard


trip_id = 2
member_id = 2

costs = View_costs(trip_id)
total_costs = costs.view_total_cost()
total_costs = total_costs[0][0]

contributions = View_contributions(member_id, trip_id)
total_contributions = contributions.view_contribution()
total_contributions = total_contributions[0][0]

remaining_contributions = total_costs - total_contributions

print(costs)
print(total_costs)