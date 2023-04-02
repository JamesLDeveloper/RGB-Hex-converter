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
                green = raw_input("Please enter an integer value for Green between 0 and 255: " )
                if green.isdigit():
                    green = int(green)
                    if green <0 or green >255: #or not green.isdigit():
                        print invalid_entry_msg
                    #    return
                    else:
                        blue = raw_input("Please enter an integer value for Blue between 0 and 255: " )
                        if blue.isdigit():
                            blue = int(blue)
                            if blue <0 or blue >255: #or not blue.isdigit():
                                print invalid_entry_msg
                         #       return
                            else:
                                break


 #   val = (bin(red) << bin(16)) + (bin(green) << bin(8)) + bin(blue)
    val = (red << 16) + (green << 8) + blue
    print "%s" % (hex(val)[2:]).upper()

def hex_rgb():
    hex_val = raw_input("Please enter a six digit hexadecimal color value to convert to an RGB: ")
    invalid_length_msg = "Sorry that input is not valid, please try again."
    if len(hex_val) != 6:
        print invalid_length_msg
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
            print "error"

convert()
