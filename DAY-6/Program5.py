#Log file analyser : read a log , count error types
with open("log.txt" , "w") as file :
     file.write("ERROR\n")
     file.write("WARNING\n")
     file.write("ERROR\n")
     file.write("INFO\n")
     file.write("ERROR\n")
     file.write("WARNING\n")
     cursor = file.seek(0)
print("Log file created! ")
error_count = 0
warning_count = 0
info_count = 0
with open("log.txt" , "r" ) as file :
     for line in file :
          if line.strip() == "ERROR" :
            error_count += 1
          elif line.strip() == "WARNING" :
            warning_count += 1
          elif line.strip() == "INFO" :
              info_count += 1
print("ERROR =" , (error_count))
print("WARNING " , (warning_count))
print("INFO " , (info_count))