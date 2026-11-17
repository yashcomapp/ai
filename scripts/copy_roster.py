import sys
import os
import subprocess

def copy_image_to_clipboard(image_path):
    if not os.path.exists(image_path):
        print(f"Error: File not found: {image_path}")
        return False
    
    # PowerShell STA command to load image into Windows Clipboard
    cmd = [
        "powershell",
        "-STA",
        "-NoProfile",
        "-Command",
        f"Add-Type -AssemblyName System.Windows.Forms; "
        f"$img = [System.Drawing.Image]::FromFile('{image_path}'); "
        f"[System.Windows.Forms.Clipboard]::SetImage($img); "
        f"$img.Dispose(); "
        f"Write-Host 'Copied {os.path.basename(image_path)} to clipboard!'"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(res.stdout.strip())
        return True
    else:
        print("Error copying to clipboard:", res.stderr)
        return False

if __name__ == "__main__":
    cls = sys.argv[1] if len(sys.argv) > 1 else "8"
    base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\los-next"
    target = os.path.join(base_dir, f"Class_{cls}_Diwali_Vacation_Roster_HD.png")
    copy_image_to_clipboard(target)
