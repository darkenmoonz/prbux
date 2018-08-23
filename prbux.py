import webbrowser

def boatLink():
    webbrowser.open('https://www.youtube.com/watch?v=WCBM5LVbSmY')
    welcome()

def Rolimons():
    webbrowser.open('https://www.rolimons.com/deals')
    welcome()

def mainCalc():
    print('Price of the item')
    itemprice = int(input())
    print(itemprice)
    print('Your selling price')
    sellprice = int(input())
    print(sellprice)
    percentagethrowaway = sellprice * .3
    percentageprice = sellprice - percentagethrowaway
    profit = percentageprice - itemprice
    percenthalfthrow = percentagethrowaway / 2
    percentthreethrow = percentagethrowaway / 3
    print(profit)
    print('--------------------')
    print('Sales Robot recommends...')
    if profit >= percentagethrowaway:
        print('BUY! Sales Robot says: Because of the fact that profit, ', profit, ', is bigger than percentagethrowaway, ', percentagethrowaway, ' this item seems like a good purchase.')
    elif profit <= 1:
        print('DO NOT BUY! Sales Robot strongly recommends that you do not buy this item, the deficit would be very large! Profit: ', profit)
    elif profit <= percenthalfthrow and profit >= percentthreethrow:
        print('Buy with caution. The return on investment would be around 33 - 50% since profit, ', profit, ' is in between percentagethrowaway divided by 2 ', percenthalfthrow, ' and percentagethrowaway divided by 3, ', percentthreethrow, ' The percentagethrowaway is, ', percentagethrowaway)
    elif profit <= percentagethrowaway:
        print('Consider. Sales Robot says: Because of the fact that profit, ', profit, ', is smaller than percentagethrowaway, ', percentagethrowaway, ' this item seems like a risky purchase.')

    welcome()
              
def welcome():
    #prrobux v1 8/19/18
    print('--------------------')
    print("Welcome to PRBUX")
    welcomelist = ["Calculate = 1 Rolimon's = 2 3 = Make a boat in Roblox Studio"]
    print(welcomelist)
    goto = int(input())
    print(goto)
    if goto == 1:
        mainCalc()
    elif goto == 2:
        Rolimons()
    elif goto == 3:
        boatLink()
    elif goto >= 4:
        print(goto)
        return "invalid function"
        welcome()
    #main

        
welcome()
