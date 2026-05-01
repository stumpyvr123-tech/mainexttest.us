import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Please select your role", font=("Arial", 24))
label.pack()
root.mainloop()

print("Select an option:")
print("1. Teacher")
print("2. Student")

choice = input("Enter choice (1 or 2): ")

if choice == "1":
    print("Starting teacher program...")
elif choice == "2":
    print("Starting student program...")
else:
    print("Invalid option!")
