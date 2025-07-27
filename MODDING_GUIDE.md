# 🛠 Modding Guide Plan for STALKER Scripts Fixer v1.0
///////////
--Example
//////////
This guide helps modders and contributors extend the features of STALKER Scripts Fixer, especially by adding new auto-fix patterns or improving localization.

---

## 🔧 Adding New Auto-Fix Rules

If you want to define new fix rules (e.g., known broken script patterns or CTD lines), edit or add to the fix logic in the `src/main.py` or similar script file.

You can optionally suggest using a future `fix_rules.json` file (planned feature) with this sample format:

```json
[
  {
    "pattern": "r_nvg\\.set_nightvision_animated",
    "wrap_if_type": true,
    "comment": "-- FIXED: safer nightvision function"
  },
  {
    "pattern": "some_function\\(\\)",
    "replace_with": "safe_wrapper(some_function)",
    "comment": "-- AUTO-WRAPPED"
  }
]

--This allows you to add logic without touching the core script directly.

🧪 Testing Your Fixes
If contributing auto-fixes:
    • Drop a ‘gamedata’ folder into the GUI.
    • Check the log output window to see which lines were fixed.

🤝 Contributing
    1. Fork the repository
    2. Make changes in your own branch
    3. Submit a pull request with a clear description of your changes

📫 Contact
For suggestions or bug reports:
📧 mangganern2023@gmail.com
🔖 Maintainer: PhantomBeardPH
//////////
