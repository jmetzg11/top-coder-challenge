def cal_base_reimbursement(days, miles):
    """Base calculation with more nuanced mileage tiers"""
    if days == 5:
        daily_allowance = days * 95
    elif days in [4, 6]:
        daily_allowance = days * 90
    elif days in [1, 2, 3]:
        daily_allowance = days * 85
    elif days <= 8:
        daily_allowance = days * 88
    else:
        daily_allowance = days * 80 - (days - 8) * 5

    if miles <= 100:
        mile_amount = miles * 0.50
    elif miles <= 300:
        mile_amount = 100 * 0.50 + (miles - 100) * 0.45
    elif miles <= 600:
        mile_amount = 100 * 0.50 + 200 * 0.45 + (miles - 300) * 0.40
    else:
        mile_amount = 100 * 0.50 + 200 * 0.45 + 300 * 0.40 + (miles - 600) * 0.42

    return daily_allowance + mile_amount

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


def cal_receipt_scaling(days, miles, receipts):
    """Improved receipt scaling that considers both days and mileage context"""
    per_day = receipts / days
    miles_per_day = miles / days

    if days == 1:
        if receipts <= 100:
            base_factor = 0.75
        elif receipts <= 300:
            base_factor = 0.65
        elif receipts <= 500:
            base_factor = 0.55
        elif receipts <= 1000:
            base_factor = 0.50
        else:
            base_factor = 0.55
    else:
        if days <= 3:
            base_factor = 0.35 if per_day > 400 else 0.50
        elif days <= 7:
            base_factor = 0.30 if per_day > 200 else 0.45
        else:
            base_factor = 0.40

    if days == 1:
        if miles_per_day < 50 and receipts > 800:
            base_factor = min(0.85, base_factor + 0.30)
        elif miles_per_day > 350 and receipts < 400:
            base_factor = max(0.45, base_factor - 0.10)

    return base_factor




def cal_efficiency_multiplier(days, miles):
    miles_per_day = miles / days
    if 150 <= miles_per_day <= 250:
        multiplier = 1.10
    elif 100 <= miles_per_day < 150 or 250 < miles_per_day <= 350:
        multiplier = 1.02
    elif miles_per_day >= 350:
        multiplier = 1.05
    else:
        multiplier = 0.95

    return multiplier
