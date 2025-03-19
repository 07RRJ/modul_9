# import platform

# x = platform.system()
# print(x)

# if isinstance(2.0, int):
#     print("yep")

# print(int(float('68.0')))

import msvcrt

print("Press 'Esc' to exit the program.")

while True:
    key = msvcrt.getwch()  # Wait for a key press
    if key == 'q':  # Escape key in ASCII
        print("Exiting the program...")
        break  # Exit the loop
    else:
        print(f"You pressed: {key}")