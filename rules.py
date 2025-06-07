def cal_miles(miles):
    if miles <= 100:
        return miles * 0.58
    elif miles <= 300:
        return (100 * 0.58) + ((miles - 100) * 0.45)
    elif miles <= 600:
        return (100 * 0.58) + (200 * 0.45) + ((miles - 300) * 0.40)
    else:
        return (100 * 0.58) + (200 * 0.45) + (300 * 0.40) + ((miles - 600) * 0.48)

def cal_efficiency(days, miles):
    miles_per_day = miles / days
    if 180 <= miles_per_day <= 220:
        return 30
    elif 150 <= miles_per_day < 180 or 220 < miles_per_day <= 250:
        return 10
    else:
        return -10

def cal_trip_bonus(trip_duration_days):
    if trip_duration_days == 5:
        return 50  # Keep the sweet spot
    elif 4 <= trip_duration_days <= 6:
        return 25  # Keep moderate bonus for 4-6 days
    elif trip_duration_days >= 8:
        return -(trip_duration_days - 7) * 15  # PENALTY for long trips
    else:
        return 0

def cal_receipts(days, receipts):
    per_day = receipts / days

    # Special handling for 1-day trips - much more conservative
    if days == 1:
        if receipts > 2000:
            return receipts * 0.25
        elif receipts > 1000:
            return receipts * 0.35
        else:
            return receipts * 0.45

    # More generous for 2-3 day trips
    elif days <= 3:
        if per_day > 800:
            return receipts * 0.25
        elif per_day > 400:
            return receipts * 0.35
        else:
            return receipts * 0.50

    # Fix 4-day trips - they shouldn't be penalized so much
    elif days == 4:
        if per_day > 600:
            return receipts * 0.20
        elif per_day > 300:
            return receipts * 0.30
        else:
            return receipts * 0.40

    # 5-6 day trips
    elif days <= 6:
        if per_day > 400:
            return receipts * 0.20
        else:
            return receipts * 0.30

    # Long trips - slightly more generous
    else:
        if per_day > 300:
            return receipts * 0.15
        else:
            return receipts * 0.25


def cal_interactions(days, miles, receipts):
    bonus = 0
    per_day_spending = receipts / days
    miles_per_day = miles / days

    # Kevin's sweet spot: 5 days + efficient + modest spending
    if days == 5 and miles_per_day >= 180 and per_day_spending < 100:
        bonus += 100

    # High mileage + low spending combo bonus
    if miles > 500 and per_day_spending < 50:
        bonus += 20

    # ENHANCED: Single day high-mileage bonuses
    if days == 1:
        if miles > 800:
            bonus += 50  # INCREASED from 30
        elif miles > 600:
            bonus += 30  # NEW tier
        elif miles > 400:
            bonus += 15

    # NEW: Extreme 1-day mileage bonus
    if days == 1 and miles > 800:
        bonus += (miles - 800) * 0.1  # Additional bonus for very high mileage

    return bonus


