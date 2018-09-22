import hashlib as hl, json

def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    '''hashes block and returns a string representation
    
    Arguments:
        :block: The block to be hash

    '''
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())