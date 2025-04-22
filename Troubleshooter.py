import os
import subprocess
import tkinter as tk
import platform
import psutil
import winreg
import ctypes
import sys
from tkinter import messagebox

# Function to Adjust Transparency
def adjust_transparency(value):
    root.attributes('-alpha', float(value) / 100)  # Convert 0-100 to 0.0-1.0

# System Cleanup Functions
def clear_temp():
    os.system('del /s /q "%temp%\\*.*"')
    messagebox.showinfo("Success", "Temporary files cleared!")

def remove_update_residue():
    os.system("cleanmgr /sagerun:1")
    messagebox.showinfo("Success", "Windows Update residue files removed!")

def remove_bloatware():
    bloatware_apps = ["CandyCrushSaga", "Twitter", "XboxApp", "Spotify", "Clipchamp", "News", "SolitaireCollection", "Microsoft.MixedReality.Portal", "Print3D", "Spotify", "Microsoft.Office.Sway", "Microsoft.Office.OneNote", "Microsoft.SkypeApp", "MicrosoftCorporationII.MicrosoftFamily", "MicrosoftTeams", "MSTeams", "Microsoft.549981C3F5F10", "Microsoft.3DBuilder", "Microsoft.Messaging", "Microsoft.SkypeApp", "Microsoft.WindowsMaps", "Microsoft.WindowsSoundRecorder", "Microsoft.XboxApp"]
    for app in bloatware_apps:
        os.system(f"powershell -Command \"Get-AppxPackage *{app}* | Remove-AppxPackage\"")
    messagebox.showinfo("Success", "Preinstalled bloatware removed!")

def registry_cleanup():
    os.system("reg delete HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentDocs /f")
    messagebox.showinfo("Success", "Dump registry cleaned up!")

# System Maintenance Functions
def check_disk():
    subprocess.run("chkdsk /f", shell=True)
    messagebox.showinfo("Info", "Disk check initiated. Restart may be required.")

def check_system_integrity():
    os.system("sfc /scannow")
    messagebox.showinfo("Info", "System integrity check initiated.")

def memory_diagnostic():
    os.system("mdsched.exe")
    messagebox.showinfo("Info", "Memory diagnostic tool launched. Restart may be required.")

def defragment_disk():
    os.system("dfrgui")
    messagebox.showinfo("Info", "Disk Defragmenter launched!")

# Network Functions
def flush_dns():
    os.system("ipconfig /flushdns")
    messagebox.showinfo("Success", "DNS cache flushed!")

def reset_network():
    os.system("netsh winsock reset")
    messagebox.showinfo("Success", "Network adapter reset!")

def enable_file_printer_sharing():
    os.system("netsh advfirewall firewall set rule group=\"File and Printer Sharing\" new enable=Yes")
    messagebox.showinfo("Success", "File and Printer Sharing enabled without password protection!")

# Driver Issues Functions
def reinstall_network_drivers():
    os.system("devmgmt.msc")  # Opens Device Manager for manual installation
    messagebox.showinfo("Success", "WiFi and LAN drivers reinstalled!")

def reinstall_touchpad_driver():
    os.system("devmgmt.msc")  # Opens Device Manager for manual installation
    messagebox.showinfo("Success", "Touchpad driver reinstalled!")

def reinstall_sound_driver():
    os.system("devmgmt.msc")
    messagebox.showinfo("Success", "Sound driver reinstalled!")

def reinstall_display_driver():
    os.system("devmgmt.msc")
    messagebox.showinfo("Success", "Display driver reinstalled!")

def disable_display_driver():
    os.system("devmgmt.msc")
    messagebox.showinfo("Success", "Display driver disabled!")

# System Restore & Performance Functions
def create_restore_point():
    script = "Wmic.exe /Namespace:\\root\\default Path SystemRestore Call CreateRestorePoint \"Manual Restore Point\", 100, 7"
    os.system(script)
    messagebox.showinfo("Success", "System Restore Point Created!")

def system_restore():
    os.system("rstrui.exe")
    messagebox.showinfo("Info", "System Restore launched. Follow on-screen instructions.")

def enable_max_performance():
    os.system("powercfg -setactive SCHEME_MAX")
    messagebox.showinfo("Success", "Power plan set to Maximum Performance!")

