import csv
with open('csv_m.csv','w',newline='') as i:
    details=csv.writer(i)
    details.writerow(['name','id','collegename','group'])

    for c in range(2):
        name=input('enter student name:- ')
        id=input('enter student id:- ')
        collegename=input('enter student college name:- ')
        group=input('enter student group:- ')
        details.writerow([name,id,collegename,group])