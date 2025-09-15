import random
def lower(name):
    name_list = list(name)
    new_name_list = []
    for letter in name_list:
        int_value = ord(letter)
        if int_value < 90 and int_value > 64:
            new_int_value = int_value+32
            lower_letter = chr(new_int_value)
            new_name_list.append(lower_letter)
        else:
            already_lower_letter = chr(int_value)
            new_name_list.append(already_lower_letter)
    return("".join(new_name_list))
    

def upper(name):
    name_list = list(name)
    new_name_list = []
    for letter in name_list:
        int_value = ord(letter)
        if int_value > 96 and int_value < 122:
            new_int_value = int_value-32
            higher_letter = chr(new_int_value)
            new_name_list.append(higher_letter)
        else:
            already_higher_letter = chr(int_value)
            new_name_list.append(already_higher_letter)
    return("".join(new_name_list))     
            




def vowel_count(lower_or_upper_name):
    name = lower(lower_or_upper_name)
    name_list = list(name)
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_name = 0

    for letter in name_list:
        if letter in vowels:
            vowels_in_name += 1
    print(f'There are {vowels_in_name} vowels in this name')

def constanant_count(lower_or_upper_name):
    name = lower(lower_or_upper_name)
    name_list = list(name)
    vowels = ["a", "e", "i", "o", "u"]
    constanant_in_name = 0

    for letter in name_list:
        if letter not in vowels:
            constanant_in_name += 1
    print(f'There are {constanant_in_name} constanants in this name')

def first_name(name):
    name_list = list(name)
    counter = 0
    if " " in name_list:
        for letter in name_list:
            if letter == " ":
                break
            else:
                counter = counter + 1
        first_name_list = name_list[0:counter]
        first_name_string = "".join(first_name_list)
        return first_name_string
    else:
        return("Theres only 1 word in name so unable to run this function")

def reverse(name):
    return name[::-1]

def hyphen_check(name):
    for letter in name:
        if "-" in name:
            return True
            break
        else:
            return False
def last_name(name):
    name_list = list(name)
    if " " in name_list:
        backwards_name = reverse(name)
        backwards_last_name = first_name(backwards_name)
        last_name = reverse(backwards_last_name)
        return last_name
    else:
        return("There's only 1 word in name so unable to run this function")


def middle_name(name):
    name_list = list(name)
    space_counter = 0
    for letter in name:
        if letter == " ":
            space_counter += 1
    if space_counter > 1:
        for i in name:
            if i == " ":
                name_list.remove(i)
                break
            else:
                name_list.remove(i)
        first_name_removed = "".join(name_list)
        fnr_reversed = reverse(first_name_removed)
        fnr_reversed_list = list(fnr_reversed)
        for letter in fnr_reversed_list:
            if letter == " ":
                fnr_reversed_list.remove(letter)
                break
            else:
                fnr_reversed_list.remove(letter)
        fnrlnr_reversed = "".join(fnr_reversed_list)
        fnrlnr = reverse(fnrlnr_reversed)
        return fnrlnr
        
        
        



    else:
        print('There is no middle name')


def titles(name):
    titles = ["Dr."]
    first_part_of_name = first_name(name)
    if first_part_of_name in titles:
        return True
    else:
        return False



def shuffle(name):
    pass
        
 






        
            
        

        

def main():
    while True:
        users_name = input("What's your name?")
        menu = input(
    """
                                    MENU
    1. Detect how many vowels are in the name
    2. Which part of the name is the first name
    3. Which part of the name is the last name
    4. Reverse name
    5. Detect how many constanants are in the name
    6. Detect if there is a hyphen in the name
    7. Make all characters in name lower
    8. Which part of the name is the middle name
    9. Make all characters in name capitilized
    10. Test if it is a palindrome
    11. Shuffle name
    """       
        )
        if menu == "1":
            vowel_count(users_name)
        elif menu =="2":
            print(first_name(users_name))
        elif menu == "3":
            print(last_name(users_name))
        elif menu == "4":
            print(reverse(users_name))
        elif menu == "5":
            constanant_count(users_name)
        elif menu == "6":
            if hyphen_check(users_name) == True:
                print('there is a hyphen in the name')
            else:
                print('there is not a hyphen in the name')
        elif menu == "7":
            print(lower(users_name))
        elif menu == "8":
            print(middle_name(users_name))
        elif menu == "9":
            print(upper(users_name))
        elif menu == "10":
            if users_name == reverse(users_name):
                print('it is a palindrome')
            else:
                print('it is not a palindrome')
        elif menu == "11":
            print(shuffle(users_name))
        
        else:
            print('not an option(type number(1, 2, etc)')

main()

