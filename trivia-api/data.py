
import requests
AMOUNT = 10
CATEGORY = 15
TYPE = "boolean"
response = requests.get(url=f"https://opentdb.com/api.php?amount={AMOUNT}&category={CATEGORY}&type={TYPE}")
response.raise_for_status()
question_data = response.json()["results"]
print(question_data)