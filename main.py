import os
import sys
import time
import re
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading

# Safe patterns to auto-wrap for function call checks
AUTO_WRAP_FUNCTIONS = [
    r"r_nvg\.set_nightvision_animated",
    r"r_nvg\.toggle_nightvision",
    r"torch:section\(\)",
    r"db\.actor:item_in_slot\(\d+\)",
    r"item_device\.nv_state"
]

# Mod detection keywords
KNOWN_MODS = ["GAMMA", "EFP", "ANOMALY", "ANTHALOGY"]

# File types to scan
VALID_EXTENSIONS = [".script", ".ltx", ".ini", ".xml", ".txt"]

# Backup function with timestamp and per-directory saving
BACKUP_BASE = "backups"
def backup_file(path, root_folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    rel_path = os.path.relpath(path, root_folder)
    backup_root = os.path.join(os.path.dirname(root_folder), BACKUP_BASE, timestamp)
    os.makedirs(backup_root, exist_ok=True)
    backup_path = os.path.join(backup_root, rel_path.replace(os.sep, "__")) + ".bak"
    if not os.path.exists(backup_path):
        shutil.copy2(path, backup_path)

# Function wrapper for known risky calls
def wrap_known_risky_calls(content):
    for pattern in AUTO_WRAP_FUNCTIONS:
        matches = list(re.finditer(pattern, content))
        for match in reversed(matches):
            line_start = content.rfind("\n", 0, match.start()) + 1
            line_end = content.find("\n", match.end())
            if line_end == -1:
                line_end = len(content)
            line = content[line_start:line_end].strip()
            if not line.startswith("if type") and not "function" in line:
                wrapped = f"if type({pattern.split('.')[0]}) == \"table\" and type({pattern}) == \"function\" then\n    {line}\nend"
                content = content[:line_start] + wrapped + content[line_end:]
    return content

# Detect modified files
def get_recent_files(folder, days=30):
    cutoff = time.time() - (days * 86400)
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            if os.path.splitext(file)[1].lower() in VALID_EXTENSIONS:
                if os.path.getsize(path) < 5 * 1024 * 1024:
                    if os.path.getmtime(path) >= cutoff:
                        yield path

def get_all_valid_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            if os.path.splitext(file)[1].lower() in VALID_EXTENSIONS:
                if os.path.getsize(path) < 5 * 1024 * 1024:
                    yield path

# Process and auto-fix a file
def fix_file(path, root_folder):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    fixed = wrap_known_risky_calls(content)
    if content != fixed:
        backup_file(path, root_folder)
        with open(path, "w", encoding="utf-8") as f:
            f.write(fixed)
        return f"✔ Fixed: {path}"
    else:
        return f"- No issues: {path}"

# Detect mod type (future use)
def detect_mod_type(folder):
    types = []
    for mod in KNOWN_MODS:
        if mod.lower() in folder.lower():
            types.append(mod)
    return types

# Scan log file for common errors
def scan_log_for_errors(log_path, log_output):
    if not os.path.exists(log_path):
        log_output.append(f"⚠ Log file not found: {log_path}")
        return
    log_output.append(f"🔎 Scanning log: {log_path}")
    with open(log_path, "r", encoding="utf-8", errors="ignore") as log:
        for line in log:
            if any(keyword in line.lower() for keyword in ["fatal", "error", "nil", "attempt to call"]):
                log_output.append(f"❗ {line.strip()}")

# GUI for drag-and-drop and user interaction
def launch_gui():
    def choose_folder():
        folder = filedialog.askdirectory(title="Select your STALKER gamedata folder")
        if folder:
            start_scan(folder)

    def start_scan(folder):
        scan_thread = threading.Thread(target=run_fix, args=(folder, scan_all.get()))
        scan_thread.start()

    def run_fix(folder, scan_all_files):
        btn.config(state="disabled")
        cancel_btn.config(state="normal")
        file_list.delete(0, tk.END)
        log_output = []
        stop_flag[0] = False

        mods = detect_mod_type(folder)
        if mods:
            messagebox.showinfo("Mod Detected", f"Detected mods: {', '.join(mods)}")

        files = list(get_all_valid_files(folder) if scan_all_files else get_recent_files(folder))
        progress_bar["maximum"] = len(files)

        for i, path in enumerate(files):
            if stop_flag[0]:
                log_output.append("⛔ Scan cancelled. Reverting changes is manual via backups.")
                break
            msg = fix_file(path, folder)
            file_list.insert(tk.END, msg)
            file_list.yview_moveto(1)
            progress_bar["value"] = i + 1
            root.update_idletasks()

        log_path = os.path.join(os.path.dirname(folder), "logs", "xray.log")
        scan_log_for_errors(log_path, log_output)

        # Save logs
        logs_dir = os.path.join(os.path.dirname(folder), "stalkerscriptsfixer logs")
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, f"scan_log_{time.strftime('%Y-%m-%d_%H-%M-%S')}.txt")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("\n".join(log_output))

        cancel_btn.config(state="disabled")
        btn.config(state="normal")
        messagebox.showinfo("Done", "All suspicious lines have been reviewed or patched.")

    def cancel_scan():
        stop_flag[0] = True

    root = tk.Tk()
    root.title("STALKER Auto Fixer")
    root.geometry("640x480")
    root.resizable(False, False)

    lbl = tk.Label(root, text="Drop your STALKER 'gamedata' folder", font=("Arial", 12))
    lbl.pack(pady=10)

    scan_all = tk.BooleanVar(value=False)
    chk = tk.Checkbutton(root, text="Scan all files (not just recent ones)", variable=scan_all, font=("Arial", 10))
    chk.pack()

    btn = tk.Button(root, text="Select Folder", command=choose_folder, font=("Arial", 11))
    btn.pack(pady=10)

    cancel_btn = tk.Button(root, text="Cancel Scan", command=cancel_scan, state="disabled", font=("Arial", 10))
    cancel_btn.pack()

    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progress_bar.pack(pady=10)

    file_list = tk.Listbox(root, width=80, height=15, font=("Courier", 8))
    file_list.pack(pady=10)

    stop_flag = [False]
    root.mainloop()

# Entry point
def main():
    if len(sys.argv) < 2:
        launch_gui()
    else:
        folder = sys.argv[1]
        print(f"🔍 Scanning: {folder}")
        mods = detect_mod_type(folder)
        if mods:
            print(f"📦 Detected mods: {', '.join(mods)}")

        for path in get_recent_files(folder):
            print(fix_file(path, folder))

        log_output = []
        log_path = os.path.join(os.path.dirname(folder), "logs", "xray.log")
        scan_log_for_errors(log_path, log_output)

        logs_dir = os.path.join(os.path.dirname(folder), "stalkerscriptsfixer logs")
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, f"scan_log_{time.strftime('%Y-%m-%d_%H-%M-%S')}.txt")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("\n".join(log_output))

        print("\n✅ Done. All suspicious lines have been reviewed or patched.")

if __name__ == "__main__":
    main()
