#Language operations: 
# '#' adds 1
# '@' subtracts 1 
# '*' multiplies by itself  
# '&' prints current number

message = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&" 
def minicompiler(string):
    value = 0
    result_string = ""
    for symbol in string:
        if symbol == "#":
            value += 1
        elif symbol == "@":
            value -= 1
        elif symbol == "*":
            value *= value
        elif symbol == "&":
            result_string += str(value)
    return result_string
print(minicompiler(message))