import locale

# Initial parameters 
initial_fcf = 100 # $40 million
growth_rate_10_years = 0.1  # 10%
growth_rate_terminal = 0.035  # 3.5%
discount_rate = 0.12  # 12%
years = 10  # First 10 years
share_count = 100  # 100 million shares

def calculate_cash_flows(initial_earnings, growth_rate, years):
    return [initial_earnings * (1 + growth_rate)**year for year in range(1, years + 1)]

def calculate_terminal_value(cash_flow, growth_rate, discount_rate):
    if discount_rate == growth_rate:
        raise ValueError("Discount rate and terminal rate cannot be equal")
    return cash_flow * (1 + growth_rate) / (discount_rate - growth_rate)

def calculate_present_values(cash_flows, discount_rate):
    return [cf / (1 + discount_rate)**year for year, cf in enumerate(cash_flows, start=1)]

def calculate_intrinsic_value(present_values, terminal_value_discounted):
    return sum(present_values) + terminal_value_discounted

def calculate_intrinsic_value_per_share(intrinsic_value, share_count):
    return intrinsic_value / share_count

cash_flows = calculate_cash_flows(initial_fcf, growth_rate_10_years, years)
terminal_value = calculate_terminal_value(cash_flows[-1], growth_rate_terminal, discount_rate)
present_values = calculate_present_values(cash_flows, discount_rate)
terminal_value_discounted = terminal_value / (1 + discount_rate)**years
intrinsic_value = calculate_intrinsic_value(present_values, terminal_value_discounted)
intrinsic_value_per_share = calculate_intrinsic_value_per_share(intrinsic_value, share_count)

# Format intrinsic_value_per_share as dollars
locale.setlocale(locale.LC_ALL, '')
intrinsic_value_per_share_formatted = locale.currency(intrinsic_value_per_share, grouping=True)

print(intrinsic_value_per_share_formatted)
