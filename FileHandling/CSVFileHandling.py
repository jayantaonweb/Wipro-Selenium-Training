import csv
with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//Data.csv",'r')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing to the csv file
with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//writecsv.csv",'w',newline="") as  file:
    writer=csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1,"Rahul",85])
    writer.writerow([2,"Anita",95])


#append to csv file
with open("C://Users//jkpja//PycharmProjects//Python Advance Programing//DataFormats//Data.csv",'a',newline="")as file:
    writer=csv.writer(file)
    writer.writerow([4, "Amit", 85])
    writer.writerow([5, "Rohit", 55])