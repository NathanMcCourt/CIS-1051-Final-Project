#Nathan McCourt

fileref = open("C:/Users/natha/OneDrive/Desktop/StarterFiles/Fantasy Football Week 13 Data.csv", "r", encoding = "utf-8-sig")
lines = fileref.readlines()

qb = {}
rb = {}
wr = {}
te = {}
flx = {}
df = {}
k = {}

for line in lines[1:]:
    category = line.strip().split(",")
    #print(category)
    
    if category[0] == "QB":
        qb[(category[1])] = (category[2])
    elif category[0] == "RB":
        rb[(category[1])] = (category[2])
        flx[(category[1])] = (category[2])
    elif category[0] == "WR":
        wr[(category[1])] = (category[2])
        flx[(category[1])] = (category[2])
    elif category[0] == "TE":
        te[(category[1])] = (category[2])
        flx[(category[1])] = (category[2])
    elif category[0] == "D/ST":
        df[(category[1])] = (category[2])
    else:
        k[(category[1])] = (category[2])

##print(qb)
##print(rb)
##print(wr)
##print(te)
##print(flx)
##print(df)
##print(k)

qbscores = list(qb.values())
rbscores = list(rb.values())
wrscores = list(wr.values())
tescores = list(te.values())
dfscores = list(df.values())
kscores = list(k.values())

qbscore_map = map(float, qbscores)
qbscore_list = list(qbscore_map)

rbscore_map = map(float, rbscores)
rbscore_list = list(rbscore_map)

wrscore_map = map(float, wrscores)
wrscore_list = list(wrscore_map)

tescore_map = map(float, tescores)
tescore_list = list(tescore_map)

dfscore_map = map(float, dfscores)
dfscore_list = list(dfscore_map)

kscore_map = map(float, kscores)
kscore_list = list(kscore_map)
                    

qb_high = max(qbscore_list)
rb1_high = max(rbscore_list)
rbscore_list.remove(rb1_high)
rb2_high = max(rbscore_list)
rbscore_list.remove(rb2_high)
wr1_high = max(wrscore_list)
wrscore_list.remove(wr1_high)
wr2_high = max(wrscore_list)
wrscore_list.remove(wr2_high)
te_high = max(tescore_list)
tescore_list.remove(te_high)
df_high = max(dfscore_list)
k_high = max(kscore_list)

flx_list = rbscore_list + wrscore_list + tescore_list
flx_high = max(flx_list)

total = float(qb_high + rb1_high + rb2_high + wr1_high + wr2_high + te_high + flx_high + df_high + k_high)

def starting_position(a, b, c, d, e, f, g, h, i):
    inv_qb = {v: k for k, v in qb.items()}
    inv_rb = {v: k for k, v in rb.items()}
    inv_wr = {v: k for k, v in wr.items()}
    inv_te = {v: k for k, v in te.items()}
    inv_flx = {v: k for k, v in flx.items()}
    inv_df = {v: k for k, v in df.items()}
    inv_k = {v: k for k, v in k.items()}
    startinglineup = []
    startinglineup.append(inv_qb[a])
    startinglineup.append(inv_rb[b])
    startinglineup.append(inv_rb[c])
    startinglineup.append(inv_wr[d])
    startinglineup.append(inv_wr[e])
    startinglineup.append(inv_te[f])
    startinglineup.append(inv_flx[g])
    startinglineup.append(inv_df[h])
    startinglineup.append(inv_k[i])
    return(startinglineup)
    
          
qh = str(qb_high)
r1h = str(rb1_high)
r2h = str(rb2_high)
w1h = str(wr1_high)
w2h = str(wr2_high)
th = str(te_high)
fh = str(flx_high)
dh = str(df_high)
kh = str(k_high)
starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)

headings = ("Position", "Player", "Projected Score")
positions = ["QB", "RB1", "RB2", "WR1", "WR2", "TE", "Flex", "D/ST", "K"]

print("This Week's Starting Lineup: (Fantasy Football)", "\n")

titlePosition = "Position"
titlePlayer = "Player"
titleProjectedScore = "Projected Score"
print("%-15s %-20s %-20s" %(titlePosition, titlePlayer, titleProjectedScore))
#QB
position = positions[0]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[0]
projectedscore = qh
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#RB1
position = positions[1]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[1]
projectedscore = r1h
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#RB2
position = positions[2]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[2]
projectedscore = r2h
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#WR1
position = positions[3]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[3]
projectedscore = w1h
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#WR2
position = positions[4]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[4]
projectedscore = w2h
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#TE
position = positions[5]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[5]
projectedscore = th
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#FLEX
position = positions[6]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[6]
projectedscore = fh
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#D/ST
position = positions[7]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[7]
projectedscore = dh
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#K
position = positions[8]
player = starting_position(qh, r1h, r2h, w1h, w2h, th, fh, dh, kh)[8]
projectedscore = kh
print("%-15s %-20s %-20s" %(position, player, projectedscore))
#Last Line
firstline = " "
secondline = " "
thirdline = round(total, 2)
print("%-15s %-20s %-20s %-20s" %(firstline, secondline, thirdline, ":Total"))


fileref.close()







        
        
        



    

    
