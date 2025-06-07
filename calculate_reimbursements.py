import sys
from rules import *

def calculate_reimbursement(days, miles, receipts):
    """Try multiplicative approach"""
    base = cal_base_reimbursement(days, miles)
    receipt_factor = cal_receipt_scaling(days, receipts)
    efficiency_mult = cal_efficiency_multiplier(days, miles, receipts)

    # Try: base + (receipts * receipt_factor * efficiency_mult)
    return base + (receipts * receipt_factor * efficiency_mult)




if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
        sys.exit(1)

    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])

    result = calculate_reimbursement(days, miles, receipts)
    print(result)  # Only output the number, nothing else
