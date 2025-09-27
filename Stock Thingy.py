import yfinance as yf
import matplotlib.pyplot as plt
from windows_toasts import WindowsToaster,Toast
import time

def investment_mode(a):
   import sys
   portfolio = {}
   total_portfolio = 0
   profit_loss = 0
   print("Stock      Shares      Buying Price      Current Price      p/l")
   print("---------------------------------------------------------------")
   for i in a: 
      shares = int(input("How many shares of %s you own? "%i)) 
      sys.stdout.write('\033[1A\033[K') #stolen from stackoverflow , Idfk how this works
      sys.stdout.flush()  #\033[1A moves cursor up 1 line , \033[K select from cursor to end and flush() clears the console from selected cursor
      buying_price = float(input("What is your buying price for %s? "%i))
      sys.stdout.write('\033[1A\033[K')
      sys.stdout.flush()   
      portfolio[i] = shares
      ticker = yf.Ticker(i)
      data = ticker.history(period="1d")
      current = float(data["Close"].iloc[-1])
      total_portfolio += current*portfolio[i]
      profit_loss += (buying_price-current) *shares
      print("%s         %d        %f        %.6f     %f" %(i,shares,buying_price,current,profit_loss))
   print("---------------------------------------------------------------")
   print("Current portfolio price: $%f"%total_portfolio)
   print("Current profit/loss: $%f" %profit_loss)

def csv_stuff(data):
   csv_option = input("Do you want to print out a CSV file? y/n: ")
   match csv_option:
      case "y":
        with open("Table.csv","w",encoding="UTF-8",newline = "") as file:
         data.to_csv(file)
      case "n":
         restart()

def live_noti(a,b):
   columbia,alert_threshold = input("Alert me if %s goes (above/below) (price): "%b).split()
   alert_threshold = float(alert_threshold)
   match columbia:
      case "above":
         while True:
          data = a.history(period="1d")
          current = float(data["Close"].iloc[-1])
          print("Current %s price: %f" %(b,current))
          if alert_threshold < current:
               in_yo_face = WindowsToaster("Stock tracking script")
               bread = Toast() 
               bread.text_fields = ["%s is above %.6f currently at: %.6f!!!" %(b,alert_threshold,current)]
               in_yo_face.show_toast(bread)
          time.sleep(60)
      case "below":
         while True:
          data = a.history(period="1d")
          current = float(data["Close"].iloc[-1])
          print("Current %s price: %f" %(b,current))
          if alert_threshold > current:
               in_yo_face = WindowsToaster("Stock tracking script")
               bread = Toast() 
               bread.text_fields = ["%s is below %.6f currently at: %.6f!!!" %(b,alert_threshold,current)]
               in_yo_face.show_toast(bread)
          time.sleep(60)
            

def restart():
   real = input("Restart the application? (y/n): ")
   match real:
      case "y":
         __init__()
      case "n":
         quit()
      case _:
         print("Wrong input!!!!!")
         restart()
      
def __init__():
   user_input = input("Input stock symbol(s) (eg.MSFT, META): ").split(",")
   stock = yf.Tickers(user_input)
   option = input("Do you want to graph data? (y/n) live notification function? (live) or track your portfolio? (invest): ")
   match option:
      case"invest":
         investment_mode(user_input)
      case "y":
         thingy = input("What time period do you want as data? (eg. 1d/1mo/1y): ")
         data = stock.history(period=thingy)
         magic = input("What data(s) do you want to present? (Close,Open,Low,High): ").split(",")
         comprehended_magic = list(map(lambda item:item.capitalize(),magic))
         data[comprehended_magic].plot(title="%s prices(Last %s)" % (comprehended_magic,thingy) ,lw= 2)
         plt.show()
         csv_stuff(data)
      case "n":
         thingy = input("What time period do you want as data? (d/mo/y): ")
         data = stock.history(period=thingy)
         csv_stuff(data)
      case "live":
         live_noti(stock,user_input)
      case _:
         print("Invalid output")
         __init__()

__init__()






    


            
        