def remove_duplicate_ids(ids_list):
    
    num_entries = len(ids_list)
    index_to_update = 1
    for i in range(1, num_entries):
        if ids_list[i] != ids_list[i-1]:
            ids_list[index_to_update] = ids_list[i]
            index_to_update += 1
    N = index_to_update
    print(N)
    return (N, ids_list)

