
class Caesar(object):

    def encode(self, string, shift):
        encoded = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
         !,.?-+@#$%^&*()=0123456789""'
        for s in string:
            for i in xrange(0,len(alphabet)):
                if s == alphabet[i]:
                    j = i + shift
                    break     # Break out of the second loop, to increase speed
            if j >= len(alphabet):
                j = j % len(alphabet)
            encoded += alphabet[j]
        return encoded

    def decode(self, string, shift):
        decoded = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
         !,.?-+@#$%^&*()=0123456789""'
        for s in string:
            for i in xrange(0,len(alphabet)):
                if s == alphabet[i]:
                    j = i - shift
                    break     # Break out of the second loop, to increase speed
            decoded += alphabet[j]
        return decoded

    def encode1(self, str, shift): 
        result = ''
        for i in str:
            result += chr(ord(i) + shift) 
        return result

    def decode1(self, str, shift):
        result = ''
        for i in str:
            result += chr(ord(i) - shift)
        return result

class Vigenere(object):

    def encode(self, str, passcode):
        encoded = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
         !,.?-+@#$%^&*()=0123456789""'
        for i in range(len(str)):
            for j in xrange(0,len(alphabet)):
                if str[i] == alphabet[j]:
                    c1 = j
                    break
            for j in xrange(0,len(alphabet)):
                if passcode[i % len(passcode)] == alphabet[j]:
                    c2 = j
                    break
            if str[i] in alphabet:
                encoded += alphabet[(c1+c2) % len(alphabet)]
            else:
                encoded += str[i]
        return encoded

    def decode(self, str, passcode):
        decoded = ''
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
         !,.?-+@#$%^&*()=0123456789""'
        for i in range(len(str)):
            for j in xrange(0,len(alphabet)):
                if str[i] == alphabet[j]:
                    c1 = j
                    break
            for j in xrange(0,len(alphabet)):
                if passcode[i % len(passcode)] == alphabet[j]:
                    c2 = j
                    break
            if str[i] in alphabet:
                decoded += alphabet[c1-c2]
            else:
                decoded += str[i]
        return decoded

    def encode1(self, str, passcode):
        encoded = ''
        for i in range(len(str)):
            encoded += chr(ord(str[i]) + ord(passcode[i % len(passcode)]))
        return encoded

    def decode1(self, str, passcode):
        decoded = ''
        for i in range(len(str)):
            decoded += chr(ord(str[i]) - ord(passcode[i % len(passcode)]))
        return decoded