import tkinter as tk
import random

class PasswordAuthenticator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Authenticator")
        
        # Create labels and entry fields
        self.password_label = tk.Label(self.master, text="Enter Password:")
        self.password_label.pack()
        
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()
        
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()
        
        # Create buttons
        self.check_button = tk.Button(self.master, text="Check", command=self.check_password)
        self.check_button.pack()
        
        self.generate_button = tk.Button(self.master, text="Generate", command=self.generate_password)
        self.generate_button.pack()
        
        # Generate a random password
        self.generated_password = self.generate_random_password()
        
    def check_password(self):
        entered_password = self.password_entry.get()
        if entered_password == self.generated_password:
            self.result_label.config(text="Access Granted", fg="green")
        else:
            self.result_label.config(text="Access Denied", fg="red")
    
    def generate_password(self):
        self.generated_password = self.generate_random_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, self.generated_password)
    
    def generate_random_password(self):
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        password = "".join(random.choice(characters) for _ in range(10))
        return password

# Create the main window
root = tk.Tk()

# Create the PasswordAuthenticator instance
authenticator = PasswordAuthenticator(root)

# Run the main loop
root.mainloop()