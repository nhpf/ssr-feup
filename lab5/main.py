from math import gcd
import codecs

def str_to_int(msg):
    return int(codecs.encode(msg.encode(), "hex").decode(), 16)

def int_to_str(num):
    return codecs.decode(hex(num)[2:], "hex") 


def task_1():
    p = 0xF7E75FDC469067FFDC4E847C51F452DF
    q = 0xE85CED54AF57E53E092113E62F436F4F
    e = 0x0D88C3
    n = p * q

    lamb = int((p-1)*(q-1)/gcd(p-1,q-1))

    print(f"lambda = {hex(lamb)}")

    public_key = (e, n)
    private_key = (pow(e, -1, lamb), n)

    print(f"d = {hex(private_key[0])}")

def task_2():
    msg = "A top secret!"
    int_msg = str_to_int(msg)
    
    e = 0x010001
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D

    c = pow(int_msg, e, n)
    print("encoded message = ", hex(c))

def task_3():
    msg = "A top secret!"
    int_msg = str_to_int(msg)
    
    e = 0x010001
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D

    c = pow(int_msg, e, n)
    print("encoded message = ", hex(c))

    dec_msg = pow(c, d, n)
    dec_str = int_to_str(dec_msg)

    print("decoded message = ", dec_str) 


def task_4():
    msg = "I owe you $2000."
    int_msg = str_to_int(msg)
    
    e = 0x010001
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D

    signature = pow(int_msg, e, n)
    proof = pow(signature, d, n)
    
    print(f"message = {msg}\n\tsign = {hex(signature)}\n\tproof = {int_to_str(proof)}")

    new_msg = "I owe you $3000."
    int_msg = str_to_int(new_msg)
    
    signature = pow(int_msg, e, n)
    proof = pow(signature, d, n)
    
    print(f"new message = {new_msg}\n\tsign = {hex(signature)}\n\tproof = {int_to_str(proof)}")


def task_5():
    msg = "Launch a missile."
    supposed_signature = 0x643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F
    e = 0x010001 # this hex value equals to decimal 65537
    n = 0xAE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115

    int_msg = str_to_int(msg)
    actual_signature = pow(int_msg, e, n)

    print(f"Alice's actual sigature = {hex(actual_signature)}\nGiven signature = {hex(supposed_signature)}")
    print("The message is not hers" if actual_signature!=supposed_signature else "The message is hers")

    corrupted_signature = 0x643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6803F
    actual_signature = pow(int_msg, e, n)

    print(f"\nAlice's actual sigature = {hex(actual_signature)}\nGiven signature = {hex(corrupted_signature)}")
    print("The message is not hers" if actual_signature!=supposed_signature else "The message is hers")

if __name__ == '__main__':
    task_5()



