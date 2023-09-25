import sys
import subprocess

print("🐶 Chester - Setup")
print("Starting...")
print()

#### Step 1
try:
    returnStr = subprocess.run("git branch changelog", capture_output=True, text=True,check=True,shell=True)
    returnStr.check_returncode()
except subprocess.CalledProcessError: 
    print("(X) Couldn't create git branch 'changelog'") 
except Exception:
    print("(X) Unknown error occured [SOURCE: Git-Branch-Creation].")
print("Step 1: (i) Successful.")
####

print("...Stopping")
sys.exit()