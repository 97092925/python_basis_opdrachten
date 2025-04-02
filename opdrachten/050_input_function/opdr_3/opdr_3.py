
input_waarden = "tomaten, Carrots, cookies, macaroni, controller"
lijst = [item.strip() for item in input_waarden.split(",")]
lijst.sort(reverse=True)
print(lijst)
