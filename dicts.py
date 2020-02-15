product = {
"city": "Moscow",
"temperature": "20"
}
print(product["city"])
product["temperature"] = int(product["temperature"]) 
print(product["temperature"] - 5)
print(product["temperature"])
print(product)
print(product.get("country"))