def validate_month(month):
    if month >= 1 and month <= 12:
        return True
    else:
        return False

# Test case
month = 6
result = validate_month(month)
print(f"The month '{month}' is valid: {result}")
