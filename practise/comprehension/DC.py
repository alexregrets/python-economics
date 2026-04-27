companies = ["КАМАЗ", "Газпром", "Сбер", "Лукойл", "МТС"]
revenues = [310, 980, 890, 750, 560]

print({name: rev for name, rev in zip(companies, revenues) if rev > 700 })