# PyDefrage-live 
**Version 1.0.0**


An Interactive python script that uses the `e4defrag ` utility as backend


## ⚠BACKUP BEFORE RUNNING⚠
 This tool runs as root and modifies system files,ensure you have backed up the files to be safe in case of error
 ## Requirements
 * **Operating systems** : Linux based operating systems(Debian,Ubuntu,Linux Mint,.....)

 
* **Filesystem** : Only EXT4 filesystem supported


### **Dependencies**
* `e2fsprongs`
* `python 3.10 >` 
```bash
sudo apt update && sudo apt install e2fsprogs
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
## Release notes
You need to type proper file paths eg: `~` will not work you need to type `/home/<username>` dont analyze the home directory

This issue will be fixed in the future versions
