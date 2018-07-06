
class IPAddress:

    @staticmethod
    def start_with_zero(s):
        """
        :type s: str
        :rtype: boolean
        """
        if len(s) > 1 and s[0] == '0':
            return True
        return False

    @staticmethod
    def is_hex(s):
        """
        :type s: str
        :rtype: boolean
        """
        s = s.upper()
        hex_1 = [str(i) for i in range(10)]
        hex_2 = [chr(i) for i in range(65, 71)]

        for c in s:
            if not (c in hex_1 and c in hex_2):
                return False

        return True

    @staticmethod
    def is_ipv4(IP):
        """
        :type IP: str
        :rtype: boolean
        """
        segments = IP.split(".")

        if len(segments) != 4:
            return False

        for segment in segments:
            if segment == '' or not segment.isdigit() or IPAddress.start_with_zero(segment):
                return False
            s = int(segment)
            if s < 0 or s > 255:
                return False

        return True

    @staticmethod
    def is_ipv6(IP):
        """
        :type IP: str
        :rtype: boolean
        """
        segments = IP.split(":")

        if len(segments) != 8:
            return False

        for segment in segments:
            if segment == '' or len(segment) > 4 or not IPAddress.is_hex(segments):
                return False

        return True

class Solution:

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP and IPAddress.is_ipv4(IP):
            return "IPv4"
        elif ':' in IP and IPAddress.is_ipv6(IP):
            return "IPv6"
        else:
            return "Neither"

