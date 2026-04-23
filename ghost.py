import json
import os
import re
import argparse
import time

def draw_banner():
    # Force clear terminal before showing logo for maximum impact
    os.system('clear')
    banner = r"""
    [!] ========================================== [!]
    
      ██████  ██   ██  ██████  ███████ ████████ 
     ██       ██   ██ ██    ██ ██         ██    
     ██   ███ ███████ ██    ██ ███████    ██    
     ██    ██ ██   ██ ██    ██      ██    ██    
      ██████  ██   ██  ██████  ███████    ██    
                                                
    [!] SESSION GHOST - AI CONTEXT INJECTOR
    [!] DEVELOPED FOR SESSION MIGRATION & REHYDRATION
    [!] ========================================== [!]
    """
    print("\033[91m" + banner + "\033[0m") 
    time.sleep(0.5) # Small delay so you see the logo before the list loads

def clean_noise(text):
    code_blocks = re.findall(r'```.*?```', text, re.DOTALL)
    placeholder = "[[CODE_BLOCK]]"
    temp_text = re.sub(r'```.*?```', placeholder, text, flags=re.DOTALL)

    noise_patterns = [
        r"I understand your request",
        r"Certainly!",
        r"I can help with that",
        r"Here is the code",
        r"Let me know if you have questions",
        r"I hope this helps",
        r"Please find the updated version",
        r"Sure, I can assist",
        r"Feel free to ask",
        r"Based on your requirements"
    ]
    
    for pattern in noise_patterns:
        temp_text = re.sub(pattern, "", temp_text, flags=re.IGNORECASE)

    for block in code_blocks:
        temp_text = temp_text.replace(placeholder, block, 1)

    temp_text = re.sub(r'\n{3,}', '\n\n', temp_text)
    return temp_text.strip()

def process_session(input_file):
    draw_banner()
    
    if not os.path.exists(input_file):
        print(f"\033[91m[-] FILE NOT FOUND: {input_file}\033[0m")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[-] JSON ERROR: {e}")
        return

    conversations = data if isinstance(data, list) else data.get('conversations', [])
    
    print(f"[*] TOTAL SESSIONS DETECTED: {len(conversations)}\n")
    for i, conv in enumerate(conversations):
        title = conv.get('name') or conv.get('title') or "Untitled_Log"
        print(f"  [{i}] {title}")

    try:
        choice = int(input("\n[?] TARGET ID TO GHOST: "))
        selected_conv = conversations[choice]
    except:
        print("\033[91m[-] INVALID TARGET SELECTION.\033[0m")
        return
    
    payload = "[SYSTEM_STATE_RESUME]\n" + "="*40 + "\n"
    msgs = selected_conv.get('chat_messages') or selected_conv.get('messages') or []

    for msg in msgs:
        role = str(msg.get('sender', 'unknown')).upper()
        content = msg.get('text') or msg.get('content') or ""
        if content:
            refined_content = clean_noise(content)
            if refined_content:
                payload += f"### {role}:\n{refined_content}\n\n"

    with open("resume_payload.txt", 'w', encoding='utf-8') as f:
        f.write(payload)

    print(f"\n\033[92m[+] SUCCESS: PAYLOAD COMPRESSED AND EXPORTED TO 'resume_payload.txt'\033[0m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="conversations.json")
    args = parser.parse_args()
    process_session(args.input)