dereceTipi = input("derece tipi girin: ")
dereceTipi = dereceTipi if dereceTipi in ("celcius", "kelvin", "fahrenheit")
dereceOld = int(input("derece girin: "))
derece = dereceOld - 273 if dereceTipi == "kelvin" else ((dereceOld - 32) * 5 / 9 if dereceTipi == "fahrenheit" else dereceOld)
if dereceTipi != "celcius": print(f"{dereceOld} {dereceTipi} = {derece} Celcius")


if derece < 8: print("çok soğuk")
elif derece < 15: print("soğuk")
elif derece < 24: print("ılık")
elif derece < 32: print("sıcak")
else: print("çok sıcak")
