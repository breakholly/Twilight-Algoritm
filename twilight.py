# Import modules
import core.xor  as Xor
import core.salt as Salt
import core.hash as Hash

# Encrypt function
def Encrypt(text, key):
    
    salt = Hash.getSaltByKey(key, text)
    saltedText = Salt.protect(text, salt)
    xoredText  = Xor.encode(saltedText, key)
    return xoredText

# Decrypt function
def Decrypt(text, key):
    unxoredText = Xor.decode(text, key)
    salt = Hash.getSaltByKey(key, unxoredText)
    unsaltData  = Salt.unprotect(unxoredText, salt)
    return unsaltData
