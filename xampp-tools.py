import os
import shutil
import webbrowser
from tkinter import Tk, Label, Button, Entry, messagebox, ttk, StringVar, Frame
import subprocess

class XamppTools:
    def __init__(self):
        # Configuration locations
        self.XAMPP_PATH = r"C:\xampp"
        self.MYSQL_BACKUP_DIR = os.path.join(self.XAMPP_PATH, "mysql", "backup")
        self.MYSQL_DATA_DIR = os.path.join(self.XAMPP_PATH, "mysql", "data")
        self.APACHE_CONFIG_FILE = os.path.join(self.XAMPP_PATH, "apache", "conf", "httpd.conf")
        self.HTDOCS_PATH = os.path.join(self.XAMPP_PATH, "htdocs")
        
        # Default language
        self.language = "en"
        
        # Create main window
        self.root = Tk()
        self.root.title("XAMPP Tools")
        self.root.geometry("600x350")
        
        # Create main columns
        self.create_columns()
        
        # Initialize UI elements
        self.setup_project_column()
        self.setup_xampp_column()
        self.setup_footer()
        
        # Start the application
        self.root.mainloop()
    
    def create_columns(self):
        """Create the three main columns"""
        # Main container
        self.main_container = Frame(self.root)
        self.main_container.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Three columns
        self.project_column = Frame(self.main_container, relief='groove', bd=1)
        self.xampp_column = Frame(self.main_container, relief='groove', bd=1)
        
        # Pack columns
        self.project_column.pack(side='left', expand=True, fill='both', padx=5)
        self.xampp_column.pack(side='left', expand=True, fill='both', padx=5)
    
    def setup_project_column(self):
        """Setup the project management column"""
        # Column title
        Label(self.project_column, text="Project Management", 
              font=("Arial", 12, "bold")).pack(pady=10)
        
        # New project section
        Label(self.project_column, text="New Project", 
              font=("Arial", 10, "bold")).pack(pady=5)
        
        self.entry_new_project = Entry(self.project_column, width=30)
        self.entry_new_project.pack(pady=5)
        
        Button(self.project_column, text="Create New Project",
               command=self.create_new_project, width=25).pack(pady=5)
        
        # Project selection section
        Label(self.project_column, text="Select Existing Project", 
              font=("Arial", 10, "bold")).pack(pady=10)
        
        self.project_var = StringVar()
        self.project_dropdown = ttk.Combobox(self.project_column, 
                                           textvariable=self.project_var, 
                                           width=27)
        self.update_project_list()
        self.project_dropdown.pack(pady=5)
        
        Button(self.project_column, text="Open Project & VS Code",
               command=self.open_project_and_vscode, width=25).pack(pady=5)
    
    def setup_xampp_column(self):
        """Setup the XAMPP controls column"""
        # Column title
        Label(self.xampp_column, text="XAMPP Controls", 
              font=("Arial", 12, "bold")).pack(pady=10)
        
        # XAMPP controls
        Button(self.xampp_column, text="Open XAMPP & Start Services",
               command=self.open_xampp_and_start_services, width=25).pack(pady=5)
        
        Button(self.xampp_column, text="Open phpMyAdmin",
               command=self.open_phpmyadmin, width=25).pack(pady=5)
        
        # Port settings
        Label(self.xampp_column, text="Apache Port Settings", 
              font=("Arial", 10, "bold")).pack(pady=10)
        
        self.entry_port = Entry(self.xampp_column, width=15)
        self.entry_port.insert(0, self.get_apache_port() or "80")
        self.entry_port.pack(pady=5)
        
        Button(self.xampp_column, text="Change Apache Port",
               command=self.set_apache_port, width=25).pack(pady=5)
        
        # MySQL Fix
        Button(self.xampp_column, text="Fix MySQL",
               command=self.copy_mysql_backup, width=25).pack(pady=20)
    
    def setup_footer(self):
        """Setup the footer with GitHub link"""
        self.footer = Label(self.root, text="GitHub: Lukman754",
                          font=("Arial", 8), fg="blue", cursor="hand2")
        self.footer.pack(side="bottom", pady=5)
        self.footer.bind("<Button-1>", self.open_github)
    
    # Helper Methods
    def update_project_list(self):
        """Update the project dropdown list"""
        projects = self.get_htdocs_projects()
        self.project_dropdown['values'] = projects
        if projects:
            self.project_var.set(projects[0])
    
    def get_htdocs_projects(self):
        """Get list of projects in htdocs directory"""
        try:
            if not os.path.exists(self.HTDOCS_PATH):
                return []
            return [d for d in os.listdir(self.HTDOCS_PATH) 
                   if os.path.isdir(os.path.join(self.HTDOCS_PATH, d)) 
                   and d not in ['.', '..']]
        except Exception:
            return []
    
    # Action Methods
    def create_new_project(self):
        """Create a new project in htdocs and automatically open it"""
        project_name = self.entry_new_project.get().strip()
        if not project_name:
            messagebox.showerror("Error", "Please enter a project name")
            return
        
        project_path = os.path.join(self.HTDOCS_PATH, project_name)
        if os.path.exists(project_path):
            messagebox.showerror("Error", "Project already exists")
            return
        
        try:
            os.makedirs(project_path)
            with open(os.path.join(project_path, "index.php"), "w") as f:
                f.write("<?php\necho 'Welcome to " + project_name + "';\n?>")
            
            self.update_project_list()
            # Set dropdown to newly created project
            self.project_var.set(project_name)
            # Clear the entry field
            self.entry_new_project.delete(0, 'end')
            
            messagebox.showinfo("Success", "Project created successfully")
            
            # Automatically open the project in browser and VS Code
            self.root.after(500, self.open_project_and_vscode)  # Add slight delay for better UX
            
        except Exception as e:
            messagebox.showerror("Error", f"Error creating project: {e}")
    
    def open_project_and_vscode(self):
        """Open selected project in browser and VS Code"""
        project = self.project_var.get()
        if not project:
            messagebox.showerror("Error", "Please select a project")
            return
        
        # Open in browser
        port = self.entry_port.get() or "80"
        url = f"http://localhost:{port}/{project}"
        webbrowser.open(url)
        
        # Open in VS Code
        project_path = os.path.join(self.HTDOCS_PATH, project)
        try:
            vscode_path = r"C:\Users\{}\AppData\Local\Programs\Microsoft VS Code\Code.exe".format(
                os.getenv('USERNAME'))
            
            if not os.path.exists(vscode_path):
                vscode_path = r"C:\Program Files\Microsoft VS Code\Code.exe"
            
            if os.path.exists(vscode_path):
                subprocess.Popen([vscode_path, project_path],
                               creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                messagebox.showerror("Error", "VS Code not found")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error opening VS Code: {e}")
    
    def get_apache_port(self):
        """Get current Apache port from config"""
        try:
            if not os.path.exists(self.APACHE_CONFIG_FILE):
                return "80"
            
            with open(self.APACHE_CONFIG_FILE, "r") as file:
                for line in file:
                    if line.strip().startswith("Listen"):
                        return line.strip().split()[1]
            return "80"
        except Exception:
            return "80"
    
    def set_apache_port(self):
        """Update Apache port in config"""
        new_port = self.entry_port.get()
        if not new_port.isdigit() or int(new_port) < 1 or int(new_port) > 65535:
            messagebox.showerror("Error", "Please enter a valid port (1-65535)")
            return
        
        try:
            with open(self.APACHE_CONFIG_FILE, "r") as file:
                lines = file.readlines()
            
            with open(self.APACHE_CONFIG_FILE, "w") as file:
                for line in lines:
                    if line.strip().startswith("Listen"):
                        file.write(f"Listen {new_port}\n")
                    else:
                        file.write(line)
            
            messagebox.showinfo("Success", 
                              f"Apache port changed to {new_port}. Please restart Apache.")
        except Exception as e:
            messagebox.showerror("Error", f"Error changing port: {e}")
    
    def open_xampp_and_start_services(self):
        """Open XAMPP Control Panel and start services"""
        try:
            xampp_control = os.path.join(self.XAMPP_PATH, "xampp-control.exe")
            if os.path.exists(xampp_control):
                subprocess.Popen([xampp_control],
                               creationflags=subprocess.CREATE_NO_WINDOW)
                subprocess.Popen([os.path.join(self.XAMPP_PATH, "xampp_start.exe")],
                               creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                messagebox.showerror("Error", "XAMPP Control Panel not found")
        except Exception as e:
            messagebox.showerror("Error", f"Error opening XAMPP: {e}")
    
    def open_phpmyadmin(self):
        """Open phpMyAdmin in browser"""
        port = self.entry_port.get() or "80"
        url = f"http://localhost:{port}/phpmyadmin"
        webbrowser.open(url)
    
    def copy_mysql_backup(self):
        """Copy MySQL backup files to data directory and restart MySQL service"""
        try:
            if not os.path.exists(self.MYSQL_BACKUP_DIR):
                messagebox.showerror("Error", f"MySQL backup directory not found:\n{self.MYSQL_BACKUP_DIR}")
                return

            if not os.path.exists(self.MYSQL_DATA_DIR):
                messagebox.showerror("Error", f"MySQL data directory not found:\n{self.MYSQL_DATA_DIR}")
                return

            for root, dirs, files in os.walk(self.MYSQL_BACKUP_DIR):
                for file in files:
                    if file == "ibdata1":
                        continue
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, self.MYSQL_BACKUP_DIR)
                    dest_path = os.path.join(self.MYSQL_DATA_DIR, relative_path)

                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(source_path, dest_path)

            subprocess.Popen([os.path.join(self.XAMPP_PATH, "mysql", "bin", "mysqld.exe")], 
                            creationflags=subprocess.CREATE_NO_WINDOW)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
            
    def open_github(self, event=None):
        """Open GitHub profile"""
        webbrowser.open("https://github.com/Lukman754")

if __name__ == "__main__":
    XamppTools()