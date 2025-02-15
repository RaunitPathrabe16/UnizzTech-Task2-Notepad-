import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class Notepad:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")  

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')
 
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_notepad)

    def open_file(self):
        """Open a file and display its contents in the text area."""
        file_path = filedialog.askopenfilename(defaultextension=".txt",  filetypes=[("Text files", "*.txt"),("All files", "*.*")])
                                                
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)  
                    self.text_area.insert(tk.END, file.read()) 
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        """Save the current contents of the text area to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",  filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
                                                   
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END)) 
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def save_as_file(self):
        """Save the current contents of the text area to a new file."""
        self.save_file() 

    def exit_notepad(self):
        """Exit the notepad application."""
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()