"""
Functionality

1. Input years/age, final amount and return amount per month at APY of 5, 7, 10 percent
2. Input years/age, amount per month, return final amount at APY of 5, 7, 10 percent 
"""

def periodic_investment(rate, num_investments, years):
    result = ((1+(rate/num_investments))**(num_investments*years)-1)/(rate/num_investments)
    return result

def savings_per_month():
    
    age = int(input("How old are you? "))
    end_goal = int(input("What is your goal amount? "))

    periodic_payment_5_percent = round(end_goal/periodic_investment(0.05, 12, 60-age),2)
    periodic_payment_7_percent = round(end_goal/periodic_investment(0.07, 12, 60-age),2)
    periodic_payment_10_percent = round(end_goal/periodic_investment(0.10, 12, 60-age),2)
    
    print(f"""
    To save ${end_goal} by age 60 you need to save:
    
        ${periodic_payment_5_percent} per month at 5% per year
        ${periodic_payment_7_percent} per month at 7% per year
        ${periodic_payment_10_percent} per month at 10% per year""")


def total_saved():
    
    age = int(input("How old are you? "))
    monthly_savings = int(input("How much will you save per month? "))

    end_result_5_percent = round(periodic_investment(0.05, 12, 60-age)*monthly_savings,2)
    end_result_7_percent = round(periodic_investment(0.07, 12, 60-age)*monthly_savings,2)
    end_result_10_percent = round(periodic_investment(0.10, 12, 60-age)*monthly_savings,2)

    print(f"""
    If you save ${monthly_savings} per month, then at 60 you will have:
    
        ${end_result_5_percent} at 5% per year
        ${end_result_7_percent} at 7% per year
        ${end_result_10_percent} at 10% per year""")

def wrapper():
    input_choice = int(input("Do you want to calculate total savings (1) or savings per month (2): "))

    if input_choice == 1:
        total_saved()
    elif input_choice == 2:
        savings_per_month()
    else:
        print("Bye bye")
        

if __name__ == "__main__":
    wrapper()