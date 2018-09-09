import hashlib as hl, json

def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    '''hashes block and returns a string representation
    
    Arguments:
        :block: The block to be hash

    '''
    return hash_string_256(json.dumps(block, sort_keys=True).encode())