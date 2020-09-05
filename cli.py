# Import modules
import argparse
import core.twilight as twilight


# Main
if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(description = "Encrypt/Decrypt you data with Key & Salt")
    parser.add_argument("-e", "--encrypt", type = str, metavar = "<DATA>", help = "Your string to be encrypted.", required = False)
    parser.add_argument("-d", "--decrypt", type = str, metavar = "<DATA>", help = "Your string to be decrypted.", required = False)
    parser.add_argument("-k", "--key",  type = str, metavar = "<KEY>", help = "Your encryption key.", required = True)
    args = parser.parse_args()

    dtext = args.decrypt
    etext = args.encrypt
    key   = args.key

    if(dtext):
        print("Decrypted value: " + twilight.Decrypt(dtext, key))
    elif(etext):
        print("Encrypted value: " + twilight.Encrypt(etext, key))
    else:
        print("Select mode: --encrypt \"string\" or --decrypt \"string\"")