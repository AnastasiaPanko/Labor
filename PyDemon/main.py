import keyboard
import pynput.mouse
import controller
import time


def blockinput():
    global block_input_flag
    block_input_flag = 1
    t1 = threading.Thread(target=blockinput_start)
    t1.start()
    print("[SUCCESS] Input blocked!")


def unblockinput():
    blockinput_stop()
    print("[SUCCESS] Input unblocked!")

def blockinput_start():
    mouse = controller()
    global block_input_flag
    for i in range(150):
        keyboard.block_key(i)
        while block_input_flag == 1:
            mouse.position = (0, 0)

def blockinput_stop():
    global block_input_flag
    for i in range(150):
        keyboard.unblock_key(i)
    block_input_flag = 0
blockinput()
print("now blocking")
sleep(5)
print("now unblocking")



