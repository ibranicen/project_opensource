import base64
import os

LIST_MENU = [
    "teks",
    "file"
]

MAIN_MENU = [
    "decoder base64",
    "encoder base64"
]

def main_banner():
    print("-"*50)
    print("MENU".center(50))
    print("-"*50)
    
    for index,menu in enumerate(MAIN_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_decoder64():
    os.system("cls")
    print("-"*50)
    print("DECODER BASE64".center(50))
    print("-"*50)
    
    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_encoder64():
    os.system("cls")
    print("-"*50)
    print("ENCODER BASE64".center(50))
    print("-"*50)

    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def base64_decoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode('utf-8')
        teks64Decode = base64.b64decode(teksToBytes)
        print(f'[+] Hasil Decode Anda: {teks64Decode.decode()}')

    except Exception as e:     
        print("-"*50)
        print(f"[!] Error: {e}")

def base64_decoder_file(file_name:str) -> str:
    try:
        with open(file_name, "rb") as file:
            fileRead = file.read().decode('utf-8')

        decodeFile64 = base64.b64decode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Decode Anda:\n{decodeFile64.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")

def base64_encoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode('utf-8')
        teksBase64 = base64.b64encode(teksToBytes)
        print("-"*50)
        print(f"[+] Hasil Encode Anda: {teksBase64.decode()}")
    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")    

def base64_encoder_file(file_name:str) -> str:
    try:
        with open(file_name, "r") as file:
            fileRead = file.read().encode('utf-8')

            encodeBase64 = base64.b64encode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Encode Anda:\n{encodeBase64.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")

def base64_execution_decode_teks():
    while True:
        try:
            print("-"*50)
            teksToDecode = input("Your Teks Here >> ").strip()
            
            if not teksToDecode:
                raise Exception
            
            if teksToDecode:
                base64_decoder_teks(teksToDecode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base64_execution_decode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base64_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base64_decoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base64_execution_encode_teks():
    while True:
        try:
            print("-"*50)
            teksToEncode = input("Your Teks Here >> ").strip()
            
            if not teksToEncode:
                raise Exception
            
            if teksToEncode:
                base64_encoder_teks(teksToEncode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base64_execution_encode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base64_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base64_encoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def input_user():
    while True:
        main_banner()

        try:
            userChoice = str(input(">> ")).strip().lower()
            
            if userChoice not in MAIN_MENU and userChoice not in ["1", "2"]:
                raise Exception

            if userChoice == "1" or userChoice == "decoder base64":
                while True:
                    banner_decoder64()

                    try:
                        user_input1 = str(input(">> ")).strip().lower()
                        
                        if user_input1 not in LIST_MENU and user_input1 not in["1", "2"]:
                            raise Exception

                        if user_input1 =="1" or user_input1 == "teks":
                            base64_execution_decode_teks()
                            return

                        if user_input1 == "2" or user_input1 == "file":
                            base64_execution_decode_file()
                            return

                    except Exception:
                        continue
            
            if userChoice == "2" or userChoice =="encoder base64":
                while True:
                    banner_encoder64()

                    try:
                        user_input2 = str(input(">> ")).strip().lower()

                        if user_input2 not in LIST_MENU and user_input2 not in["1", "2"]:
                            raise Exception
                        
                        if user_input2 == "1" or user_input2 == "teks":
                            base64_execution_encode_teks()
                            return
                        
                        if user_input2 == "2" or user_input2 == "file":
                            base64_execution_encode_file()
                            return

                    except Exception:
                        continue    

        except Exception:
            continue


if __name__ == '__main__':
    os.system('cls')
    input_user()