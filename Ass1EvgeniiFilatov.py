# autor Evgenii Filatov
# 21F_CST8333_350 

import csv
import sys


fileVac = "vaccination-coverage-byVaccineType.csv"
# create class for reading csv-file 
class VaccineCoverage(): 
    #  create constructor for the table
    def __init__(self, pruid = "", prename = "", prfname = "", week_end = "", product_name = "", 
                numtotal_atleast1dose = "", numtotal_partially = "", numtotal_fully = "",
                prop_atleast1dose = "", prop_partially = "", prop_fully = ""):
            self._pruid = pruid
            self._prename = prename
            self._prfname = prfname
            self._week_end = week_end 
            self._product_name = product_name 
            self._numtotal_atleast1dose = numtotal_atleast1dose 
            self._numtotal_partially = numtotal_partially 
            self._numtotal_fully = numtotal_fully 
            self._prop_atleast1dose = prop_atleast1dose
            self._prop_partially = prop_partially
            self._prop_fully = prop_fully

    # This method is similar to method toString in Java. Create output format.    
    def __repr__(self):
        return "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}".format(
            self._pruid,self._prename,self._prfname,
            self._week_end,self._product_name,
            self._numtotal_atleast1dose,self._numtotal_partially,
            self._numtotal_fully,self._prop_atleast1dose,
            self._prop_partially,self._prop_fully)

    #This method is similar to public static void main in Java
def main(): 

    # Open file and handle exceptions if file does not exist or has error. 
    try: 
        file = open(fileVac)
    except FileNotFoundError:
        print("The file does not exists.")
    except IOError:
        print("Problem opening file.")
        sys.exit()

    # Create arrays for records of the table  and headers

    vaccineRecords = []
    csvreader = csv.reader(file)
    tableHeaders = next(csvreader)
    listOfHeaders = []

    # This is a loop  for list of headers for 11 columns
    for i in range(0, 10):
        listOfHeaders.append(tableHeaders[i])
        
    print('|'.join(listOfHeaders))
    
    # This is a loop  reading first 100 records from the csv-file.
    for row in csvreader:
        vaccineRecord = VaccineCoverage(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        vaccineRecords.append(vaccineRecord)
        if len(vaccineRecords) == 100:
            break

    for record in vaccineRecords:
        print(record)
    # file output
    file.close()

if __name__ == "__main__":
    main()