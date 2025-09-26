import random
def lower(name):
    '''
    turns each character into a lowercase letter if it is not already
    args:
        name(str)
    output:
        name fully lowercase (str)
    '''
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
    '''
    turns each character into a uppercase letter if it is not already
    args:
        name(str)
    output:
        name fully uppercase (str)
    '''
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
    '''
    Counts the amount of vowels in your name and returns this

    Args:
    name(str)

    Returns:
    The amount of vowels in the name(str)
    '''
    name = lower(lower_or_upper_name)
    name_list = list(name)
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_name = 0

    for letter in name_list:
        if letter in vowels:
            vowels_in_name += 1
    print(f'There are {vowels_in_name} vowels in this name')

def constanant_count(lower_or_upper_name):
    '''
    Counts the amount of constanants in your name and returns this

    Args:
    name(str)

    Returns:
    The amount of constanants in the name(str)
    '''
    name = lower(lower_or_upper_name)
    name_list = list(name)
    vowels = ["a", "e", "i", "o", "u"]
    constanant_in_name = 0

    for letter in name_list:
        if letter not in vowels:
            constanant_in_name += 1
    print(f'There are {constanant_in_name} constanants in this name')

def first_name(name):
    '''
    Detects where the first space in the name is and returns everything before that

    Args:
    name(str)

    Returns:
    The first name(str)
    Theres only one name so can't run function
    '''
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
    '''
    Runs the name in reverse

    Args:
    name(str)

    Returns:
    Reversed name(str)
    '''
    return name[::-1]

def hyphen_check(name):
    '''
    Detects if a hyphen is in the name 

    Args:
    name(str)

    Returns:
    True of False (Boolean)
    '''
    for letter in name:
        if "-" in name:
            return True
            break
        else:
            return False
def last_name(name):
    '''
    Detects where the last space in the name is and returns everything before that

    Args:
    name(str)

    Returns:
    The last name(str)
    only one name so unable to run function(str)
    '''
    name_list = list(name)
    if " " in name_list:
        backwards_name = reverse(name)
        backwards_last_name = first_name(backwards_name)
        last_name = reverse(backwards_last_name)
        return last_name
    else:
        return("There's only 1 word in name so unable to run this function")


def middle_name(name):
    '''
    Detects where the first space and last pace in the name is and removes everything in between them

    Args:
    name(str)

    Returns:
    The middle name(s) (str)
    There is not middle names
    '''
    name_list = list(name)
    space_counter = 0
    for letter in name:
        if letter == " ":
            space_counter += 1
    if space_counter > 1:
        begin = 0
        for index in range(len(name)):
            if name[index] == " ":
                begin += 1
                break
            else:
                begin += 1
        end = len(name)
        for ind in range(len(name) -1):
            if name[ind] == " ":
                break
            else:
                end -= 1
        middle_names = name_list[begin: end]
        return "".join(middle_names)
            

        



def titles(name):
    '''
    Detects if a special title is in the name
    Args:
    name(str)

    Returns:
    True or False (boolean)
    '''
    titles = ["Dr.", "Sir", "Mr.", "Ms", "Mrs.", "Esq."]
    first_part_of_name = first_name(name)
    if first_part_of_name in titles:
        return True
    else:
        return False



def shuffle(name):
    '''
    Takes a random letter from the name and puts it in a new str

    Args:
    name(str)

    Returns:
    Suffled_name(str)
    '''
    name_list = list(name)
    shuffled_list = []
    while len(name_list) > 0:
        random_letter = random.randint(0, (len(name_list)-1))
        selected_letter = name_list[random_letter]
        shuffled_list.append(selected_letter)
        name_list.remove(selected_letter) 
                
    return "".join(shuffled_list)



def sorted_array(name):
    sorted_array_list = []
    ascii_list = []
    lower_letter = lower(name)
    for i in lower_letter:
        let_to_num = ord(i)
        ascii_list.append(let_to_num)
    ascii_list.sort()
    for numbers in ascii_list:
        letters = chr(numbers)
        sorted_array_list.append(letters)
    return("".join(sorted_array_list))
        
        
        

def initials(name):
    ''' 
    Takes the first letter of every word and puts a period between it

    Args:
    name(str)

    Returns:
    Initals with period between them(str)
    
    '''
    name_list = list(name)
    initals_list = []
    counter=0
    for letter in name_list:
        if counter == 0:
            initals_list.append(letter)
            counter += 1
        if letter == " ":
            counter = 0
    return(".".join(initals_list))
        
        
 






        
            
        

        

def main():
    while True:
        #Asks for the name, will be put through all functions
        users_name = input("What's your name?")
        #Where user sees all possible options for what to do with name input
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
    12. Check if theres a special title
    13. Print initals
    14. Place letters in alphabetic order
    15. Quit
    """       
        )
        if menu == "1":
            vowel_count(users_name)
        elif menu =="2":
            #If there is not a special title
            if titles(users_name) == False:
                print(first_name(users_name))
            else:
                #Remove the title and run the function
                without_title = users_name.replace(first_name(users_name), "")
                without_title_and_space = without_title.replace(" ", "", 1)
                print(first_name(without_title_and_space))
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
            if titles(users_name) == False:
                print(middle_name(users_name))
            else:
                without_title = users_name.replace(first_name(users_name), "")
                without_title_and_space = without_title.replace(" ", "", 1)
                print(middle_name(without_title_and_space))
        elif menu == "9":
            print(upper(users_name))
        elif menu == "10":
            #If the name is the same as it is when reversed
            if users_name == reverse(users_name):
                print('it is a palindrome')
            else:
                print('it is not a palindrome')
        elif menu == "11":
            print(shuffle(users_name))
        elif menu == "12":
            if titles(users_name) == True:
                print('There is a special title')
            else:
                print('There is not a special title')
        elif menu == "13":
            print(initials(users_name))
        elif menu == "14":
            print(sorted_array(users_name))
        elif menu == "15":
            break
        
        else:
            print('not an option(type number(1, 2, etc)')

main()

