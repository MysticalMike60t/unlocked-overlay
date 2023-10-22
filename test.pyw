import time
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import threading  # Add this import for threading

def close_after_5_seconds():
    root.destroy()

def create_rounded_rectangle_image(width, height, radius, bg_color, border_color):
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill=bg_color, outline=border_color)
    draw.rectangle((0, 0, width, height), fill=bg_color)
    draw.pieslice((0, 0, 2 * radius, 2 * radius), 90, 180, fill=bg_color, outline=border_color)
    draw.pieslice((width - 2 * radius, 0, width, 2 * radius), 0, 90, fill=bg_color, outline=border_color)
    draw.pieslice((0, height - 2 * radius, 2 * radius, height), 180, 270, fill=bg_color, outline=border_color)
    draw.pieslice((width - 2 * radius, height - 2 * radius, width, height), 270, 360, fill=bg_color, outline=border_color)

    return ImageTk.PhotoImage(image)

def typewriter_animation(text_widget, text, delay=50):
    for i in range(1, len(text) + 1):
        text_widget.config(text=text[:i])
        text_widget.update()
        time.sleep(delay / 1000)  # Delay in seconds

def blink_cursor(cursor_label, cursor_text, visible_delay=500, invisible_delay=500):
    while True:
        cursor_label.config(text=cursor_text)
        cursor_label.update()
        time.sleep(visible_delay / 1000)
        cursor_label.config(text="")
        cursor_label.update()
        time.sleep(invisible_delay / 1000)

root = tk.Tk()
root.overrideredirect(True)

# Dark theme colors
bg_color = "#2E2E2E"  # Dark gray background
text_color = "#FFFFFF"  # White text

# Set dimensions and radius for rounded corners
window_width = 400
window_height = 200
corner_radius = 20

# Create a rounded rectangle image
shape_image = create_rounded_rectangle_image(window_width, window_height, corner_radius, bg_color, bg_color)

# Create a canvas with the same dimensions as the image
canvas = tk.Canvas(root, width=window_width, height=window_height, highlightthickness=0)
canvas.pack()

# Create the label with rounded corners
canvas.create_image(window_width / 2, window_height / 2, image=shape_image)

# Create a label for typewriter text
typewriter_label = tk.Label(root, text="", font=("Segoe UI", 36), fg=text_color, bg=bg_color)
typewriter_label.place(relx=0.5, rely=0.5, anchor="center")

# Create a cursor label
cursor_label = tk.Label(root, text="_", font=("Segoe UI", 36), fg=text_color, bg=bg_color)
cursor_label.place(x=150, y=150)  # Adjust the position as needed

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for centering the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Start the typewriter animation after a delay
root.after(1000, typewriter_animation, typewriter_label, "Unlocked")

# Start the cursor blinking
cursor_thread = threading.Thread(target=blink_cursor, args=(cursor_label, "_", 500, 500))  # Adjust the delays as needed
cursor_thread.daemon = True
cursor_thread.start()

# Set a timer to close the window after 5 seconds
root.after(6000, close_after_5_seconds)

root.mainloop()
