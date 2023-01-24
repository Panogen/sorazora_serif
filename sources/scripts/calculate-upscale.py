print("Reminder: The arrow key moves by 2 units in Inkscape!")
while(True):
    user_input = input("Value in Inkscape: ")
    if user_input == "exit":
        exit()
    try:
        original_value = float(user_input)
    except:
        print("Input must be numeric")
        continue
    upscaled_value = original_value / 411 * 800
    print("Upscaled value (n * 800/411): " + str(upscaled_value))
    print("Rounded to int: " + str(round(upscaled_value)))
