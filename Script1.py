""" This program converts RGB to hexadecimal and hexadecimal to RGB """

def rgb_hex():
    invalid_entry_msg = "Sorry that input is not valid, please try again."
    while (True):
        red = raw_input("Please enter an integer value for Red between 0 and 255: " )
        if red.isdigit():
            red = int(red)
            if red <0 or red >255:
                print invalid_entry_msg
              #  return
            else:
                while(True):
                    green = raw_input("Please enter an integer value for Green between 0 and 255: " )
                    if green.isdigit():
                        green = int(green)
                        if green <0 or green >255: #or not green.isdigit():
                            print invalid_entry_msg
                        #    return
                        else:
                            while (True):
                                blue = raw_input("Please enter an integer value for Blue between 0 and 255: " )
                                if blue.isdigit():
                                    blue = int(blue)
                                    if blue <0 or blue >255: #or not blue.isdigit():
                                        print invalid_entry_msg
                                 #       return
                                    else:
                                        break
                            break
                break




 #   val = (bin(red) << bin(16)) + (bin(green) << bin(8)) + bin(blue)
    val = (red << 16) + (green << 8) + blue
    print "%s" % (hex(val)[2:]).upper()

def hex_rgb():
    hex_val = raw_input("Please enter a six digit hexadecimal color value to convert to an RGB: ")
    invalid_length_msg = "Sorry that input is not valid as it is not six digits, please try again."
    invalid_digits_msg = "Sorry that input does not use the correct hexadecimal digits. Please try again."

    if len(hex_val) != 6:
        print invalid_length_msg
        return

    elif (hex_val[0] != "0" and hex_val[0] != "1" and hex_val[0] != "2" and hex_val[0] != "3" and hex_val[0] != "4" \
    and hex_val[0] != "5" and hex_val[0] != "6" and hex_val[0] != "7" and hex_val[0] != "8" and hex_val[0] != "9" \
    and hex_val[0].upper() != "A" and hex_val[0].upper() != "B" and hex_val[0].upper() != "C" and hex_val[0].upper() != "D" \
    and hex_val[0].upper() != "E" and hex_val[0].upper() != "F"):

        print invalid_digits_msg
        return

    elif (hex_val[1] != "0" and hex_val[1] != "1" and hex_val[1] != "2" and hex_val[1] != "3" and hex_val[1] != "4" \
    and hex_val[1] != "5" and hex_val[1] != "6" and hex_val[1] != "7" and hex_val[1] != "8" and hex_val[1] != "9" \
    and hex_val[1].upper() != "A" and hex_val[1].upper() != "B" and hex_val[1].upper() != "C" and hex_val[1].upper() != "D" \
    and hex_val[1].upper() != "E" and hex_val[1].upper() != "F"):

        print invalid_digits_msg
        return

    elif (hex_val[2] != "0" and hex_val[2] !="1" and hex_val[2] != "2" and hex_val[2] != "3" and hex_val[2] != "4" \
    and hex_val[2] != "5" and hex_val[2] != "6" and hex_val[2] != "7" and hex_val[2] != "8" and hex_val[2] != "9" \
    and hex_val[2].upper() != "A" and hex_val[2].upper() != "B" and hex_val[2].upper() != "C" and hex_val[2].upper() != "D" \
    and hex_val[2].upper() != "E" and hex_val[2].upper() != "F"):
        print invalid_digits_msg
        return

    elif (hex_val[3] != "0" and hex_val[3] !="1" and hex_val[3] != "2" and hex_val[3] != "3" and hex_val[3] != "4" \
        and hex_val[3] != "5" and hex_val[3] != "6" and hex_val[3] != "7" and hex_val[3] != "8" and hex_val[3] != "9" \
        and hex_val[3].upper() != "A" and hex_val[3].upper() != "B" and hex_val[3].upper() != "C" and hex_val[3].upper() != "D" \
        and hex_val[3].upper() != "E" and hex_val[3].upper() != "F"):

        print invalid_digits_msg
        return

    elif (hex_val[4] != "0" and hex_val[4] !="1" and hex_val[4] != "2" and hex_val[4] != "3" and hex_val[4] != "4" \
        and hex_val[4] != "5" and hex_val[4] != "6" and hex_val[4] != "7" and hex_val[4] != "8" and hex_val[4] != "9" \
        and hex_val[4].upper() != "A" and hex_val[4].upper() != "B" and hex_val[4].upper() != "C" and hex_val[4].upper() != "D" \
        and hex_val[4].upper() != "E" and hex_val[4].upper() != "F"):

        print invalid_digits_msg
        return

    elif (hex_val[5] != "0" and hex_val[5] !="1" and hex_val[5] != "2" and hex_val[5] != "3" and hex_val[5] != "4" \
        and hex_val[5] != "5" and hex_val[5] != "6" and hex_val[5] != "7" and hex_val[5] != "8" and hex_val[5] != "9" \
        and hex_val[5].upper() != "A" and hex_val[5].upper() != "B" and hex_val[5].upper() != "C" and hex_val[5].upper() != "D" \
        and hex_val[5].upper() != "E" and hex_val[5].upper() != "F"):

        print invalid_digits_msg
        return

    else:
        hex_val = int(hex_val, 16)
        two_hex_digits = 2 ** 8
        blue = hex_val % two_hex_digits
        hex_val = hex_val >> 8
        green = hex_val % two_hex_digits
        hex_val = hex_val >> 8
        red = hex_val % two_hex_digits

        print "red: %s, green: %s, blue: %s" % (red,green,blue)

def convert():
    while(True):
        option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter x to Exit: ")
        if option == "1":
            print "RGB to HEX"
            rgb_hex()
        elif option == "2":
            print "RGB to HEX"
            hex_rgb()
        elif option.lower() == "x":
            print "Goodbye"
            break
        else:
            print "Error, incorrect choice selection."

convert()
