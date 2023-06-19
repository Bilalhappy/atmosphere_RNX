import psypy.psySI as SI

RNX_met = "ISTA00TUR_R_20231680000_01D_30S_MM.rnx"


f = open(RNX_met,"r")
data = f.readlines()
f.close()
for i in range(len(data)):
    if data[i].split()[0] == "END":
        break
del data[:i+1]
for i in range(len(data)):
    if data[i].split()[3] == "8" and data[i].split()[4] == "0" and data[i].split()[5] == "0":
        break
del data[:i]

for K in range(len(data)):
    if data[K].split()[3] == "20" and data[K].split()[4] == "0" and data[K].split()[5] == "0":
        break
    
if int(data[0].split()[1])>9:
    f = open(((data[0].split()[2]+data[0].split()[1]+data[0].split()[0])+"_Atmosferik_veriler.txt"),"w+")
else:
    f = open(((data[0].split()[2]+"0"+data[0].split()[1]+data[0].split()[0])+"_Atmosferik_veriler.txt"),"w+")

f.write(" Year MM Day Hour\tPressure(mm Hg)\t Dry Temperature(C)\t\tHum.(%)\t\tWet Temperature(C)\n")
f.write(" Yıl  Ay Gün Saat\tBasınç (mm Hg) \t Kuru Sıcaklık(C)\t\tNem (%)\t\tIslak Sıcaklık (C)\n\n")

i = 0
while i < (K+1):
    press = float(data[i].split()[6])
    T = float(data[i].split()[7])
    rh = float(data[i].split()[8])
    S=SI.state("DBT",T+273.15,"RH",rh/100,press*133.322387415) #mmHg to Pa -> *133.322387415
    f.write(f"{data[i][:22]}\t{press}\t\t\t{T}\t\t\t{rh}\t\t{round(S[5]-273,1)}\n\n")
    i += 30
f.close()
    
