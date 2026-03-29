# PyDefrage-live 
**Version 1.0.0**


An Interactive python script that uses the `e4defrag ` utility as backend


## ⚠BACKUP BEFORE RUNNING⚠
 This tool runs as root and modifies system files,ensure you have backed up the files to be safe in case of error
 ## Requirements
 * **Operating systems**: Linux based operating systems (Debian, Ubuntu , Linux Mint, etc.....)
 * **Root access**: You need root access to modify system files
 *  **Filesystem**: Only EXT4 filesystem supported


### **Dependencies**
* `e2fsprogs`
* `python 3.10+`
### Ubuntu / Debian / Mint:
```bash
sudo apt update && sudo apt install e2fsprogs
```
### Fedora (RHEL based distros):
```bash
sudo dnf install e2fsprogs
```
## Usage
Download the utility
```bash
wget https://raw.githubusercontent.com/sreeramkr-dev/PyDefrag-live/main/code.py
```
Alternatively you can download code.py directly


run code.py in terminal

```bash
python3 code.py
```
The utility will ask for the sudo password,the tool needs it for accessing system files and modifying fragmented files
## v.1.0.0 Release notes
### Known issues
* **Path Expansion**: The utility currently requires full path as input (eg;`/home/<username>`)
* **Shell expansion using**: `~` is currently not supported


**Usage Note**: Please provide full paths for accurate analysis

This issue will be fixed in the future versions
