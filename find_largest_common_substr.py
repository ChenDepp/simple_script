ref1 = "ACGATTAC"
ref2 = "ACTATTTC"
#largest common substring 
def find_LOC(ref1, ref2, min_len=3):
    ref1_len, ref2_len = len(ref1), len(ref2)
    ref1_offset, window_size, ref2_offset = 0, 1, 0 
    store_substr = []
    while ref1_offset + window_size <= ref1_len:
        substr1 = ref1[ref1_offset:ref1_offset + window_size]
        while ref2_offset <= ref2_len - window_size:
            substr2 = ref2[ref2_offset:ref2_offset + window_size]
            if substr1 == substr2:
                window_size += 1
                if ref2_offset + window_size > len(ref2):
                    if len(substr1[:-1]) >= min_len:
                        store_substr.append((ref1_offset + 1, ref2_offset + 1, substr1))
                break
            elif substr1[:-1] == substr2[:-1]:
                if len(substr1[:-1]) >= min_len:
                    store_substr.append((ref1_offset + 1, ref2_offset + 1, substr1[:-1]))
            ref2_offset += 1
        else:
            ref1_offset += 1
            ref2_offset = 0
    return store_substr