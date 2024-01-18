# Discounted Cash Flow (DCF) Calculation Script

## What is a Discounted Cash Flow Calculation?

Discounted Cash Flow (DCF) is a valuation method used to estimate the value of an investment based on its expected future cash flows. The process involves forecasting the total amount of future cash flows and then discounting them back to the present value, using a discount rate that reflects the opportunity cost, cost of capital and the return expected from the investment. This approach helps in understanding the intrinsic value of a company, asset, or project based on its ability to generate cash flows in the future. 

The main components of a DCF calculation include:
- **Future Cash Flows**: This represents the cash that is expected to be generated over a certain period.
- **Terminal Value**: The value of the company after the forecast period.
- **Discount Rate**: The rate used to 'discount' future cash flows back to the present value, reflecting the opportunity cost and time value of money.

## Initial Parameters

The script uses several initial parameters to calculate the DCF:

- **initial_fcf (Initial Free Cash Flow)**: This is the starting value of the company's annual free cash flow.
- **growth_rate_10_years (Growth Rate for the First 10 Years)**: The annual growth rate expected for the company's free cash flow during the first 10 years.
- **growth_rate_terminal (Terminal Growth Rate)**: The rate at which the company's free cash flow is expected to grow indefinitely after the first 10 years.
- **discount_rate (Discount Rate)**: The rate used to discount future cash flows to their present values.
- **years (Forecast Period)**: The number of years for which the cash flows are explicitly calculated (usually 10 years).
- **share_count (Number of Shares)**: The total number of outstanding shares of the company.

## Script Overview

At a high level, the script performs the following steps to calculate the intrinsic value per share:

1. **Calculate Cash Flows**: It forecasts the future cash flows of the company for a specified number of years based on the initial free cash flow and the growth rate.
2. **Calculate Terminal Value**: It calculates the terminal value of the company, which is the value of all future cash flows beyond the forecast period, at the end of the specified number of years.
3. **Discount Cash Flows**: It then discounts these future cash flows, including the terminal value, back to their present value using the discount rate.
4. **Calculate Intrinsic Value**: It sums up the present values of the forecasted cash flows and the present value of the terminal value to derive the total intrinsic value of the company.
5. **Determine Intrinsic Value Per Share**: Finally, it divides the total intrinsic value by the number of shares to find the intrinsic value per share.

The result is the estimated intrinsic value per share of the company.

## How to Run the Script

To run this script, ensure you have Python installed on your machine and open your terminal or command prompt, navigate to the repository where the script is located, and run the script using Python by typing:
   ```
   python DCF.py
   ```

## How to Use the Answer

The script calculates the intrinsic value per share of a company by performing a DCF analysis with the given parameters. After running the script, it will display the intrinsic value per share formatted as a currency. This value represents the estimated 'fair' value of one share of the company based on the future cash flows it is expected to generate.

Here's how to interpret and use the answer:
- **Intrinsic Value Per Share**: This is the result printed at the end of the script execution. It represents the estimated value of each share based on the DCF calculation.
- **Investment Decision**: Compare the intrinsic value per share with the current market price of the share. If the intrinsic value is higher than the market price, it might indicate that the stock is undervalued and potentially a good buy. Conversely, if the market price is higher, it might suggest the stock is overvalued.

Modify the initial parameters in the script to suit the specific company you wish to perform analysis on.

**DISCLAIMER** This script is for demonstration and academic purposes only. Please do not base investment decisions on the output of this script.
