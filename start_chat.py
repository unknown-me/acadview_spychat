# start_chat
import os;
from default_details import status_msg;
def old_status ():
	next_status	=	"Y";
	current_choice	=	0;
	i=0;
	print ("Press\n1. 0 to exit anytime.\n2. A to see all msgs.");
	raw_input ("Press anything to continue...");
	os.system ("cls");
	for	i	in		status_msg:
		next_status	=	raw_input("Want to see next msg(Y/N/A/0): ");
		print (i);
		if (next_status	==	'Y'	or	next_status	==	'y'):
			print (str(i+1)+". "+str(status_msg[i])+".");
			i=i+1;
			continue;
		elif (next_status	==	"A"	or	new_status	==	"a"):
			os.system("cls");
			for	temp	in		status_msg:
				i=0;
				print (str(i+1)+". "+str(status_msg[i])+".");
				i=i+1;
			current_choice	=	int(raw_input("\nPlz enter ur choice(Press 0 to enter new status): "));
			break;
		elif (next_status	==	'N'	or	next_status	==	'n'):
			print ("\n\nEnter 0 if dont want to see further msgs and want to enter new status otherwise choose from above msgs: ");
			current_choice	=	int(raw_input("Plz enter ur choice: "));
		elif (int(next_status)	==	0):
			pass;
		else:
			print ("\n\nPlz Enter valid choice(Y/N/A/0): ");
			i=i-1;
	else:
		print("\nEnd of the list.");
		current_choice	=	int(raw_input("Plz Enter your choice(Press 0 to enter new status): "));
	if (current_choice	!=	0):
		while (len(status_msg)<current_choice):
			print ("Plz Enter valid choice: ");
		print ("Ur status has been updated to: "+status_msg[current_choice-1]);
		return False;
	else:
		os.system ("cls");
		return True;
		
def new_status (new_status):
	while(new_status	==	""):
		print ("U haven't entered anything.");
		new_status =	raw_input("Enter Ur Status msg: ");
	add_to_saved	=	raw_input ("U want to save this msg?(Y/N):");
	while (add_to_saved	!=	'N'	and	add_to_saved	!=	'n'	and	add_to_saved	!=	'Y'	and	add_to_saved	!=	'y'):
		print ("Plz Enter valid choice: ");
		add_to_saved	=	raw_input ("U want to save this msg?(Y/N): ");
	if (add_to_saved	==	'Y'	or	add_to_saved	==	'y'):
		status_msg.append(new_status);
		print ("Ur status has been saved.")
	print ("\nUr status has been updated to: "+new_status);
		
def start_chat(name,	age,	rating):
	menu_string	=	"Enter ur choice:\n\n1.Update status.\n9.Exit\n\n";
	menu_choice	=	int(raw_input(menu_string));
	my_status	=	"";
	choice	=	"Y";
	o_t_n	=	False;
	show_menu	=	True;
	while(show_menu):
		if (menu_choice	==	1):
			choice	=	raw_input("U want to use old status msgs(Y/N): ");
			while (choice	==	"N"	or	choice	==	"n"	or	choice	==	"Y"	or	choice	==	"y"):
					if (choice	==	'Y'	or	choice	==	'y'):
						o_t_n	=	old_status();
						if (o_t_n):
							my_status	=	raw_input("Plz enter status u want to update:");
							new_status(my_status);
						break;
					else:
						my_status	=	raw_input("Plz enter status u want to update:");
						new_status(my_status);
						break;
			else:
				print ("Plz Enter valid choice: ");
				choice	=	raw_input ("U want to use old status msgs(Y/N): ");
			
			raw_input ("Press anything to continue...");
			print (menu_string);
			menu_choice	=	int(raw_input(menu_string));
		elif (menu_choice == 9):
			print ("Exiting...");
			show_menu	=	False;
		else:
			print ("Plz enter valid choice");
			menu_choice	=	int(raw_input(menu_string));
		
			
start_chat("abc",	12,	0);