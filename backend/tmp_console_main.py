#!/usr/bin/python3
""" console """

import cmd
from sqlalchemy.orm import Session
from app.core import crud 
from app.core.database import SessionLocal
from datetime import datetime
from app.models.base_model import BaseModel
from app.models.users import User
from app.models.hospitals import Hospital
from app.models.blood_banks import BloodBank
from app.models.blood_types import BloodType
from app.models.hospitals_Inventory import HospitalInventory
from app.models.bloodBanks_Inventory import BankInventory
from app.models.blood_requests import Request
from app.models.transactions import Transaction

import shlex  # for splitting the line along spaces except in double quotes

db = SessionLocal()

classes = {"User": User, "BaseModel": BaseModel, "Hospital": Hospital,
        "BloodBank": BloodBank, "BloodType": BloodType, "HospitalInventory": HospitalInventory,
        "BankInventory": BankInventory, "Request": Request, "Transaction": Transaction}


class BloodSync(cmd.Cmd):
    """ HBNH console """
    prompt = '(bloodsync) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg, db: Session = db):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        crud.save(instance)
        print(instance.id)

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]                
                if key in crud.all():                    
                    print(crud.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in crud.all():
                    try:
                        x = crud.all()[key]
                        db.delete(x)
                    except Exception as e:
                        print(e)
                    # print("\n\n\n\nOne\n\n\n\n")
                    db.commit()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = crud.all()
        elif args[0] in classes:
            obj_dict = crud.all(args[0])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in crud.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            obj = crud.all()[k]
                            obj2 = obj.__dict__
                            # print(obj.__dict__)
                            found = False
                            for key, value in obj2.items():
                                # print(key)
                                if args[2] == key:
                                    setattr(obj, args[2], args[3])
                                    found = True
                                    break
                            if not found:
                                print("No attr found.")                            
                            crud.save(obj)
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    BloodSync().cmdloop()
