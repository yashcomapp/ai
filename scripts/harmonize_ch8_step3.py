# scripts/harmonize_ch8_step3.py
import json
import re

with open('backups/staging/mh9_scit_8_enhanced.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} questions from staging")

# We will inspect each question and harmonize Step 3
fixed_count = 0

for idx, q in enumerate(questions):
    q_type = q['type']
    ans = q['correctAnswer']
    sol = q['solution']
    opts = q['options']
    
    # Split solution into headers
    parts = re.split(r'(### [123]\.[^\n]*)', sol)
    # parts will contain: ['', '### 1. ...', text1, '### 2. ...', text2, '### 3. ...', text3]
    if len(parts) < 7:
        print(f"Skipping Q{idx+1} ({q['questionCode']}): parts length {len(parts)}")
        continue
        
    h1 = parts[1]
    b1 = parts[2]
    h2 = parts[3]
    b2 = parts[4]
    h3 = parts[5]
    b3 = parts[6]
    
    if q_type == 'OSC':
        correct_letter = ans.strip().upper()
        letters = ['A', 'B', 'C', 'D']
        
        # Check if Step 3 currently has lines analyzing options
        # We want Step 3 to have clean:
        # - **Option A is ...**
        # - **Option B is ...**
        # - **Option C is ...**
        # - **Option D is ...**
        
        # Let's extract existing explanations for each concept/option in b3
        # Look for bullet points
        bullets = [line.strip() for line in b3.split('\n') if line.strip().startswith('-')]
        
        # Build a mapping of content from existing bullets
        content_by_keyword = {}
        for b in bullets:
            # clean bullet
            content_by_keyword[b] = b
            
        # Let's see if the correct letter in b3 already matches correct_letter
        correct_match = re.search(r'Option ([A-D])[^a-zA-Z]*(?:is\s+)?correct', b3, re.IGNORECASE)
        
        needs_fix = False
        if not correct_match:
            needs_fix = True
        elif correct_match.group(1).upper() != correct_letter:
            needs_fix = True
            
        if needs_fix:
            fixed_count += 1
            # Reconstruct Step 3 lines to match the actual options of q
            # For each option A, B, C, D:
            new_step3_lines = []
            
            # Find which old bullet corresponds to correct answer
            old_correct_bullet = None
            old_incorrect_bullets = []
            for b in bullets:
                if re.search(r'correct', b, re.IGNORECASE) and not re.search(r'incorrect', b, re.IGNORECASE):
                    old_correct_bullet = b
                else:
                    old_incorrect_bullets.append(b)
            
            # Clean old_correct_bullet text
            correct_explanation = ""
            if old_correct_bullet:
                # Strip leading prefix like "- **Option X is correct.**" or "- **Option X (text):** Correct."
                clean_exp = re.sub(r'^-\s*\*\*Option\s*[A-D][^\*]*\*\*[:\.\s]*(?:Correct\.?|is correct\.?)\s*', '', old_correct_bullet, flags=re.IGNORECASE).strip()
                correct_explanation = clean_exp
            if not correct_explanation:
                correct_explanation = f"{opts[ord(correct_letter)-65]} is the scientifically accurate answer."
                
            for opt_idx, letter in enumerate(letters):
                opt_text = opts[opt_idx]
                if letter == correct_letter:
                    new_step3_lines.append(f"- **Option {letter} is correct.** {correct_explanation}")
                else:
                    # Find a matching incorrect explanation or construct a solid one
                    found_exp = ""
                    for b in old_incorrect_bullets:
                        # If old bullet mentions opt_text or parts of it
                        # or if old bullet was for this specific distractor
                        opt_words = [w for w in re.findall(r'[a-zA-Z]{4,}', opt_text) if w.lower() not in ['this', 'that', 'with', 'from', 'these', 'have', 'been', 'which']]
                        if any(w.lower() in b.lower() for w in opt_words):
                            clean_b = re.sub(r'^-\s*\*\*Option\s*[A-D][^\*]*\*\*[:\.\s]*(?:Incorrect\.?|is incorrect\.?)\s*', '', b, flags=re.IGNORECASE).strip()
                            found_exp = clean_b
                            break
                    if not found_exp and old_incorrect_bullets:
                        # Pop an unused incorrect bullet if available
                        clean_b = re.sub(r'^-\s*\*\*Option\s*[A-D][^\*]*\*\*[:\.\s]*(?:Incorrect\.?|is incorrect\.?)\s*', '', old_incorrect_bullets.pop(0), flags=re.IGNORECASE).strip()
                        found_exp = clean_b
                    if not found_exp:
                        found_exp = f"'{opt_text}' does not correctly describe the biological phenomenon in this context."
                        
                    new_step3_lines.append(f"- **Option {letter} is incorrect.** {found_exp}")
                    
            # Update b3
            new_b3 = "\n" + "\n".join(new_step3_lines) + "\n"
            parts[6] = new_b3
            q['solution'] = "".join(parts[1:])
            
    elif q_type == 'OAR':
        # Ensure Step 3 ends with "- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion."
        if not re.search(r'Option A is correct', b3, re.IGNORECASE):
            parts[6] = b3.rstrip() + "\n- **Option A is correct.** Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.\n"
            q['solution'] = "".join(parts[1:])
            fixed_count += 1

print(f"Harmonized {fixed_count} questions in Step 3")

with open('backups/staging/mh9_scit_8_enhanced.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print("Updated backups/staging/mh9_scit_8_enhanced.json successfully!")
