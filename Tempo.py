from cryptography.fernet import Fernet
from pydub import AudioSegment
import hashlib
import base64


def song_to_key(song_path):
    
    audio = AudioSegment.from_file(song_path)
   
    audio = audio.set_channels(1).set_frame_rate(44100)
  
    raw_data = audio.raw_data

    sha = hashlib.sha256(raw_data).digest()

    key = base64.urlsafe_b64encode(sha)
    return key

def encrypt_file(input_file, song_path, output_file):
    key = song_to_key(song_path)
    fernet = Fernet(key)
   
    with open(input_file, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)

    with open(output_file, "wb") as f:
        f.write(encrypted)
    print("File encrypted using music")

def decrypt_file(encrypted_file, song_path, output_file):
    key = song_to_key(song_path)
    fernet = Fernet(key)
 
    with open(encrypted_file, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)

    with open(output_file, "wb") as f:
        f.write(decrypted)
    print("File decrypted. Song matched.")

if __name__ == "__main__":
 choice = ""

 while choice != "3": 
  print("TEMPO")
  print("1. Encrypt file ")
  print("2. Decrypt file")
  print("3. Quit")
  choice = input("Enter your choice: ")

  if choice == "1":
    try:
      input_file = input("Enter the name of the file you want to encrypt: ")
      song = input("Enter the name of the song that will be used to encrypt the file: ")
      output_file = input("Enter the name of the output file: ")
      encrypt_file(input_file, song, output_file)
    except Exception as e:
       print(f"An error occurred: {e}")
       
  elif choice == "2":
     try:
       encrypted_file = input("Enter the name of the encrypted file: ")
       song = input("Enter the name of the song used to decrypt the file: ")
       output_file = input("Enter the name of the output file: ")
       decrypt_file(encrypted_file, song, output_file)
     except Exception as e:
         print(f"An error occurred: {e}")   
 
 print("Thank you for using Tempo.")