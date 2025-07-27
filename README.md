Project Title: STALKER Auto Fixer 🛠️
Objective: To build an automatic Lua/LTX error patching tool for major S.T.A.L.K.E.R. modpacks like GAMMA, EFP, Radiophobia 3, and Anomaly Anthalogy 2.0 OBT.

🧠 Project Goal
To scan and automatically fix risky scripting patterns across gamedata or mod folders by:

Detecting problematic Lua/LTX logic

Wrapping them with safe guards

Maintaining backups and logs

Reducing mod crashes for both developers and players

✅ Planned Features
Core Functionality
🔍 Scans .script, .ltx, .ini, .xml, .txt files

📂 Drag-and-drop GUI for folders or files

📌 Option to scan entire gamedata or only recently modified files

⚙️ Fixes risky Lua patterns like:

r_nvg.toggle_nightvision()

actor:give_info_portion()
(Auto-wraps with safe guards like if type(...) == "function")

🧾 Auto-backup with timestamped .bak files before changes

🧠 Detectable rules defined in fix_rules.json (fully modder-extensible)

GUI and UX
🖱️ Intuitive drag-and-drop interface

🟩 Live scanning status (file list updating during scan)

🔧 Cancel button to revert all changes

🗒️ Log viewer (opens in Notepad or Notepad++ if available)

💬 Display of scan results, patched files, and backup paths

Integrity & Safety
🔒 SHA-256 hash logging for each modified and backed-up file

🧯 No overwrite without .bak safety

🧠 Low memory usage and skips huge files >5MB

🧵 Threaded scanning for a freeze-free experience

🗂️ Output Structure
Backups Folder:

backups/YYYY-MM-DD_HH-MM-SS/

e.g., backups/2025-07-25_18-40-15/scripts/broken.script.bak

Logs Folder:

stalkerscriptsfixer logs/scan_log.txt

Older logs: stalkerscriptsfixer logs/old logs/

🧪 How It Works (Summary)
User drops a folder (e.g., gamedata/)

Program scans all script/config files

Identifies risky Lua/LTX code

Applies safe patches

Saves logs + backups

User can review, revert, or keep changes

💬 Mod Support
Confirmed Supported Modpacks:
 GAMMA

 EFP

 Radiophobia 3

 Anomaly Anthalogy 2.0 OBT

 All Anomaly-based modpacks

 Others — submit your fix_rules.json or request support via email

🛠 Planned Extras
🧰 Developer Mode: Verbose debugging logs

🔄 Auto-update checker (non-intrusive)

🌐 GitHub integration for rule submissions

📊 Export .json + .log reports for mod authors

👤 CLI fallback mode: python stalker_fixer.py path/to/gamedata --fullscan

🔐 Security Plan
Each edit is SHA-256 hashed and logged

Prevents silent tampering

Encourages transparency and rollback safety

Backup-first principle on all operations

💻 Optimization Goals
Designed for low-end PCs

Light on RAM and CPU

Multi-threaded scan engine

No restarts required — safe to run between modding sessions

🧑‍🔧 Developer Collaboration
All patch logic stored in fix_rules.json

Developers can submit rules via pull requests

No blind rewrites; only clearly scoped pattern patches

Built with open-source values and respect for mod authors

🔎 Example Auto-Patch
lua
Copy
Edit
-- Before
r_nvg.toggle_nightvision()

-- After
if type(r_nvg) == "table" and type(r_nvg.toggle_nightvision) == "function" then
    r_nvg.toggle_nightvision()
end
📫 Contact
Want your modpack officially supported?
Got a rule to suggest or bug to report?

📧 Email: mangganern2023@gmail.com

⚖️ License
MIT License — Free to use, share, modify.
Open to collaboration. Made with ❤️ for the S.T.A.L.K.E.R. modding community.

🏁 Milestone Status (as of planning)
Task	Status
GUI base built	✅ Done
Core scanning engine	✅ Done
Rule engine via fix_rules.json	✅ Done
Logging and backup system	✅ Done
Drag & Drop support	✅ Done
Auto-hash logging	✅ Done
Modpack profile support	🔄 In Progress
Developer Mode	🔄 Planned
CLI mode	🔄 Planned
Auto-updater	❌ Future Feature



