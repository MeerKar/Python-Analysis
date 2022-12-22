import os
import csv
data_path=os.path.join('Resources','budget_data.csv')

total_months=0
total_profit_loss=0
value = 0
change = 0
dates = []
profits = []
with open(data_path, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months +=1
    total_profit_loss += int (first_row[1])
    value = int(first_row[1])

    for row in csvreader:

        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        total_months +=1
        total_profit_loss=total_profit_loss + int(row[1])

        avg_change = sum(profits)/len(profits)


        greatest_increase = max(profits)
        greatest_inc_index = profits.index(greatest_increase)
        greatest__inc_date = dates[greatest_inc_index]

        greatest_decrease = min(profits)
        greatest__dec_index = profits.index(greatest_decrease)
        greatest__dec_date = dates[greatest__dec_index]

        printoutput = (
            f"Financial Analysis\n"
            f"------------------------------------\n"
            f"Total Months: {str(total_months)}\n"
            f"Total: ${str(total_profit_loss)} \n"
            f"Average Change: ${str(round(avg_change,2))}\n"
            f"Greatest Increase in Profits: {greatest__inc_date}(${str(greatest_increase)})\n"  

            f"Greatest decrease in Priofit: {greatest__dec_date}(${str(greatest_decrease)})\n") 

        print(printoutput)

output_file = os.path.join('Analysis', 'pyBank_output.txt')

pybankoutput = open(output_file, "w")

line1 = "Financial Analysis"
line2 = "------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Average Change: ${str(round(avg_change,2))}")
line5 = str(f"Greatest Increase in Profits: {greatest__inc_date}($${str(greatest_increase)})")
line6 = str(f"Greatest Decrease in Profits: {greatest__dec_date}($${str(greatest_increase)})")

pybankoutput.write('{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6))

     
