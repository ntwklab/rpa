import rpa as r
import os
import csv

basedir = os.path.abspath(os.path.dirname(__file__))

def write_csv(write_file, data_list):
    
    # Output
    with open(write_file, "w", newline="") as f:
        csv_writer = csv.DictWriter(f, data_list[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(data_list)
    print("CSV written out")


r.init(True, True)
r.url('https://www.x-rates.com/table/?from=USD&amount=1')
r.wait(2.5)
euro = r.read('//*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[17]/td[2]/a')
gbp = r.read('//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[2]/td[2]/a')
aud = r.read('//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[4]/td[2]/a')
cad = r.read('//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[5]/td[2]/a')
yen = r.read('//*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[9]/td[2]/a')

print(f"\n1 USD buys: {euro} Euro")
print(f"1 USD buys: {gbp} GBP")
print(f"1 USD buys: {aud} AUD")
print(f"1 USD buys: {cad} CAD")
print(f"1 USD buys: {yen} YEN\n")
r.wait(1)
r.close()

forex_list = []
forex_dict = {"Euro":euro,
            "GBP":gbp,
            "AUD":aud,
            "CAD":cad,
            "Yen":yen
            } 
forex_list.append(forex_dict)



# Write Output
write_file = f"{basedir}/forex.csv"
write_csv(write_file,forex_list)
