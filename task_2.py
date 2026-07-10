deposit_account = {
"client_id": "C1025",
"balance": 5000.0,
"currency": "UAH",
"interest_rate": 0.08, # 8% річних
"is_active": True
}


interest = deposit_account["balance"] * deposit_account["interest_rate"]

print(interest)


deposit_account["balance"] = deposit_account["balance"] + interest


deposit_account["last_update_type"] = "interest accrual"


deposit_account["is_active"] = False


print(deposit_account)