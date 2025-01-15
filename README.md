# XAMPP Tools

## Description
This program is a simple tool to manage key XAMPP functionalities, such as opening the XAMPP Control Panel, changing the Apache port, fixing the MySQL directory, and accessing phpMyAdmin. It features a user-friendly GUI built with `tkinter`.

![403430975-1de23ca3-d4a6-4af3-a40f-fc24b8d40ac7 (1)](https://github.com/user-attachments/assets/c23d57a3-3aba-41d2-9a06-d7134ecb4e72)


---

## Features

Here's the improved description using English:

1. **Create New Project**
   - Creates a new PHP project in the htdocs folder with basic structure
   - Automatically generates index.php with a welcome page template
   - Opens the project in VS Code after creation

2. **Project Quick Access**
   - Displays existing projects from htdocs folder as interactive buttons
   - Single click to launch project in browser and open in VS Code editor
   - Provides quick navigation to your development environments

3. **Open XAMPP & Start Apache/MySQL**
   - Opens the XAMPP Control Panel and starts the Apache and MySQL services.

4. **Open phpMyAdmin**
   - Launches phpMyAdmin in the default browser using the configured Apache port.

5. **Change Apache Port**
   - Allows users to change the default Apache port (e.g., from 80 to a custom port).

6. **Fix MySQL**
   - Repairs the MySQL data directory by copying files from the backup folder (`C:\xampp\mysql\backup`) to the MySQL data directory (`C:\xampp\mysql\data`).

     
---

## System Requirements

- **Operating System**: Windows
- **No Additional Installation Required**: The program is available as an executable file.

---

## How to Use

1. **Download the Program**:
   - Download the executable file from the following link: [Download XAMPP Tools](https://github.com/lukman754/Xampp-tools/raw/refs/heads/main/xampp-tools.exe).

2. **Run the Program**:
   - Double-click the downloaded `.exe` file to launch the application.

3. **Interface**:
   - **Open XAMPP & Start Apache/MySQL**: Click this button to open the XAMPP Control Panel and start the services.
   - **Open phpMyAdmin**: Click this button to open phpMyAdmin in your default browser.
   - **Change Apache Port**:
     - Enter the new port number in the input field.
     - Click the "Change Apache Port" button.
     - The program will update the Apache configuration.
   - **Fix MySQL**: Click this button to repair the MySQL directory (useful in case of data issues).
   - **Language Settings**: Click the "Language" button to toggle between English and Indonesian.

---

## Program Structure

- `MYSQL_BACKUP_DIR`: Directory for MySQL backups.
- `MYSQL_DATA_DIR`: Directory for MySQL data.
- `APACHE_CONFIG_FILE`: Apache configuration file.
- `XAMPP_PATH`: Path to the XAMPP Control Panel.
- `texts`: A dictionary for multi-language support.

---

## Important Notes

1. Ensure that the selected port for Apache is not in use by another application.
2. The default XAMPP directory is assumed to be `C:\xampp`. If XAMPP is installed elsewhere, adjust the relevant variables accordingly.
3. Notifications are only displayed for the "Change Apache Port" function.

---

## License
This program is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. For more information about the license, visit [GPL-3.0 License Details](https://www.gnu.org/licenses/gpl-3.0.en.html).

---

## Contributors
Created by: **Lukman Muludin**  
GitHub: [Lukman754](https://github.com/Lukman754)

---

### Tag/Keyword
XAMPP Tools, Apache port changer, MySQL fix tool, phpMyAdmin launcher, XAMPP management, MySQL shutdown unexpectedly, Apache blocked port, XAMPP troubleshooting, XAMPP GUI tool, fix MySQL data directory, XAMPP utilities, Apache configuration tool, manage XAMPP services, XAMPP helper, MySQL error repair, MySQL backup restoration, Apache port settings, XAMPP Windows tool, localhost management, Apache port blocked fix, MySQL crash fix

08:19:20  [mysql] 	Error: MySQL shutdown unexpectedly.
08:19:21  [mysql] 	This may be due to a blocked port, missing dependencies, 
08:19:21  [mysql] 	improper privileges, a crash, or a shutdown by another method.
08:19:21  [mysql] 	Press the Logs button to view error logs and check
08:19:21  [mysql] 	the Windows Event Viewer for more clues
08:19:21  [mysql] 	If you need more help, copy and post this
08:19:21  [mysql] 	entire log window on the forums


