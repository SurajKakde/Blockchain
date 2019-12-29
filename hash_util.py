import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """
    Return calculated hash value using hashlib library for the block.

    Arguments:
        :block: The block that should be hashed.
    """
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
