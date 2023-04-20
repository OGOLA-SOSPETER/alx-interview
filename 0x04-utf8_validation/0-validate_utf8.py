def validUTF8(data):
    # Initialize a count of the number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Iterate over each byte in the data set
    for byte in data:
        # Check if this byte is the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte >> 7) == 0b0:
                # This is a single-byte UTF-8 character
                num_bytes = 1
            elif (byte >> 5) == 0b110:
                # This is a two-byte UTF-8 character
                num_bytes = 2
            elif (byte >> 4) == 0b1110:
                # This is a three-byte UTF-8 character
                num_bytes = 3
            elif (byte >> 3) == 0b11110:
                # This is a four-byte UTF-8 character
                num_bytes = 4
            else:
                # This byte is not the start of a valid UTF-8 character
                return False
        else:
            # This byte is part of a multi-byte UTF-8 character
            if (byte >> 6) != 0b10:
                # This byte is not a continuation byte
                return False
            
            # Decrement the count of bytes remaining in the current UTF-8 character
            num_bytes -= 1
        
    # If we reach the end of the data set and there are still bytes remaining in the current UTF-8 character,
    # then the data set is not a valid UTF-8 encoding
    if num_bytes > 0:
        return False
    
    # Otherwise, the data set is a valid UTF-8 encoding
    return True

