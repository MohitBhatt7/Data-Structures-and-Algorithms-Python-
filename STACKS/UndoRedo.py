# Undo Redo using stacks.
import keyboard
import time

undo_stack = []
redo_stack = []

def do_actions(action):
    undo_stack.append(action)
    redo_stack.clear()
    print(f"Action performed is:- {action}")
    show_stacks()
    
def Undo():
    if undo_stack:
        action = undo_stack.pop()
        redo_stack.append(action)
        print(f"Action undo:- {action}")
        
    else:
        print("Nothing to undo.")
        
        
    show_stacks()
    
def redo():
    if redo_stack:
        action = redo_stack.pop()
        undo_stack.append(action)
        print(f"Action redo:- {action}")
        
    else:
        print("Nothing to redo.")
    
    show_stacks()
    
def show_stacks():
    print(f"Undo_stacks:- {undo_stack}")
    print(f"Redo_stacks:- {redo_stack}")
    
actions = ["Typed 'Hello'", "Typed 'World'", "Deleted 'World'", "Typed 'Python'"]
for act in actions:
    do_actions(act)
    time.sleep(5)  # Small pause for readability

print("\nPress Ctrl+Z to Undo, Ctrl+Y to Redo. Press ESC to exit.")

# Listen for keyboard events
while True:
    if keyboard.is_pressed('ctrl+z'):
        undo_stack()
        time.sleep(0.3)  # prevent multiple triggers
    elif keyboard.is_pressed('ctrl+y'):
        redo_stack()
        time.sleep(0.3) 
    elif keyboard.is_pressed('esc'):
        print("\nExiting...")
        break
