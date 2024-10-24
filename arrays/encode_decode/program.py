'''

# Prompt

Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 does:
string encoded_string = encode(strs);


and Machine 2 does:
vector<string> strs2 = decode(encoded_string);


strs2 in Machine 2 should be the same as strs in Machine 1.


# Constraints

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.



'''

from typing import List


class Codec:

    DELIMITER = '?;_;?'
    DELIMITER = ';'

    def encode(self, strs: List[str]) -> str:
        return self.DELIMITER.join(strs)


    def decode(self, s: str) -> List[str]:
        return s.split(self.DELIMITER)


    def encode(self, strs: List[str]) -> str:

        encoded_str = ''

        for s in strs:
            encoded_str += f'{len(s)+1};{s}'

        return encoded_str


    def decode(self, s: str) -> List[str]:

        decoded_str = []
        num_str = ''
        i = 0

        length = len(s)

        while i < length:

            c = s[i]

            if c != ';':
                num_str += c
                i += 1

            else:
                num = int(num_str)

                decoded_s = s[i+1:i+num]
                decoded_str.append(decoded_s)

                num_str = ''

                i += num


        return decoded_str


codec = Codec()

strs = ['Hello', 'World']
encoded_str = codec.encode(strs)
print(encoded_str)
decoded_str = codec.decode(encoded_str)
print(decoded_str)
