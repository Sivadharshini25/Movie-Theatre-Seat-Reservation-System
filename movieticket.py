import os
import mysql.connector as sqltor
def welcome():
 # the function that asks the user for a choice and responds 
accordingly.
 print('Enter,')
 print('1, to add details of a ticket booking to the database.')
 print('2, to update details of ticket booking.')
 print('3, to remove record(s) of ticket booking.')
 print('4, to display required data.')
 print('5, to exit the window.')
 while True:
 ch = int(input('Enter your choice:'))
 if ch == 1:
 m_choice1()
 elif ch == 2:
 m_choice2()
 elif ch == 3:
 m_choice3()
 elif ch == 4:
 m_choice4()
 elif ch == 5:
 os._exit(ch == 6)
 else:
 print('Please do enter a valid choice (1 to 6):',)
def m_rowcount():
 # returns the total number of rows in the movies table eveytime 
it is called.
 cursor.execute('select * from ticket_booking')
 count = cursor.rowcount
 print("Total number of movies ticket_booking records:",count)
def m_choice1():
 # gets the values from the user at run time and inserts the record 
into the ticket booking table.
 m_rec = []
 n = int(input('How many records do you want to add?'))
 for i in range(n):
 print('Record', i+1)
 t_no = int(input('Enter the ticket no:'))
 a_no = int(input('Enter the audi no:'))
 m_name = input("Enter the movie name:")
 n_seat= int(input("Enter the no of seats:"))
 t_price = int(input("Enter the ticket price:"))
 s_timings = (input("Enter the show timings:"))
 m_rec.append([t_no, a_no, m_name, n_seat, t_price, 
s_timings,])
 print()
 ins_query = "insert into ticket_booking values(%s, %s, %s,%s, 
%s, %s)"
 cursor.executemany(ins_query, m_rec)
 con.commit()
 print('Records inserted successfully.')
 m_rowcount()
 tablemenu_or_quit()
def m_choice2():
 # the function called when the update choice is selected. This 
calls the update function defined separately.
 cond = True
 while cond:
 print('Do you want to update:')
 print("1.Ticket no")
 print("2,Audi_no")
 print("3.Movie name")
 print("4.No of seats")
 print("5.Ticket price")
 print("6.Show timings")
 update_choice = int(input('Enter your choice:'))
 update(update_choice)
 print('Record updated successfully.')
 m_rowcount()
 user_cont = input('Do you want to update more records? 
[y/n]')
 if user_cont == 'y' or user_cont == 'Y':
 cond = True
 else:
 break
 tablemenu_or_quit()
def update(update_choice):
 # takes any column from the reservation table in general and 
updates one column at a time.
 if update_choice in range(1,7):
 update_col = mtable_col[update_choice-1]
 else:
 print('Enter a valid choice (1 to 6):')
 m_old = input('Enter the existing ' + update_col + ':')
 t = type(m_old)
 m_new = t(input('Enter the new ' + update_col + ':'))
 condn = input(
 'Enter conditions, if any, using the column names t_no, a_no, 
m_name, n_seat, t_price, s_timing. ')
 if condn == '':
 if t == str:
 update_query = 'update ticket_booking set ' + update_col 
+ \
 ' = "{mn}" where '.format(
 mn=m_new) + update_col + ' = "{mo}"' 
.format(mo=m_old)
 else:
 update_query = 'update ticket_booking set ' + update_col 
+ \
 ' = {mn} where '.format(mn=m_new) + \
 condn + ' = {mo}' .format(mo=m_old)
 else:
 if t == str:
 update_query = 'update ticket_booking set ' + update_col 
+ \
 ' = "{mn}" where '.format(
 mn=m_new) + condn + ' = "{mo}"' 
.format(mo=m_old) + ' and ' + condn
 else:
 update_query = 'update ticket_booking set ' + update_col 
+ \
 ' = {mn} where '.format(mn=m_new) + \
 condn + ' = {mo}' .format(mo=m_old) + ' and ' + condn
 cursor.execute(update_query)
 con.commit()
def m_choice3():
 # this function removes required records from the 
ticket_booking table.
 cond = True
 while cond:
 remove_col = int(
 input('Enter the Ticket_no whose record is to be 
removed:'))
 remove_query = 'delete from ticket_booking where t_no = 
%s' % (
 remove_col)
 cursor.execute(remove_query)
 con.commit()
 print('Record removed successfully.')
 m_rowcount()
 user_cont = input('Want to delete more rows? [y/n]')
 if user_cont == 'y' or user_cont == 'Y':
 cond = True
 else:
 break
 tablemenu_or_quit()
def m_choice4():
 # d_choice4(): this function queries data from the table and 
displays it in the Python output screen.
 cond = True
 while cond:
 condn = input(
 'Enter conditions, if any, using the column names t_no, 
a_no, m_name, n_seat, t_price, s_timing.')
 if condn == '':
 select_query = "select * from ticket_booking"
 else:
 select_query = "select * from ticket_booking where " + 
condn
 cursor.execute(select_query)
 data = cursor.fetchall()
 for i in data:
 print(i)
 cont = input('Do you want to access a different set of data? 
[y/n]')
 if cont == 'y' or cont == 'Y':
 cond = True
 else:
 break
 tablemenu_or_quit()
def tablemenu_or_quit():
 # This function applies to all the modules defined for each 
table.
 # The user of the program has an option to go back to the 
respective table's menu, or quit the window then and there.
 back = input('Enter y to go back to the movie menu, or n to 
quit.')
 if back.lower() == 'y':
 welcome()
 else:
 os._exit(back.lower() == 'n')
# main
con = 
sqltor.connect(host='localhost',username='Root_',password='1234
5678',database='cs_project')
cursor = con.cursor(buffered=True)
mtable_col = ['t_no', 'a_no', 'm_name', 'n_seat', 't_price', 
's_timing']
print('\t*****TICKET BOOKING*****')
m_rowcount()
print()
welcome()
con.close()
