def cal_base_reimbursement(days, miles):
    """Base calculation with more nuanced mileage tiers"""
    # Base daily allowance - higher for optimal trip lengths
    if days == 5:
        daily_allowance = days * 95  # Kevin's "sweet spot"
    elif days in [4, 6]:
        daily_allowance = days * 90
    elif days in [1, 2, 3]:
        daily_allowance = days * 85
    elif days <= 8:
        daily_allowance = days * 88
    else:
        # Penalty for very long trips gets stronger
        daily_allowance = days * 80 - (days - 8) * 5

    # More sophisticated mileage calculation
    if miles <= 100:
        mile_amount = miles * 0.50  # Higher rate for short distances
    elif miles <= 300:
        mile_amount = 100 * 0.50 + (miles - 100) * 0.45
    elif miles <= 600:
        mile_amount = 100 * 0.50 + 200 * 0.45 + (miles - 300) * 0.40
    else:
        mile_amount = 100 * 0.50 + 200 * 0.45 + 300 * 0.40 + (miles - 600) * 0.42

    return daily_allowance + mile_amount

def cal_receipt_scaling(days, receipts):
    """Receipt-based scaling - increased factors"""
    per_day = receipts / days

    # Higher scaling factors to make receipts more dominant
    if days == 1:
        if receipts > 1500:
            return 0.25  # Increased from 0.15
        elif receipts > 500:
            return 0.40  # Increased from 0.25
        else:
            return 0.55  # Increased from 0.35
    elif days <= 3:
        if per_day > 400:
            return 0.35  # Increased from 0.20
        else:
            return 0.50  # Increased from 0.30
    elif days <= 7:
        if per_day > 200:
            return 0.30  # Increased from 0.15
        else:
            return 0.45  # Increased from 0.25
    else:  # Long trips
        return 0.40  # Increased from 0.20


def cal_efficiency_multiplier(days, miles, receipts):
    """Efficiency as a multiplier rather than addition"""
    miles_per_day = miles / days

    # Base multiplier
    if 150 <= miles_per_day <= 250:
        multiplier = 1.2  # 20% bonus
    elif 100 <= miles_per_day < 150 or 250 < miles_per_day <= 350:
        multiplier = 1.05  # 5% bonus
    elif miles_per_day >= 350:
        multiplier = 1.15  # High mileage bonus
    else:
        multiplier = 0.9   # Small penalty for very low efficiency

    return multiplier

