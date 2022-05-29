print("Thanks for using pyessentials")


# __author__  ~~Shaurya Mishra~~
# __date created__ 29/05/2022
#                                  
#                                Details-
#                             * This library uses base64 for encryption and decryption purpose.
#                             * Contains two classes *encryption and *text having 4 and 3 functions respectively.
#                             * Class encryption can be used for encrypting data and files while text file can be used to read, write or alter strings present in a text file.


import base64


class encryption():


    def encrypt(string):
        string_bytes = string.encode("ascii")
        base64_bytes = base64.b64encode(string_bytes)
        base64_message = base64_bytes.decode("ascii")
        return base64_message


    def decrypt(string):
        string_bytes = string.encode("ascii")
        base64_bytes = base64.b64decode(string_bytes)
        base64_message = base64_bytes.decode("ascii")
        return base64_message

    def cryptimg(path):
        binary = open((path), "rb")
        binary_data = binary.read()
        encode_data = base64.b64encode(binary_data)
        crypted = encode_data.decode("ascii")
        return crypted


    def decryptimg(img, output):
        img_bytes = img.encode("ascii")
        file_to_save = open(output, "wb")
        decoded_data = base64.decodebytes(img_bytes)
        file_to_save.write(decoded_data)



class text():


    def write(string, name):
        f = open(str(name), "w")
        f.writelines(str(string))
        f.close()

    def alter(string, name):
        f = open(str(name), "a")
        f.writelines(str(string))
        f.close()


    def study(name):
        f = open(str(name), "r")
        r = f.read()
        return r        


    