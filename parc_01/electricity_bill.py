


# print("Electricity bill estimator")
# electricity_price = float(input("Enter cents per kWh: ")) * 0.01
# daily_use = float(input("Enter daily use in kWh: "))
# days = int(input("Enter number of billing days: "))
# print(f"Estimated bill: ${electricity_price * daily_use * days}")


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
price_choice = float(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))
if price_choice == 11:
    print(f"Estimated bill: ${TARIFF_11 * daily_use * days}")
elif price_choice == 31:
    print(f"Estimated bill: ${TARIFF_31 * daily_use * days}")