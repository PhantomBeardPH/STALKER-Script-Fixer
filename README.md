# STALKER-Scripts-Fixer
 Auto-fixer for S.T.A.L.K.E.R. mods (Anomaly,GAMMA, EFP, Radiophobia series and Stalker  Anthalogy OBT) to prevent script crashes. 
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

Example auto-patch:
```lua
-- Before
r_nvg.toggle_nightvision()

-- After
if type(r_nvg) == "table" and type(r_nvg.toggle_nightvision) == "function" then
    r_nvg.toggle_nightvision()
end
