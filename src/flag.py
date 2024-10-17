from zlib import crc32
from hashlib import md5, sha1

salt = b'lmao12345'

FLAG = "FIA{{this_is_an_example_flag_{}}}".format(
    crc32(salt)
)