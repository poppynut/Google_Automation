import pexpect

def main():
    print("Entered.")
    child = pexpect.spawn('ssh root@192.168.0.1')
    print("Finished.")

if __name__ == '__main__':
    main()