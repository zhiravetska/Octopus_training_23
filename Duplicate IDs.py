def remove_duplicate_ids(ids_list):
    
    num_entries = len(ids_list)
    print(num_entries)
    index_to_update = 1

    for i in range(1, num_entries):
        if ids_list[i] != ids_list[i-1]:
            ids_list[index_to_update] = ids_list[i]
            index_to_update += 1
    N = index_to_update
    #print(N)
    #print(ids_list)
    print(N, ids_list[:N])
    return (N, ids_list[:N])
    

remove_duplicate_ids([1,2,2,3,3,4,4,5,5])