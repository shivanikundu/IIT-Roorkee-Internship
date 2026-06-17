#CSV grade sheet : read marks , compute average , write results
import csv
with open("marks.csv" , "w+" , newline = "") as file :
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Varsha", 85])
    writer.writerow(["Rahul", 90])
    writer.writerow(["Aman", 75])

    cursor = file.seek(0)
    print("CSV file created!")
    total = 0
    count = 0
    reader = csv.reader(file)
    next(reader)  #skip header
    for row in reader :
      total += int(row[1])
      count += 1
average = total / count
import csv
with open("result.txt" , "w") as file :
      file.write("Average Marks = " + str(average))
print("Average = " , average)