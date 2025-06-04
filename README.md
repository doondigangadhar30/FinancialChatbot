# Financial Chatbot Prototype 🚀

A simple Python chatbot that answers 5 predefined financial queries for **Microsoft, Tesla, and Apple** using data from 10-K filings in a CSV. Ideal for learning rule-based chatbot development.

---

## 📊 Features

- Answers queries on:
  - Total revenue
  - Net income change
  - Total assets
  - Cash flow from operations
  - Overall financial health
- Uses `pandas` to load data from `financial_data.csv`
- CLI interaction with simple `input()` commands

---

## 🛠️ Requirements

- Python 3.8+
- pandas
- CSV file with the following format:

```csv
Company,Year,Total Revenue,Net Income,Total Assets,Total Liabilities,Cash Flow from Operating Activities
Apple,2023,383285000000,96995000000,352583000000,290437000000,110543000000
Tesla,2023,96773000000,14974000000,106618000000,43009000000,13256000000
Microsoft,2023,211915000000,72361000000,411976000000,205753000000,87582000000
```

# 📥 Installation
```bash
git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot
pip install pandas
```
- Add your financial_data.csv file in the project directory.


## 🧪 Example Output

| Query | Response |
|-------|----------|
| What is the total revenue for Apple? | $383,285,000,000.00 |
| How has net income changed for Tesla? | Increased by 25.50% |
| Total assets for Microsoft? | $411,976,000,000.00 |
| Invalid query | Only supports predefined queries |

## 🚫 Limitations
- Only 5 hardcoded queries supported
- No NLP or fuzzy matching
- Requires correctly formatted CSV

## 🤝 Contributing
Fork, submit issues, or PRs to contribute!
Happy coding! 🎉
