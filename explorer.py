import pandas as pd
import json
from calculate_reimbursements import calculate_reimbursement

with open('public_cases.json', 'r') as f:
    data = json.load(f)

flattened_data = []
for item in data:
    row = item['input']
    row['expected_output'] = item['expected_output']
    flattened_data.append(row)

df = pd.DataFrame(flattened_data)


errors = {}
for i, row in df.iterrows():
    days = row['trip_duration_days']
    miles = row['miles_traveled']
    receipts = row['total_receipts_amount']
    expected_output = row['expected_output']
    result = calculate_reimbursement(days, miles, receipts)

    relative_error = abs(result - expected_output) / expected_output * 100
    real_error = result - expected_output
    errors[relative_error] = (days, miles, receipts, round(expected_output, 2), round(result, 2), round(real_error, 2))

sorted_errors = sorted(errors.items(), reverse=True)
total_error = sum(error for error, _ in sorted_errors)

with open('error_analysis.txt', 'w') as f:
    f.write("Error%   Diff  Days Miles Receipts Expected  Actual\n")
    for error, (days, miles, receipts, expected, actual, real_err) in sorted_errors:
       direction = "+" if real_err > 0 else "-"
       f.write(f"{error:5.1f}% {direction}{abs(real_err):6.0f} {int(days):4d} {int(miles):5d} {receipts:8.2f} {expected:8.2f} {actual:7.2f}\n")



print(f"Total: {total_error:.2f}, average error: {total_error/len(sorted_errors):.2f}")
