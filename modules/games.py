
import random
import builtins
import pickle

from datetime import datetime
cashDB = {}


# Initialize user values
def checkUser():
    if (userList[1] not in cashDB.keys()):
        cashDB[userList[1]] = [500,'']    

# General


try:
    f = open("./cashList.bin","rb")
    cashDB = pickle.load(f)
    f.close()
except:
    f = open("./cashList.bin","wb")
    pickle.dump({},f)
    f.close()

def saveData():
    pickle.dump(cashDB,open("./cashList.bin","wb"))

def jc_balance():
    name = builtins.userList[1]
    if (name not in cashDB.keys()):
        cashDB[name] = [500.00,''] 
    jcbot_sendMessage("Balance: " + str(cashDB[userList[1]]))
    

def jc_paycheck():
    checkUser()
    if (cashDB[userList[1]][1] == '' or (datetime.now() -cashDB[userList[1]][1]).seconds >= 36000 ):
        cashDB[userList[1]][1] = datetime.now()
        cashDB[userList[1]][0] += 100
        jcbot_sendMessage("You have recieved a paycheck of 100 credits")
    else:
        jcbot_sendMessage("Come back later for your next paycheck. Seconds remaining: "+str((datetime.now() -cashDB[userList[1]][1]).seconds)) 
    pass
    saveData()

def jc_transfer():
    checkUser()
    user = argsList[1]
    money = argsList[2]
    if (argsList[1] in cashDB.keys()):
        cashDB[userList[1][0]] -= argsList[2]
# Games
def jc_roulette():
    checkUser()
    payout = 0
    computer = random.randint(1,36)
    if (argsList[1] == 'E'):
        argsList[1] = '2-4-6-8-10-12-14-16-18-20-22-24-26-28-30-32-34-36'
    elif (argsList[1] == 'O'):
        argsList[1] = '1-3-5-7-9-11-13-15-17-19-21-23-25-27-29-31-33-35'    
    betList = argsList[1].split('-')
    bet = float(argsList[2])
    if (bet < 0):
        jcbot_sendMessage("Bet cannot be negative..")
        return
    if (bet > cashDB[userList[1]][0]):
        jcbot_sendMessage("Insufficient Funds..")
        return
    cashDB[userList[1]][0] -= bet
    jcbot_sendMessage("Player: "+argsList[1]+" Computer: "+str(computer))
    if (str(computer) in betList):
        jcbot_sendMessage("PAYOUT!" + " Bet Profit Ratio -- " +  str(1/len(betList)*(36-len(betList))) + ":1")
        cashDB[userList[1]][0] += 1/len(betList)*(36-len(betList))* bet + bet
    else:
        jcbot_sendMessage("Better luck next time!")
    saveData()

#slotList = ['🔟','💯','👩','👯','💪'] 
slotList = ['\U0001f51f','\U0001F4AF','\U0001F469', '\U0001F46F', '\U0001F4AA']
slotLen = len(slotList) - 1
def jc_slot():
    checkUser()
    if (cashDB[userList[1]][0] < 5):
        jcbot_sendMessage("Insufficient Funds...")
        return
    payline = int(argsList[1]); payout = 0;
    cashDB[userList[1]][0] -= 5
    for x in range(3):
        a = random.randint(0,slotLen)
        b = random.randint(0, slotLen)
        c = random.randint(0, slotLen)
        jcbot_sendMessage(slotList[a]+ ' ' + slotList[b] + ' ' + slotList[c])
        if ( a == b == c and payline == x + 1):
            payout = 1
    if (payout == 1):
        jcbot_sendMessage("JACKPOT!")
        cashDB[userList[1]][0] += 1000
    saveData()

    
builtins.commands["roulette"] = jc_roulette
builtins.commands["slot"] = jc_slot

builtins.commands["balance"] = jc_balance
builtins.commands["paycheck"] = jc_paycheck
