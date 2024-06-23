# Youtube Link: https://www.youtube.com/watch?v=PgLjwl6Br0k

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd
import matplotlib.pyplot as plt 

# initalise the tkinter GUI
root = tk.Tk()

root.geometry("400x400") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.
root.configure(bg='white')
root.title("Welcome to Company Results App")
# Frame for TreeView
frame1 = tk.LabelFrame(root, text=" Company Results")
frame1.place(height=40, width=400)
frame1.configure(bg='red')
# Frame for open file dialog
choose_frame = tk.LabelFrame(root, text="Choose your Company Results")
choose_frame.place(height=400, width=400, rely=0.8, relx=0)
choose_frame.configure(bg='light blue')
# Buttons
button1 = tk.Button(choose_frame, text="CProf", command=lambda: CompProfitsMonthly())
button1.place(rely=0.100, relx=0.10)

button2 = tk.Button(choose_frame, text="Lplot", command=lambda: LineCompProfMont())
button2.place(rely=0.100, relx=0.20)

button3 = tk.Button(choose_frame, text="AlPdSale", command=lambda: AllProductSales())
button3.place(rely=0.100, relx=0.40)

button4 = tk.Button(choose_frame, text="TpSaleScat", command=lambda: TpSaleScat())
button4.place(rely=0.100, relx=0.60)

button5 = tk.Button(choose_frame, text="FC_FW_BaCh", command=lambda: FC_FW_BarChart())
button5.place(rely=0.100, relx=0.80)

#button6 = tk.Button(choose_frame, text="Jaguar only", command=lambda: Load_JAGUAR())
#button6.place(rely=0.50, relx=0.10)

## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


def CompProfitsMonthly():
    
    df = pd.read_csv("D:\\Python\\company_sales_data.csv")
    profitList = df ['total_profit'].tolist()
    monthList  = df ['month_number'].tolist()
    plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
    plt.xlabel('Month number')
    plt.ylabel('Profit in dollar')
    plt.xticks(monthList)
    plt.title('Company profit per month')
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()
    return None

def LineCompProfMont():
    
    df = pd.read_csv("D:\\Python\\company_sales_data.csv")
    profitList = df ['total_profit'].tolist()
    monthList  = df ['month_number'].tolist()
    plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k',linestyle='--', linewidth=3)   
    plt.xlabel('Month Number')
    plt.ylabel('Profit in dollar')
    plt.legend(loc='lower right')
    plt.title('Company Sales data of last year')
    plt.xticks(monthList)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()
    return None

def AllProductSales():
    
    df = pd.read_csv("D:\\Python\\company_sales_data.csv")
    monthList  = df ['month_number'].tolist()
    faceCremSalesData   = df ['facecream'].tolist()
    faceWashSalesData   = df ['facewash'].tolist()
    toothPasteSalesData = df ['toothpaste'].tolist()
    bathingsoapSalesData   = df ['bathingsoap'].tolist()
    shampooSalesData   = df ['shampoo'].tolist()
    moisturizerSalesData = df ['moisturizer'].tolist()

    plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
    plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, bathingsoapSalesData, label = 'Bathing Soap Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, shampooSalesData, label = 'Shampoo Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, moisturizerSalesData, label = 'Moisturizer Sales Data', marker='o', linewidth=3)

    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.xticks(monthList)
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.title('Sales data')
    plt.show()
    return None

def TpSaleScat():
    
    df = pd.read_csv("D:\\Python\\company_sales_data.csv")
    monthList  = df ['month_number'].tolist()
    toothPasteSalesData = df ['toothpaste'].tolist()
    plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
    plt.xlabel('Month Number')
    plt.ylabel('Number of units Sold')
    plt.legend(loc='upper left')
    plt.title(' Tooth paste Sales data')
    plt.xticks(monthList)
    plt.grid(True, linewidth= 1, linestyle="--")
    plt.show()
    return None 

def FC_FW_BarChart():
    
    df = pd.read_csv("D:\\Python\\company_sales_data.csv")
    monthList  = df ['month_number'].tolist()
    faceCremSalesData   = df ['facecream'].tolist()
    faceWashSalesData   = df ['facewash'].tolist()

    plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
    plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.title(' Sales data')

    plt.xticks(monthList)
    plt.grid(True, linewidth= 1, linestyle="--")
    plt.title('Facewash and facecream sales data')
    plt.show()
    return None

def clear_data():
    tv1.delete(*tv1.get_children())
    return None


root.mainloop()
