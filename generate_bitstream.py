

from bitarray import bitarray


def main():
    with open("grid_bits.txt", "r") as fo:
        bitstring = ''
        for line in fo:
            bitstring += ''.join(line.split())

    bits = bitarray(bitstring)
    
    with open("bit_map", "wb") as fo:
        bits.tofile(fo)
            
            


if __name__ == '__main__':
    main()
