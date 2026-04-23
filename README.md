

#  Session Ghost
### **[!] SESSION GHOST - AI CONTEXT INJECTOR**
### **[!] DEVELOPED FOR SESSION MIGRATION & REHYDRATION**

**Session Ghost** is a specialized CLI utility designed for security researchers and power users who need to migrate complex AI chat sessions between accounts. 

Standard chat exports are bloated with metadata that wastes "Context Window" space. Session Ghost solves this by surgically extracting the core dialogue and logic, stripping away token-wasting noise to ensure you have the maximum space available for your code and technical research.

---

##  Core Optimization Features
* **Metadata Stripping:** Automatically removes timestamps, unique message IDs, and sender metadata that consume unnecessary tokens.
* **Noise Reduction:** Filters out common AI filler phrases (e.g., "I understand your request," "Certainly!").
* **Logic Preservation:** Protects all code blocks (triple backticks) to ensure technical accuracy remains 100% during migration.
* **Payload Compression:** Consolidates hundreds of messages into a single "State Resume" payload.

---

## 🛠️ The "Ghost Protocol" Workflow

### 1. Data Acquisition (Claude.ai)
1.  Open **Claude Settings** > **Data Export**.
2.  Request your export and download the `.zip` file from your email.
3.  Place the `.zip` file in your `~/Downloads` folder.

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/mountainaddict0/SessionGhost.git

# Enter the directory
cd SessionGhost
```

### 3. Execution (From Scratch)
Run these commands in order to process your export:

```bash
# 1. Clean previous workspace
rm -f conversations.json resume_payload.txt

# 2. Extract only the required database file from the zip
# Replace 'export.zip' with your actual filename
unzip ~/Downloads/export.zip conversations.json

# 3. Initialize the Ghost Injector
python3 ghost.py
```

---

## 📂 Usage
1.  Upon launch, the tool will display the **Red Ghost Banner** and a list of your archived sessions.
2.  Select the **ID Number** of the session you want to migrate.
3.  The tool generates `resume_payload.txt` in your directory.
4.  Copy the content: `cat resume_payload.txt | xclip -selection clipboard` (or use manual copy).
5.  Paste the payload into a **New Session** to resume work with zero context loss.

---

##  Security & Privacy
* **Local Processing:** Your conversation data never leaves your machine.
* **Privacy Guard:** The included `.gitignore` ensures that your `conversations.json` and `resume_payload.txt` are never uploaded to GitHub.

