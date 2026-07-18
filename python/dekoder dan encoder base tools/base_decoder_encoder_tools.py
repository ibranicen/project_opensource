import base64
import os

MAIN_MENU = [
    "base64",
    "base32",
    "base85",
    "base16"
]

LIST_MENU = [
    "teks",
    "file"
]

MAIN_MENU_BASE16 = [
    "decoder base16",
    "encoder base16"
]

MAIN_MENU_BASE64 = [
    "decoder base64",
    "encoder base64",
]

MAIN_MENU_BASE85 = [
    "decoder base85",
    "encoder base85"
]

MAIN_MENU_BASE32 = [
    "decoder base32",
    "encoder base32",
    "hexdecode base32",
    "hexencode base32"
]

def main_banner():
    print("-"*50)
    print("MENU".center(50))
    print("-"*50)

    for index, menu in enumerate(MAIN_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def main_banner_base64():
    print("-"*50)
    print("MENU BASE64".center(50))
    print("-"*50)
    
    for index,menu in enumerate(MAIN_MENU_BASE64, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def main_banner_base16():
    print("-"*50)
    print("MENU BASE16".center(50))
    print("-"*50)
    
    for index,menu in enumerate(MAIN_MENU_BASE16, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def main_banner_base85():
    print("-"*50)
    print("MENU BASE85".center(50))
    print("-"*50)
    
    for index,menu in enumerate(MAIN_MENU_BASE85, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def main_banner_base32():
    print("-"*50)
    print("MENU BASE32".center(50))
    print("-"*50)

    for index, menu in enumerate(MAIN_MENU_BASE32, start=1):
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

def banner_decoder16():
    os.system("cls")
    print("-"*50)
    print("DECODER BASE16".center(50))
    print("-"*50)
    
    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_decoder85():
    os.system("cls")
    print("-"*50)
    print("DECODER BASE85".center(50))
    print("-"*50)
    
    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_decoder32():
    os.system("cls")
    print("-"*50)
    print("DECODER BASE32".center(50))
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

def banner_encoder16():
    os.system("cls")
    print("-"*50)
    print("ENCODER BASE16".center(50))
    print("-"*50)

    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_encoder85():
    os.system("cls")
    print("-"*50)
    print("ENCODER BASE85".center(50))
    print("-"*50)

    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_encoder32():
    os.system("cls")
    print("-"*50)
    print("ENCODER BASE32".center(50))
    print("-"*50)

    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_hexdecoder32():
    os.system("cls")
    print("-"*50)
    print("HEXDECODER BASE32".center(50))
    print("-"*50)

    for index,menu in enumerate(LIST_MENU, start=1):
        print(f"{index}. {menu}")
    print("-"*50)

def banner_hexencoder32():
    os.system("cls")
    print("-"*50)
    print("HEXENCODER BASE32".center(50))
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

def base16_decoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode('utf-8')
        teks16Decode = base64.b16decode(teksToBytes)
        print(f'[+] Hasil Decode Anda: {teks16Decode.decode()}')

    except Exception as e:     
        print("-"*50)
        print(f"[!] Error: {e}")

def base85_decoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode('utf-8')
        teks85Decode = base64.a85decode(teksToBytes)
        print(f'[+] Hasil Decode Anda: {teks85Decode.decode()}')

    except Exception as e:     
        print("-"*50)
        print(f"[!] Error: {e}")

def base32_decoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode("utf-8")
        teks32Decode = base64.b32decode(teksToBytes)
        print(f"[+] Hasil Decode Anda: {teks32Decode.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")    

def base32_hexdecoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode("utf-8")
        teks32hexDecode = base64.b32hexdecode(teksToBytes)
        print(f"[+] Hasil Decode Anda: {teks32hexDecode.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")    

def base32_hexencoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode("utf-8")
        teks32hexEnecode = base64.b32hexencode(teksToBytes)
        print(f"[+] Hasil Decode Anda: {teks32hexEnecode.decode()}")

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

def base16_decoder_file(file_name:str) -> str:
    try:
        with open(file_name, "rb") as file:
            fileRead = file.read().decode('utf-8')

        decodeFile16 = base64.b16decode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Decode Anda:\n{decodeFile16.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")

def base85_decoder_file(file_name:str) -> str:
    try:
        with open(file_name, "rb") as file:
            fileRead = file.read().decode('utf-8')

        decodeFile85 = base64.a85decode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Decode Anda:\n{decodeFile85.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")

def base32_decoder_file(file_name:str) -> str:
    try:    
        with open(file_name, "rb") as file:
            fileRead = file.read().decode("utf-8")

        decodeFile32 = base64.b32decode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Decode Anda: \n{decodeFile32.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")    

def base32_hexdecoder_file(file_name:str) -> str:
    try:    
        with open(file_name, "rb") as file:
            fileRead = file.read().decode("utf-8")

        decodeFile32 = base64.b32hexdecode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Decode Anda: \n{decodeFile32.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")    

def base32_hexencoder_file(file_name:str) -> str:
    try:    
        with open(file_name, "r") as file:
            fileRead = file.read().encode("utf-8")

        encodeFile32hex = base64.b32hexencode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Decode Anda: \n{encodeFile32hex.decode()}")

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

def base16_encoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode('utf-8')
        teksBase16 = base64.b16encode(teksToBytes)
        print("-"*50)
        print(f"[+] Hasil Encode Anda: {teksBase16.decode()}")
    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")    

def base85_encoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode('utf-8')
        teksBase85 = base64.a85encode(teksToBytes)
        print("-"*50)
        print(f"[+] Hasil Encode Anda: {teksBase85.decode()}")
    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")    

def base32_encoder_teks(teks:str) -> str:
    try:
        teksToBytes = teks.encode("utf-8")
        teksBase32 = base64.b32encode(teksToBytes)
        print("-"*50)
        print(f"[+] Hasil Encode Anda: {teksBase32.decode()}")
    except Exception as e:
        print('-'*50)
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

def base16_encoder_file(file_name:str) -> str:
    try:
        with open(file_name, "r") as file:
            fileRead = file.read().encode('utf-8')

        encodeBase16 = base64.b16encode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Encode Anda:\n{encodeBase16.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")

def base85_encoder_file(file_name:str) -> str:
    try:
        with open(file_name, "r") as file:
            fileRead = file.read().encode('utf-8')

        encodeBase85 = base64.a85encode(fileRead)
        print("-"*50)
        print(f"[+] Hasil Encode Anda:\n{encodeBase85.decode()}")

    except Exception as e:
        print("-"*50)
        print(f"[!] Error: {e}")

def base32_encoder_file(file_name:str) -> str:
    try:
        with open(file_name, "r") as file:
            fileRead = file.read().encode("utf-8")

        encode_base32 = base64.b32encode(fileRead)
        print("-"*50)
        print(f'[+] Hasil Encode Anda: \n{encode_base32}')

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

def base16_execution_decode_teks():
    while True:
        try:
            print("-"*50)
            teksToDecode = input("Your Teks Here >> ").strip()
            
            if not teksToDecode:
                raise Exception
            
            if teksToDecode:
                base16_decoder_teks(teksToDecode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base85_execution_decode_teks():
    while True:
        try:
            print("-"*50)
            teksToDecode = input("Your Teks Here >> ").strip()
            
            if not teksToDecode:
                raise Exception
            
            if teksToDecode:
                base85_decoder_teks(teksToDecode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base32_execution_decode_teks():
    while True:
        try:
            print("-"*50)
            teksToDecode = input("Your Teks Here >> ").strip()

            if not teksToDecode:
                raise Exception
            
            if teksToDecode:
                base32_decoder_teks(teksToDecode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")    

def base32_execution_hexdecode_teks():
    while True:
        try:
            print("-"*50)
            teksToDecode = input("Your Teks Here >> ").strip()

            if not teksToDecode:
                raise Exception
            
            if teksToDecode:
                base32_hexdecoder_teks(teksToDecode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")    

def base32_execution_hexencode_teks():
    while True:
        try:
            print("-"*50)
            teksToDecode = input("Your Teks Here >> ").strip()

            if not teksToDecode:
                raise Exception
            
            if teksToDecode:
                base32_hexencoder_teks(teksToDecode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")    

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

def base16_execution_decode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base16_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base16_decoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base85_execution_decode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base85_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base85_decoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base32_execution_decode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base32_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base32_decoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base32_execution_hexdecode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base32_hexdecoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base32_hexdecoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base32_execution_hexencode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base32_hexencoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base32_hexencoder_file(file)
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

def base16_execution_encode_teks():
    while True:
        try:
            print("-"*50)
            teksToEncode = input("Your Teks Here >> ").strip()
            
            if not teksToEncode:
                raise Exception
            
            if teksToEncode:
                base16_encoder_teks(teksToEncode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base85_execution_encode_teks():
    while True:
        try:
            print("-"*50)
            teksToEncode = input("Your Teks Here >> ").strip()
            
            if not teksToEncode:
                raise Exception
            
            if teksToEncode:
                base85_encoder_teks(teksToEncode)
                break

        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base32_execution_encode_teks():
    while True:
        try:
            print("-"*50)
            teksToEncode = input("Your Teks Here >> ").strip()
            
            if not teksToEncode:
                raise Exception
            
            if teksToEncode:
                base32_encoder_teks(teksToEncode)
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

def base16_execution_encode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base16_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base16_encoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base85_execution_encode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base85_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base85_encoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def base32_execution_encode_file():
    while True:
        try:
            print("-"*50)
            fileName = input("Type Your File Name here >> ").lower()
                
            if not fileName:
                raise Exception
            
            if fileName:
                if fileName[-4:] == ".txt":
                    base32_decoder_file(fileName)
                    break

                if fileName[-4:] != ".txt":
                    file = f"{fileName}.txt"
                    base32_encoder_file(file)
                    break
                    
        except Exception as e:
            print("-"*50)
            print(f"[!] Error: {e}")
            continue

def input_user_base64():
    while True:
        main_banner_base64()

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

def input_user_base16():
    while True:
        main_banner_base16()

        try:
            userChoice = str(input(">> ")).strip().lower()
            
            if userChoice not in MAIN_MENU and userChoice not in ["1", "2"]:
                raise Exception

            if userChoice == "1" or userChoice == "decoder base16":
                while True:
                    banner_decoder16()

                    try:
                        user_input1 = str(input(">> ")).strip().lower()
                        
                        if user_input1 not in LIST_MENU and user_input1 not in["1", "2"]:
                            raise Exception

                        if user_input1 =="1" or user_input1 == "teks":
                            base16_execution_decode_teks()
                            return

                        if user_input1 == "2" or user_input1 == "file":
                            base16_execution_decode_file()
                            return

                    except Exception:
                        continue
            
            if userChoice == "2" or userChoice =="encoder base16":
                while True:
                    banner_encoder16()

                    try:
                        user_input2 = str(input(">> ")).strip().lower()

                        if user_input2 not in LIST_MENU and user_input2 not in["1", "2"]:
                            raise Exception
                        
                        if user_input2 == "1" or user_input2 == "teks":
                            base16_execution_encode_teks()
                            return
                        
                        if user_input2 == "2" or user_input2 == "file":
                            base16_execution_encode_file()
                            return

                    except Exception:
                        continue    

        except Exception:
            continue

def input_user_base85():
    while True:
        main_banner_base85()

        try:
            userChoice = str(input(">> ")).strip().lower()
            
            if userChoice not in MAIN_MENU and userChoice not in ["1", "2"]:
                raise Exception

            if userChoice == "1" or userChoice == "decoder base85":
                while True:
                    banner_decoder85()

                    try:
                        user_input1 = str(input(">> ")).strip().lower()
                        
                        if user_input1 not in LIST_MENU and user_input1 not in["1", "2"]:
                            raise Exception

                        if user_input1 =="1" or user_input1 == "teks":
                            base85_execution_decode_teks()
                            return

                        if user_input1 == "2" or user_input1 == "file":
                            base85_execution_decode_file()
                            return

                    except Exception:
                        continue
            
            if userChoice == "2" or userChoice =="encoder base85":
                while True:
                    banner_encoder85()

                    try:
                        user_input2 = str(input(">> ")).strip().lower()

                        if user_input2 not in LIST_MENU and user_input2 not in["1", "2"]:
                            raise Exception
                        
                        if user_input2 == "1" or user_input2 == "teks":
                            base85_execution_encode_teks()
                            return
                        
                        if user_input2 == "2" or user_input2 == "file":
                            base85_execution_encode_file()
                            return

                    except Exception:
                        continue    

        except Exception:
            continue

def input_user_base32():
    while True:
        main_banner_base32()

        try:
            userChoice = str(input(">> ")).strip().lower()
            
            if userChoice not in MAIN_MENU and userChoice not in ["1", "2", "3", "4"]:
                raise Exception

            if userChoice == "1" or userChoice == "decoder base32":
                while True:
                    banner_decoder32()

                    try:
                        user_input1 = str(input(">> ")).strip().lower()
                        
                        if user_input1 not in LIST_MENU and user_input1 not in["1", "2"]:
                            raise Exception

                        if user_input1 =="1" or user_input1 == "teks":
                            base32_execution_decode_teks()
                            return

                        if user_input1 == "2" or user_input1 == "file":
                            base32_execution_decode_file()
                            return

                    except Exception:
                        continue
            
            if userChoice == "2" or userChoice =="encoder base32":
                while True:
                    banner_encoder32()

                    try:
                        user_input2 = str(input(">> ")).strip().lower()

                        if user_input2 not in LIST_MENU and user_input2 not in["1", "2"]:
                            raise Exception
                        
                        if user_input2 == "1" or user_input2 == "teks":
                            base32_execution_encode_teks()
                            return
                        
                        if user_input2 == "2" or user_input2 == "file":
                            base32_execution_encode_file()
                            return

                    except Exception:
                        continue    

            if userChoice == "3" or userChoice == "hexdecode base32":
                while True:
                    banner_hexdecoder32()

                    try:
                        user_input2 = str(input(">> ")).strip().lower()

                        if user_input2 not in LIST_MENU and user_input2 not in["1", "2"]:
                            raise Exception
                        
                        if user_input2 == "1" or user_input2 == "teks":
                            base32_execution_hexdecode_teks()
                            return
                        
                        if user_input2 == "2" or user_input2 == "file":
                            base32_execution_hexdecode_file()
                            return

                    except Exception:
                        continue    

            if userChoice == "4" or userChoice == "hexencode base32":
                while True:
                    banner_hexencoder32()

                    try:
                        user_input2 = str(input(">> ")).strip().lower()

                        if user_input2 not in LIST_MENU and user_input2 not in["1", "2"]:
                            raise Exception
                        
                        if user_input2 == "1" or user_input2 == "teks":
                            base32_execution_hexencode_teks()
                            return
                        
                        if user_input2 == "2" or user_input2 == "file":
                            base32_execution_hexencode_file()
                            return

                    except Exception:
                        continue    


        except Exception:
            continue

def main():
    main_banner()

    while True:
        try:
            user = str(input(">> ")).lower()

            if user not in ["1", "2", "3", "4"] and user not in MAIN_MENU:
                raise Exception

            if user == "1" or user == "base64":
                input_user_base64()
                break

            if user == "2" or user == "base32":
                input_user_base32()    
                break

            if user == "3" or user == "base85":
                input_user_base85()
                break

            if user == "4" or user == "base16":
                input_user_base16()
                break

        except Exception:
            print("-"*50)
            print(f"[!] Menu tidak tersedia")    

if __name__ == '__main__':
    os.system('cls')
    main()