# for tool name include this package
from pyfiglet import figlet_format


def crypto():
    # encryption
    def encrypt():
        # get input from the user
        plaintxt = input("Enter the text to be encrypted:")

        # empty string to manipulate the original text
        ciphertxt = ""

        # main logic
        for alpha in plaintxt:
            alpha_code = ord(alpha)  # put the character code of the particular character in alpha_code
            enc_alpha_code = alpha_code + 3 % 26  # encryption is done by adding +3 in the character code and taking modulus of that character
            new_alpha = chr(enc_alpha_code)  # whatever the character code we will get we use the char() to determine the character of which it holds the value
            ciphertxt += new_alpha  # stores the complete cipher text of the plain text we entered

        print(ciphertxt + "\n\n")

    # decryption
    def decrypt():
        # get input from the user
        ciphertxt = input("Enter the text to be decrypted:")

        # empty string to manipulate the original text
        plaintxt = ""

        # main logic
        for alpha in ciphertxt:
            alpha_code = ord(alpha)  # put the character code of the particular character in alpha_code
            enc_alpha_code = alpha_code - 3 % 26  # encryption is done by adding +3 in the character code and taking modulus of that character
            new_alpha = chr(enc_alpha_code)  # whatever the character code we will get we use the char() to determine the character of which it holds the value
            plaintxt += new_alpha  # stores the complete cipher text of the plain text we entered

        print(plaintxt + "\n")

    title = figlet_format("CyPhEr SuItE☺")
    print(title)
    while True:
        print("1.Encrypt a message\n2.Decrypt a message\n3.EXIT")
        choice = int(input("Choose one from above:-"))
        if choice == 1:
            encrypt()
            cont = input("Do you want to continue:?(y/n):")
            cont = cont.lower()
            if cont != 'y':
                print("Exiting Program...")
                break
        elif choice == 2:
            decrypt()
            cont = input("Do you want to continue:?(y/n):")
            cont = cont.lower()
            if cont != 'y':
                print("Exiting Program...")
                break
        elif choice == 3:
            cont = input("Do you want to continue:?(y/n):")
            cont = cont.lower()
            if cont != 'y':
                print("Exiting Program...")
                break


if __name__ == "__main__":
    crypto()