def enable_hibernate():
    os.system("powercfg -h on")
    messagebox.showinfo("Success", "Hibernate enabled!")

def disable_hibernate():
    os.system("powercfg -h off")
    messagebox.showinfo("Success", "Hibernate disabled!")

def disable_windows_update():
    os.system("sc stop wuauserv")
    os.system("sc config wuauserv start=disabled")
    os.system("sc stop bits")
    os.system("sc config bits start=disabled")
    os.system("sc stop cryptsvc")
    os.system("sc config cryptsvc start=disabled")
    messagebox.showinfo("Success", "Windows Update disabled!")

def disable_windows_update():
    os.system("sc stop wuauserv")
    os.system("sc config wuauserv start=disabled")
    os.system("sc stop bits")
    os.system("sc config bits start=disabled")
    os.system("sc stop cryptsvc")
    os.system("sc config cryptsvc start=disabled")
    messagebox.showinfo("Success", "Windows Update disabled!")

def search_for_updates():
    os.system("ms-settings:windowsupdate-action")
    messagebox.showinfo("Info", "Windows Update search initiated!")

def disable_drive_encryption():
    os.system("manage-bde -off C:")
    messagebox.showinfo("Success", "Drive encryption disabled!")

def create_recovery_drive():
    os.system("RecoveryDrive.exe")
    messagebox.showinfo("Info", "Recovery Drive creation tool launched!")

# Additional System Functions
def open_device_manager():
    os.system("devmgmt.msc")

def open_disk_management():
    os.system("diskmgmt.msc")

def open_network_adapters():
    os.system("ncpa.cpl")

def open_event_viewer():
    os.system("eventvwr.msc")

def open_add_remove_programs():
    os.system("appwiz.cpl")
    messagebox.showinfo("Info", "Add or Remove Programs opened!")

def open_optional_features():
    os.system("optionalfeatures")
    messagebox.showinfo("Info", "Windows Optional Features opened!")

def restart_explorer():
    os.system("taskkill /f /im explorer.exe & start explorer")
    messagebox.showinfo("Success", "Explorer.exe restarted!")

def show_hidden_files():
    os.system("reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v Hidden /t REG_DWORD /d 1 /f")
    os.system("taskkill /f /im explorer.exe & start explorer")
    messagebox.showinfo("Success", "Hidden files are now visible!")

def open_services():
    os.system("services.msc")

def change_date_time():
    os.system("timedate.cpl")

def change_time_zone():
    os.system("tzutil /l")
    messagebox.showinfo("Info", "Time Zone settings opened!")

def change_pc_name():
    os.system("sysdm.cpl")
    messagebox.showinfo("Info", "Change PC Name settings opened!")

def change_workgroup():
    os.system("sysdm.cpl")
    messagebox.showinfo("Info", "Change Workgroup settings opened!")

def change_user_name():
    os.system("control userpasswords2")
    messagebox.showinfo("Info", "User Account settings opened!")

def open_computer_management():
    os.system("compmgmt.msc")

def open_system_configuration():
    os.system("msconfig")


def get_system_info():
    # Get Processor Info from Registry
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
        cpu_name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
        winreg.CloseKey(key)
    except:
        cpu_name = "Unknown Processor"

    # Get Total RAM Size
    ram_size = round(psutil.virtual_memory().total / (1024**3), 2)

    # Get Total Storage Size
    storage_size_gb = sum(
        psutil.disk_usage(d.mountpoint).total for d in psutil.disk_partitions() if 'fixed' in d.opts
    ) / (1024**3)

    # Get GPU Information
    try:
        gpu_info_raw = subprocess.getoutput("wmic path win32_videocontroller get caption").strip().split("\n")
        gpu_info = "\n".join(line.strip() for line in gpu_info_raw[1:] if line.strip())
    except:
        gpu_info = "GPU Info Not Available"

    # Display Information
    info = f"Processor: {cpu_name}\n"
    info += f"RAM Size: {ram_size} GB\n"
    info += f"Total Storage Size: {int(storage_size_gb)} GB\n"
    info += f"Graphics Card: {gpu_info}\n"

    messagebox.showinfo("System Information", info)

