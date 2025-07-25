# STALKER Auto Fixer 🛠️

An automatic Lua/LTX error patcher for major **S.T.A.L.K.E.R.** modpacks like **GAMMA**, **EFP**, **Radiophobia 3**, and **Anomaly Anthalogy 2.0 OBT**.

This tool scans your `gamedata` folder (or full mod directory), detects risky script patterns, and applies safe auto-fixes to help prevent crashes. It comes with a drag-and-drop GUI, live scan status, and full logging/backup support.

---

## 🔧 Features

✅ Drag-and-drop GUI for folders or files  
✅ Checkbox to scan **entire gamedata** or just recently modified files  
✅ Supports `.script`, `.ltx`, `.ini`, `.xml`, and `.txt` files  
✅ Live list of scanned files shown during scan  
✅ Safe auto-wraps for Lua functions like `r_nvg.toggle_nightvision`, `actor:give_info_portion()`  
✅ **Auto backup** with versioned timestamps (before any changes)  
✅ **SHA-256 log and patch integrity check**  
✅ Threaded scanning (no freezing)  
✅ Revert all changes with cancel button  
✅ Auto-saves logs to `stalkerscriptsfixer logs/`  
✅ Option to open logs in Notepad or Notepad++  
✅ Open-source, community-rule friendly (`fix_rules.json`)  

---

## ⚙️ How It Works

The tool:

1. Scans `.script`, `.ltx`, `.ini`, `.xml`, and `.txt` files in `gamedata` or entire mod directory  
2. Looks for known **risky Lua or LTX functions** (customizable via `fix_rules.json`)  
3. Auto-wraps with safe `if type(...) == "function"` guards  
4. Creates timestamped `.bak` versions of every edited file  
5. Displays live progress in GUI  
6. Saves logs with scan results, file paths, and backups  

---

## 🚀 How to Use

### Drag-and-Drop Mode (Recommended)

1. Run `StalkerScriptFixer.exe`  
2. Drag your **`gamedata` folder** or **entire mod directory** onto the window  
3. Check `Scan Entire Gamedata` if needed  
4. Click `Start Scan`  
5. Monitor live progress, or click `Cancel & Revert` at any time

---

## 🗂️ Where Are Backups and Logs Stored?

- 🔙 **Backups**:  
  Saved to a separate `backups/` folder (not inside `gamedata`)  
  e.g., `backups/2025-07-25_18-40-15/scripts/broken.script.bak`

- 📝 **Logs**:  
  All scans saved to `stalkerscriptsfixer logs/scan_log.txt`  
  Older logs and backup logs go to `stalkerscriptsfixer logs/old logs/`

- 🧾 **Open Logs**:
  After scan, click `Open Log` to view it in Notepad or Notepad++ (if installed)

---

## 📦 Supported Mods (growing list)

- [x] GAMMA  
- [x] EFP (Expanded Factions Project)  
- [x] Radiophobia 3  
- [x] Anomaly Anthalogy 2.0 OBT  
- [x] Any Anomaly-based modpack  
- [ ] Your pack? Open a GitHub Issue or submit a `fix_rules.json` PR!

---

## 💬 Modder-Friendly

- `fix_rules.json` allows you to define or suggest your own patch patterns  
- Tool does not overwrite files without `.bak` backups  
- Designed for safety — no blind rewrites of custom Lua  
- Helpful during debugging script crashes

---

## 🔐 Integrity Check

- Each `.bak` file and patched file is logged with **SHA-256 hashes**  
- Prevents tampering and allows rollback/verification of changes

---

## 💾 Ideal for Low-End PCs

- Low memory footprint  
- Skips huge files (>5MB)  
- Threaded scanning keeps GUI responsive  
- Can run during modding sessions without game restart
- 
---
## 💖 Support This Project

If you find this tool helpful, consider supporting it:

[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mesharie)
---

## 🛠️ Manual CLI Usage (Advanced)

```bash
python stalker_fixer.py path/to/gamedata
Add --fullscan to check entire gamedata

Add --log-only to only scan and report errors (no fixing)

📢 GitHub Releases
We recommend downloading the .exe from GitHub Releases (upload manually if building from source).

✅ Example
Before:

lua
Copy
Edit
r_nvg.toggle_nightvision()
After:

lua
Copy
Edit
if r_nvg and type(r_nvg.toggle_nightvision) == "function" then
    r_nvg.toggle_nightvision()
end
💡 Tip: Run After Modding!
Always run this tool after:

Installing a new mod

Making LTX or Lua edits

Seeing frequent crash logs about nil, attempt to call, or similar

🧠 Credits
Built with ❤️ for the S.T.A.L.K.E.R. modding community.
Open for collaboration and modpack-specific rules.
🛡️ License
MIT License — free to use, share, and improve.

FURTHERMORE:
contact me at mangganern2023@gmail.com
if you want your project to be supported by my work.

:) Happy Hunting Stalker!

/////////////////////////////////// 

Example auto-patch:
```lua
-- Before
r_nvg.toggle_nightvision()

-- After
if type(r_nvg) == "table" and type(r_nvg.toggle_nightvision) == "function" then
    r_nvg.toggle_nightvision()
end
///////////////////////////////////

