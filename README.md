# STALKER-Scripts-Fixer
 Auto-fixer for S.T.A.L.K.E.R. mods (Anomaly,GAMMA, EFP, Radiophobia series and Stalker  Anthalogy OBT) to prevent script crashes. Lua/LTX auto-fixer with drag-and-drop GUI and log error scan.
 
///////////////////////////////////

# STALKER Auto Fixer 🛠️

An automatic script error patcher for major **S.T.A.L.K.E.R.** modpacks like **GAMMA**, **EFP**, and **Anthalogy 2.0 OBT**.

It scans your `gamedata` folder for modified `.script`, `.ltx`, `.ini`, `.xml`, and `.txt` files and wraps **risky function calls** with safety checks. The tool helps prevent fatal engine crashes and ensures smoother gameplay even after modding or tweaking files.

---

## 🔧 Features

- ✅ Detects and scans recently modified files
- ✅ Auto-wraps vulnerable Lua calls like `r_nvg.toggle_nightvision`
- ✅ Works with most major STALKER modpacks
- ✅ Creates automatic `.bak` backups before patching
- ✅ Lightweight and uses very little RAM
- ✅ Open source and modder-friendly

---

## ⚙️ How It Works

This script automatically:
1. Scans recent files in your `gamedata` folder.
2. Looks for known risky function calls (e.g., night vision toggles, missing inventory handlers).
3. Wraps them in safe `if type(...) == "function"` checks to prevent nil crashes.
4. Backs up any changed file before fixing.

🚀 Usage
python stalker_fixer.py /path/to/gamedata
--This will recursively scan and fix script/config files in the target folder.

📦 Supported Mods (and growing):
-GAMMA (Anomaly-based)
-EFP (Expanded Factions Project)
-STALKER Anthalogy 2.0+ OBT

 Others (open a GitHub Issue or PR for requests!)

 🧠 Modder Tips:
Place this tool in your root STALKER mod directory

Run it after every mod install or script change

Use version control (like Git) to track changes

Do not run it blindly if you manually wrote complex Lua logic — always review changes

💾 Low RAM Usage
This script:

Avoids loading massive files in memory

Skips files over 5MB

Uses generator-style iteration

Ideal for low-spec machines and older PCs used for modding

📁 Where are backups saved?
NOTE: Backups are saved in 'backups' folder inside base directory (not gamedata) to prevent conflicts.

✅ Example:
If the original script is:

You can manually compare, restore, or delete the files anytime.

👥 Contributing
Pull requests welcome!

If you’re a STALKER modder or Lua nerd, help improve:

Detection logic

Wrap patterns

GUI frontend (optional future goal)

Error logging and UI feedback

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

