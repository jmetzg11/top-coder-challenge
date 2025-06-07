import sys
from rules import cal_base_reimbursement, cal_base_reimbursement_49_99, cal_receipt_scaling, cal_efficiency_multiplier


def calculate_reimbursement(days, miles, receipts):
    """Try multiplicative approach"""

    if days == 0:
        return 0.0

    miles_per_day = miles / days

    # strangeness #1
    cents = int(round(receipts * 100)) % 100
    if cents in [49, 99]:
        base = cal_base_reimbursement_49_99(days, miles)
        bonus = 55.00
        penalty_factor = 0.061
        receipt_adjustment = bonus - (receipts * penalty_factor)
        reimbursement = base + receipt_adjustment
        return max(0, round(reimbursement, 2))

    base = cal_base_reimbursement(days, miles)


    receipt_factor = cal_receipt_scaling(days, receipts)
    efficiency_mult = cal_efficiency_multiplier(days, miles)
    reimbursement = base + (receipts * receipt_factor * efficiency_mult)

    if days == 1 and miles > 450:
        reimbursement *= 1.30

    return max(0, round(reimbursement, 2))




if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
        sys.exit(1)

    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])

    result = calculate_reimbursement(days, miles, receipts)
    print(result)  # Only output the number, nothing else