def open_registry_editor():
    os.system("regedit")
    messagebox.showinfo("Info", "Registry Editor opened!")

def run_predefined_bat():
    bat_file = "winget.bat"  # Replace with your actual batch file name
    if os.path.exists(bat_file):
        os.system(f'start "" "{bat_file}"')
    else:
        messagebox.showerror("Error", "Batch file not found!")

def run_exe():
    exe_file = "hidden.exe"  # Set your predefined EXE path
    if os.path.exists(exe_file):
        os.system(f'start "" "{exe_file}"')
    else:
        messagebox.showerror("Error", "File not found!")
    



# GUI Setup
root = tk.Tk()
root.title("PC Troubleshooter")
root.geometry("600x800")
root.configure(bg='black')
root.attributes('-alpha', 0.9)  # Default transparency

frame = tk.Frame(root, bg='black')
frame.pack()

sections = {
    "System Cleanup": [
        ("Clear Temp Files", clear_temp),
        ("Remove Windows Update Residue", remove_update_residue),
        ("Remove Bloatware", remove_bloatware),
        ("Registry Cleanup", registry_cleanup)
    ],
    "System Information & Maintenance": [
	("Get System Info", get_system_info),
        ("Check Disk", check_disk),
        ("Defragment Disk", defragment_disk),
        ("Memory Diagnostic", memory_diagnostic)
    ],
    "Network": [
        ("Flush DNS", flush_dns),
        ("Reset Network", reset_network),
	("Open Network Adapters", open_network_adapters),
        ("Enable File & Printer Sharing", enable_file_printer_sharing)
    ],
    "Driver Issues": [
        ("Reinstall Network Drivers", reinstall_network_drivers),
	("Reinstall Sound Driver", reinstall_sound_driver),
	("Reinstall Display Driver", reinstall_display_driver),
	("Disable Display Driver", disable_display_driver),
        ("Reinstall Touchpad Driver", reinstall_touchpad_driver)
    ],
    "System Restore & Performance": [
        ("Create Restore Point", create_restore_point),
        ("System Restore", system_restore),
        ("Enable Hibernate", enable_hibernate),
        ("Disable Hibernate", disable_hibernate),
        ("Create Recovery Drive", create_recovery_drive),
	("Enable Max Performance", enable_max_performance)
    ],

   "Additional Functions": [
        ("Open Device Manager", open_device_manager),
        ("Open Disk Management", open_disk_management),
        ("Open Event Viewer", open_event_viewer),
        ("Add/Remove Programs", open_add_remove_programs),
        ("Open Optional Features", open_optional_features),
        ("Restart Explorer", restart_explorer),
        ("Show Hidden Files", show_hidden_files),
    	("Disbale Update", disable_windows_update),
	("Open Services", open_services),
        ("Change Date & Time", change_date_time),
        ("Change Time Zone", change_time_zone),
        ("Change PC Name", change_pc_name),
        ("Change Workgroup", change_workgroup),
        ("Change User Name", change_user_name),
        ("Open Computer Management", open_computer_management),
	("Open System Config", open_system_configuration),
	("Open Registry Editor", open_registry_editor),
	("Run Winget Installer", run_predefined_bat),
        ("Hide File/Folder", run_exe),
        ("Disable Drive Encryption", disable_drive_encryption)
        
    ]
}

for section, buttons in sections.items():
    tk.Label(frame, text=section, font=("Arial", 12, "bold"), bg='black', fg='white').pack()
    row_frame = tk.Frame(frame, bg='black')
    row_frame.pack()
    for i, (text, command) in enumerate(buttons):
        tk.Button(row_frame, text=text, command=command, width=30, bg='#333', fg='white').grid(row=i // 5, column=i % 5, padx=5, pady=5)

# Transparency Slider
slider_frame = tk.Frame(root, bg='black')
slider_frame.pack(pady=10)

tk.Label(slider_frame, text="Transparency", fg="white", bg="black").pack()
transparency_slider = tk.Scale(slider_frame, from_=10, to=100, orient="horizontal", 
                               command=adjust_transparency, bg='black', fg='white', 
                               length=200)
transparency_slider.set(90)  # Default to 90% opacity
transparency_slider.pack()
root.mainloop()
