# 🛠 STALKER Script Fixer - Modding Guide
///////////
--Example
//////////
# Introduction
//////////
This guide explains how you can modify and extend the STALKER Script Fixer to create your own versions while respecting the original author's conditions. Please read this guide carefully before making any modifications.
---

# 🔧 Permitted Modifications

✅ What You CAN Change

    1. Language Support
        ◦ Add new language translations by creating JSON files in the languages folder
        ◦ Follow the format specified in the README.md
        ◦ Add your language to the SUPPORTED_LANGUAGES list (line 199)
    2. UI Customization
        ◦ Modify colors and themes by changing the DEFAULT_BG_COLOR and related settings
        ◦ Adjust window sizes and layouts in the UI setup code
    3. Game/Mod Support
        ◦ Add support for additional STALKER mods by extending:
            ▪ SUPPORTED_GAMES list
            ▪ GameVersion enum
        ◦ Add mod-specific fixes in the fix_file() method
    4. Script Fixing Rules
        ◦ Add new script fixing rules in the fix_file() method
        ◦ Extend support for additional file types (.xml, .cfg, etc.)
    5. XRay Log Analysis
        ◦ Improve error pattern matching in extract_last_fatal_error()
        ◦ Add more file reference patterns in extract_file_references()
    6. Local Features
        ◦ Add features that don't require external services
        ◦ Extend backup functionality
        ◦ Add new file scanning capabilities
        
# ⚠️ Restricted Modifications

❌ What You CANNOT Change

    1. Core Attribution
        ◦ You must keep all original author credits and copyright notices
        ◦ Do not remove or obscure the "PhantomBeardPH" attribution
    2. License Conditions
        ◦ You may not remove the disclaimer about "EMOTIONAL DAMAGES"
        ◦ The support email and donation link must remain visible
    3. AI Functionality
        ◦ If redistributing with OpenAI API integration:
            ▪ Users must provide their own API keys
            ▪ You may not bundle or hardcode API keys
        ◦ The token limit warning (400 tokens) must remain
    4. Safety Features
        ◦ Backup functionality must remain intact
        ◦ Warning messages about potential risks cannot be removed
    5. Project Identity
        ◦ The "STALKER Script Fixer" name must remain in the title
        ◦ Version numbering should clearly distinguish from official releases

# 💻 Implementation Guidelines

🧠 Adding New Features

1.) For UI:
  # Example: Adding a new button
///
  self.new_feature_button = ttk.Button(button_frame, 
                                   text="New Feature",
                                   command=self.new_feature_method)
  self.new_feature_button.pack(side=tk.LEFT, padx=5)
///

2.) For Script Fixes:
  # Example: Adding a New LTX Fix rule
///
  if file_path.endswith('.ltx'):
    # New fix: ensure no trailing whitespace
    original_content = content
    content = "\n".join(line.rstrip() for line in content.splitlines())
    if content != original_content:
        fixes.append("Removed trailing whitespace")
///

3.) For New Mod Support:

///
# 1. Add to SUPPORTED_GAMES
SUPPORTED_GAMES = [..., "New Mod Name"]

# 2. Add to GameVersion enum
class GameVersion(Enum):
    NEW_MOD = "New Mod Name"

# 3. Add mod-specific fixes
if self.settings.game_version == "New Mod Name":
    # Add mod-specific fixes here
///

# 📦 Distribution Requirements

       If you distribute a modified version:
    1. Clearly state it's a modified version
    2. Include a link to the original project
    3. Keep all original warnings and disclaimers
    4. Do not charge money for the modified version
    5. Provide your contact information for support
    
# 📝 Best Practices

       Versioning: Use your own version scheme (e.g., "Community Edition v1.0")
    1. Documentation: Clearly document your changes in a CHANGELOG.md
    2. Testing: Thoroughly test all modifications before distribution
    3. Attribution: Credit both the original author and your contributions
    4. Compatibility: Ensure your changes don't break existing functionality
    
# 🚧 SUPPORT BOUNDARIES

       The original author is not responsible for supporting modified versions
    1. Community support should be clearly distinguished from official support
    2. Modified versions should provide their own support channels

# 💡 Example Modding Scenario

       Goal: Add support for "Lost Alpha" mod
    1. Add to supported games:
ex.
///
  python
SUPPORTED_GAMES = [..., "Lost Alpha"]
///

    2. Add to GameVersion enum:

///
class GameVersion(Enum):
    LOST_ALPHA = "Lost Alpha"
///

    3. Add specific fixes:
    
///
if self.settings.game_version == "Lost Alpha":
    if file_path.endswith('.ltx'):
        # Lost Alpha specific LTX fixes
        if "[la_section]" in content:
            content = content.replace("[la_section]", "[lostalpha_section]")
            fixes.append("LA section rename")
/// -- ⚠️ Remember to test thoroughly and document your changes!

# 📝 Final Notes

       Not hold the original author responsible for any issues
    • Clearly credit the original work
    • Respect the boundaries outlined in this guide
    • Share improvements with the community when possible



  
Happy modding! 🚀





