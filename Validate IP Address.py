#needs optimization
class Solution:
    def validIPAddress(self, IP: str) -> str:
        import string
        octets = []
        if ':' not in IP: 
            octets = IP.split('.')
            if len(octets) != 4:
                return "Neither"
            for octet in octets:
                if not octet.isnumeric() or (len(octet) > 1 and octet[0] == '0'):
                    return "Neither"
                if int(octet) < 0 or int(octet) > 255:
                    return "Neither"
            return "IPv4"       
        else:
            octets = IP.split(':')
            if len(octets) != 8:
                return "Neither"
            for octet in octets:
                if not all(c in string.hexdigits for c in octet) or len(octet) > 4 or octet == "":
                    return "Neither"
                if int(octet,16) < 0 or int(octet,16) > 0xffff:
                    return "Neither"
            return "IPv6"       
