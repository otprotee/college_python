from pynput import keyboard
list = []

def press_keyboard(letter):
    try:
        print('{0}'.format(letter.char))
    except AttributeError:
        print('{0}'.format(letter))

def release_keyboard(letter):
    print('{0}'.format(letter))
    if letter == keyboard.Key.esc:
        return False
def lists():
    f = open('test123', 'w')
    for x in range(0,10):
        list.append(release_keyboard)
        list.append(release_keyboard)
    print(list)
    f.close()

lists()
with (keyboard.Listener(
        on_press=press_keyboard,
        on_release=release_keyboard)as listener):
    listener.join()