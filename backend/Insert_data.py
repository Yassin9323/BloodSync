#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil
import os
import random
import time


print("Loading Data... ")
"""
 Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")


"""
 Updating console to remove "__main__"
"""
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    ")) 
            else:
                file_o.write(line)

import console


"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False


"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

"""
Tests
"""
print("5")
# Create 4 Hospitals
hospitals = [
    {"name": "Cairo-Hospital", "address": "Cairo-Governate", "contact_number": "045242"},
    {"name": "Giza-Hospital", "address": "Cairo-Governate", "contact_number": "0223242"},
    {"name": "AinShams-Hospital", "address": "Cairo-Governate", "contact_number": "067242"},
    {"name": "Helwan-Hospital", "address": "Cairo-Governate", "contact_number": "09823242"}
]
hospital_ids = []
for hospital in hospitals:
    hospital_id = exec_command(my_console, f'create Hospital name="{hospital["name"]}" address="{hospital["address"]}" contact_number="{hospital["contact_number"]}"')
    if hospital_id is None or hospital_id == "":
        print(f'FAIL: Can\'t create {hospital["name"]}')
    hospital_ids.append(hospital_id)


# Create Cairo_BloodBank
cairo_bloodbank_id = exec_command(my_console, 'create BloodBank name="Cairo-BloodBank" address="Cairo-Governate" contact_number="05556823242"')
if cairo_bloodbank_id is None or cairo_bloodbank_id == "":
    print("FAIL: Can't create Cairo_BloodBank")


print("4")
# Create 8 BloodTypes
blood_types = ['A+', 'B+', 'AB+', 'A-', 'B-', 'AB-', 'O+', 'O-']
blood_type_ids = []
for blood_type in blood_types:
    blood_type_id = exec_command(my_console, f'create BloodType type="{blood_type}"')
    if blood_type_id is None or blood_type_id == "":
        print(f'FAIL: Can\'t create {blood_type}')
    blood_type_ids.append(blood_type_id)


print("3")
# Create Inventories for each hospital and each blood type
inventory_ids = []
for hospital_id in hospital_ids:
    for blood_type_id in blood_type_ids:
        num = random.randint(1, 10)
        inventory_id = exec_command(my_console, f'create HospitalInventory units="{num}" hospital_id="{hospital_id}" blood_type_id="{blood_type_id}"')
        if inventory_id is None or inventory_id == "":
            print(f'FAIL: Can\'t create HospitalInventory for hospital_id={hospital_id} and blood_type_id={blood_type_id}')
        inventory_ids.append(inventory_id)
        
        
print("2")
# Create Inventory for the Cairo Blood Bank and each blood type
bank_inventory_ids = []
for blood_type_id in blood_type_ids:
    num = random.randint(20, 50)
    bank_inventory_id = exec_command(my_console, f'create BankInventory units="{num}" bank_id="{cairo_bloodbank_id}" blood_type_id="{blood_type_id}"')
    if bank_inventory_id is None or bank_inventory_id == "":
        print(f'FAIL: Can\'t create BankInventory for bank_id={cairo_bloodbank_id} and blood_type_id={blood_type_id}')
    bank_inventory_ids.append(bank_inventory_id)
    
    
print("1")
# Create 4 requests for each hospital 
req_units = []
request_ids= []
x = 0
for hospital_id in hospital_ids:
    num = random.randint(1, 10)
    req_units.append(num)
    request_id = exec_command(my_console, f'create Request blood_type_id="{blood_type_ids[x]}" units="{num}" hospital_id="{hospital_id}" blood_bank_id="{cairo_bloodbank_id}"')
    if request_id is None or request_id == "":
        print(f'FAIL: Can\'t create request for hospital_id="{hospital_id}" and blood_type_id="{blood_type_ids[x]}"')
    request_ids.append(request_id)
    x= x+1
    
    
# Create Transaction 
for x in range(len(request_ids)-1):
    
    trancsaction = exec_command(my_console, f'create Transaction units="{req_units[x]}" from_id="{cairo_bloodbank_id}" to_id="{hospital_ids[x]}" request_id="{request_ids[x]}"')
    U_status = exec_command(my_console, f'update Request {request_ids[x]} status approved')
    time.sleep(1)

print("\nData Loaded Sucessfully :) \n")

shutil.copy("tmp_console_main.py", "console.py")

# 8ca4f59b-1e69-4ce8-ad50-67a5376a49cc ---------Hospital 
# 4adfc814-6616-4e56-b1f5-bd6a84638ec5 ---------AB+
# from_inv_id="" to_inv_id="" request_id=""



# 0c040ccd-ca88-49cf-bc61-96bbf1b6072c ---------BloodBank