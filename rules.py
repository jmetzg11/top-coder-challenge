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

def cal_receipt_scaling(days, receipts):
    """Receipt-based scaling - increased factors"""
    per_day = receipts / days

    if days == 1:
        if receipts > 1500:
            return 0.25
        elif receipts > 500:
            return 0.40
        else:
            return 0.55
    elif days <= 3:
        if per_day > 400:
            return 0.35
        else:
            return 0.50
    elif days <= 7:
        if per_day > 200:
            return 0.30
        else:
            return 0.45
    else:
        return 0.40


def cal_efficiency_multiplier(days, miles):
    """Efficiency as a multiplier rather than addition"""
    miles_per_day = miles / days

    if 150 <= miles_per_day <= 250:
        multiplier = 1.2
    elif 100 <= miles_per_day < 150 or 250 < miles_per_day <= 350:
        multiplier = 1.05
    elif miles_per_day >= 350:
        multiplier = 1.15
    else:
        multiplier = 0.9

    return multiplier
