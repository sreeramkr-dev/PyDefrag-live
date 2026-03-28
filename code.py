import subprocess
print("The input should not been in qoutes")
print("Note that only ext4 filesystem is supported ")
target=input("Enter the target :")
check_fragementation=['sudo','e4defrag','-c',target]
result=subprocess.run(check_fragementation,capture_output=True,text=True)
if result.stderr:
    print(f"Error:{result.stderr.strip()}")
else:
   print(result.stdout)
while True:
    try:
        start_defrage=input("Do you want to start defragementaion [Y/n] : ")
        break
    except ValueError:
        print("choose correct options")
if start_defrage in 'Yy':
    do_defragementation=['sudo','e4defrag',target]
    subprocess.run(do_defragementation)
print('-'*74)            
