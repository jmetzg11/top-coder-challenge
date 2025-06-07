def cal_base_reimbursement(days, miles):
    """Base calculation: focus on per-day allowance + mileage"""
    # Start with a base per-day allowance
    daily_allowance = days * 85  # Base daily rate

    # Simple mileage calculation - less complex tiers
    if miles <= 200:
        mile_amount = miles * 0.45
    elif miles <= 600:
        mile_amount = 200 * 0.45 + (miles - 200) * 0.38
    else:
        mile_amount = 200 * 0.45 + 400 * 0.38 + (miles - 600) * 0.42

    # Much gentler trip adjustments
    if days == 5:
        daily_allowance += 25
    elif days in [4, 6]:
        daily_allowance += 15
    elif days >= 12:  # Only penalize very long trips slightly
        daily_allowance -= (days - 11) * 8

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
