import zlib, base64


def compress(inputfile, outputfile):
    """
    Compresses the contents of the input file and writes the compressed data to the output file.

    Parameters:
        inputfile (str): The path to the input file to be compressed.
        outputfile (str): The path to the output file where compressed data will be stored.
    """
    data = open(inputfile, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(outputfile, 'w')
    compressed_file.write(decoded_data)

# compress('demo.txt', 'ot.txt')


def decompress(inputfile, outputfile):
    """
    Decompresses the contents of the input file and writes the original data to the output file.

    Parameters:
        inputfile (str): The path to the input file containing compressed data.
        outputfile (str): The path to the output file where the original data will be restored.
    """
    file_content = open(inputfile, 'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    file = open(outputfile, 'w')
    file.write(decoded_data)
    file.close()

# decompress('ot.txt', 'dc1.txt')
