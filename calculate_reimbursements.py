import sys
from rules import cal_base_reimbursement, cal_receipt_scaling, cal_efficiency_multiplier


def calculate_reimbursement(days, miles, receipts):
    """Try multiplicative approach"""

    if days == 0:
        return 0.0

    cents = int(round(receipts * 100)) % 100
    if cents in [49, 99]:
        base = cal_base_reimbursement_49_99(days, miles)
        bonus = 55.00
        penalty_factor = 0.061
        receipt_adjustment = bonus - (receipts * penalty_factor)
        reimbursement = base + receipt_adjustment
        return max(0, round(reimbursement, 2))

    base = cal_base_reimbursement(days, miles)


    receipt_factor = cal_receipt_scaling(days, miles, receipts)
    efficiency_mult = cal_efficiency_multiplier(days, miles)
    reimbursement = base + (receipts * receipt_factor * efficiency_mult)


    return max(0, round(reimbursement, 2))





def cal_base_reimbursement_49_99(days, miles):
    if days == 1:
        daily_allowance = days * 75
    elif days in [2, 3]:
        daily_allowance = days * 82
    elif days in [4, 5, 6]:
        daily_allowance = days * 88
    elif days <= 10:
        daily_allowance = days * 85
    else:
        daily_allowance = days * 78

    if miles <= 200:
        mile_amount = miles * 0.35
    elif miles <= 500:
        mile_amount = 200 * 0.35 + (miles - 200) * 0.38
    else:
        mile_amount = 200 * 0.35 + 300 * 0.38 + (miles - 500) * 0.42

    return daily_allowance + mile_amount


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
        sys.exit(1)

    days = int(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])

    result = calculate_reimbursement(days, miles, receipts)
    print(result)  # Only output the number, nothing else
