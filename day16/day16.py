from functools import reduce

HEX_MAP = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}

class Packet:
    TYPE_FNS = {
        0: sum,
        1: lambda ls : reduce(lambda x, y: x * y, ls),
        2: min,
        3: max,
        5: lambda ls : 1 if ls[0] > ls[1] else 0,
        6: lambda ls : 1 if ls[0] < ls[1] else 0,
        7: lambda ls : 1 if ls[0] == ls[1] else 0
    }
    
    def __init__(self, hex_str=None, bits=None):
        self.version = None
        self.type = None
        self.value = None
        self.subpackets = []
        self.bits = bits if bits else []
        self.bit_end_idx = 0
        if hex_str:
            self._parse_hex(hex_str)
        if bits:
            self._parse_bits()
    
    def _parse_hex(self, hex_str):
        for char in hex_str:
            self.bits.extend(HEX_MAP[char])
        self._parse_bits()
    
    def _parse_bits(self):
        self.version = parse_bin_array(self.bits[0:3])
        self.type = parse_bin_array(self.bits[3:6])
        self._resolve_type()
    
    def _resolve_type(self):
        if self.type == 4:
            self._parse_literal()
        else:
            self._populate_subpackets()
            type_fn = Packet.TYPE_FNS[self.type]
            subpacket_values = [packet.value for packet in self.subpackets]
            self.value = type_fn(subpacket_values)

    def _populate_subpackets(self):
        length_type = self.bits[6]
        if length_type == 0:
            subpackets_length = parse_bin_array(self.bits[7:22])
            self._parse_subpacket_by_length(subpackets_length)
        elif length_type == 1:
            subpackets_num = parse_bin_array(self.bits[7:18])
            self._parse_subpacket_by_number(subpackets_num)
            
    def _parse_subpacket_by_length(self, subpackets_length):
        start_idx = 22
        curr_idx = start_idx
        while curr_idx < start_idx + subpackets_length:
            new_packet = Packet(bits=self.bits[curr_idx::])
            self.subpackets.append(new_packet)
            curr_idx += new_packet.bit_end_idx
        self.bit_end_idx = curr_idx
    
    def _parse_subpacket_by_number(self, subpackets_num):
        start_idx = 18
        subpacket_count = 0
        while subpacket_count < subpackets_num:
            new_packet = Packet(bits=self.bits[start_idx::])
            self.subpackets.append(new_packet)
            start_idx += new_packet.bit_end_idx
            subpacket_count += 1
        self.bit_end_idx = start_idx

    def _parse_literal(self):
        idx = 6
        bin_num = []
        while self.bits[idx] != 0:
            bin_num.extend(self.bits[idx + 1 : idx + 5])
            idx += 5
        bin_num.extend(self.bits[idx + 1 : idx + 5])
        self.value = parse_bin_array(bin_num)
        self.bit_end_idx = idx + 5


def parse_bin_array(arr):
    """
    Given an array of binary digits, returns the number's decimal value.
    """
    output = 0
    for idx, val in enumerate(arr[-1::-1]):
        output += (2 ** idx) * int(val)
    return output

def get_version_sum(packet):
    """
    Given a packet object, returns the sum of the version numbers of the
    packet and all its subpackets.
    """
    version_sum = packet.version
    for subpacket in packet.subpackets:
        version_sum += get_version_sum(subpacket)
    return version_sum

def part1():
    with open('input16', 'r') as f:
        transmission = f.read().strip()
        packet = Packet(hex_str=transmission)
        return get_version_sum(packet)

def part2():
    with open('input16', 'r') as f:
        transmission = f.read().strip()
        packet = Packet(hex_str=transmission)
        return packet.value

print(part1())
print(part2())