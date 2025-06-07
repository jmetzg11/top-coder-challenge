import sys
from rules import *

def calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount):
    amount = 100 * trip_duration_days

    miles_amount = cal_miles(miles_traveled)

    efficiency_amount = cal_efficiency_bonus(trip_duration_days, miles_traveled)

    trip_bonus = cal_trip_bonus(trip_duration_days)

    receipts_amount = cal_receipts(trip_duration_days, total_receipts_amount)

    interactions_amount = cal_interactions(trip_duration_days, miles_traveled, total_receipts_amount)

    return round(amount + miles_amount + efficiency_amount + trip_bonus + receipts_amount + interactions_amount, 2)





if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
        sys.exit(1)

    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])

    result = calculate_reimbursement(days, miles, receipts)
    print(result)  # Only output the number, nothing else
