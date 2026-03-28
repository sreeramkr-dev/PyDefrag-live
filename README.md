# Disk_Defragmentation_Utility_live
An Interactive python script that uses the `e4defrag ` utility as backend


## ⚠BACKUP BEFORE RUNNING⚠
 This tool runs as root and modifies system files,ensure you have backed up the files to be safe in case of error
 ## Requirements
 * **Operating systems** : Linux based operating systems(Debian,Ubuntu,Linux Mint,.....)

 
* **Filesystem** : Only EXT4 filesystem supported


### **Dependencies**
* `e2fsprongs` 
* `python 3.10 ` 
## Usage
Download the file **`code.py`**
run code.py in terminal

```bash
python3 code.py
```
The utility will ask for the sudo password the tool needs it for accessing system files and modifying fragmented files
