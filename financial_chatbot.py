import pandas as pd

# Load the financial data from the CSV file (replace with your actual file path)
df = pd.read_csv('financial_data.csv')

# Function to calculate year-over-year change for a metric
def calculate_yoy_change(company, metric):
    company_data = df[df['Company'] == company].sort_values('Year')
    latest_year = company_data.iloc[-1][metric]
    previous_year = company_data.iloc[-2][metric] if len(company_data) > 1 else 0
    change = ((latest_year - previous_year) / previous_year * 100) if previous_year != 0 else 0
    return latest_year, change

# Predefined queries and responses
def simple_chatbot(user_query):
    # Normalize user query to lowercase for case-insensitive matching
    user_query = user_query.lower().strip()

    # Query 1: Total Revenue
    if "total revenue" in user_query and any(company in user_query for company in ["microsoft", "tesla", "apple"]):
        company = next((c for c in ["microsoft", "tesla", "apple"] if c in user_query), None)
        if company:
            latest_revenue, _ = calculate_yoy_change(company.capitalize(), 'Total Revenue')
            return f"The total revenue for {company.capitalize()} in the latest year is ${latest_revenue:,.2f}."
    
    # Query 2: Net Income Change
    elif "net income change" in user_query and any(company in user_query for company in ["microsoft", "tesla", "apple"]):
        company = next((c for c in ["microsoft", "tesla", "apple"] if c in user_query), None)
        if company:
            _, change = calculate_yoy_change(company.capitalize(), 'Net Income')
            trend = "increased" if change > 0 else "decreased"
            return f"The net income for {company.capitalize()} has {trend} by {abs(change):.2f}% over the last year."
    
    # Query 3: Total Assets
    elif "total assets" in user_query and any(company in user_query for company in ["microsoft", "tesla", "apple"]):
        company = next((c for c in ["microsoft", "tesla", "apple"] if c in user_query), None)
        if company:
            latest_assets, _ = calculate_yoy_change(company.capitalize(), 'Total Assets')
            return f"The total assets for {company.capitalize()} in the latest year are ${latest_assets:,.2f}."
    
    # Query 4: Cash Flow from Operating Activities
    elif "cash flow" in user_query and any(company in user_query for company in ["microsoft", "tesla", "apple"]):
        company = next((c for c in ["microsoft", "tesla", "apple"] if c in user_query), None)
        if company:
            latest_cash_flow, _ = calculate_yoy_change(company.capitalize(), 'Cash Flow from Operating Activities')
            return f"The cash flow from operating activities for {company.capitalize()} in the latest year is ${latest_cash_flow:,.2f}."
    
    # Query 5: General Financial Health
    elif "financial health" in user_query and any(company in user_query for company in ["microsoft", "tesla", "apple"]):
        company = next((c for c in ["microsoft", "tesla", "apple"] if c in user_query), None)
        if company:
            latest_revenue, _ = calculate_yoy_change(company.capitalize(), 'Total Revenue')
            latest_net_income, _ = calculate_yoy_change(company.capitalize(), 'Net Income')
            return f"{company.capitalize()}'s financial health shows a total revenue of ${latest_revenue:,.2f} and a net income of ${latest_net_income:,.2f} in the latest year."
    
    else:
        return "Sorry, I can only provide information on predefined queries about Microsoft, Tesla, or Apple (e.g., 'What is the total revenue for Apple?', 'How has net income changed for Tesla?')."

# Command-line interaction
def run_chatbot():
    print("Welcome to the Financial Chatbot! Ask about Microsoft, Tesla, or Apple financials.")
    print("Example queries: 'What is the total revenue for Apple?', 'How has net income changed for Tesla?'")
    print("Type 'exit' to quit.")
    
    while True:
        user_query = input("\nYour query: ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        response = simple_chatbot(user_query)
        print(response)

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
