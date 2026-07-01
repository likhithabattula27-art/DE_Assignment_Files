#Q10. Transaction File Processor
#Create a file named transactions.txt containing transaction amounts.
#Read the file and:
#- Print all transaction amounts
#- Calculate total transaction value
#- Handle any file-related exceptions using try-except
f = open("transactions.txt", "w")
f.write("1500\n")
f.write("2300.50\n")
f.write("999\n")
f.write("4500.75\n")
f.write("1200\n")
f.close()
 
try:
    f = open("transactions.txt", "r")
    total = 0
    for line in f:
        amt = float(line.strip())
        print("Transaction:", amt)
        total = total + amt
    f.close()
    print("Total transaction value:", total)
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("File has some invalid data")