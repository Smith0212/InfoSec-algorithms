import math

def encryption (massage, key):
    massage = massage.replace(" ", "")
    msg = []
    x = 0
    count = 0
    num_of_rows = math.ceil((len(massage)/len(key)))
    padding = int(num_of_rows * len(key)) - len(massage)
    massage += padding * "x"
    
    for rows in range(num_of_rows):
        row = []
        for i in range(len(key)):
            row.append(massage[i+x])
            count += 1
        x = count  
        msg.append(row)
    # print(msg)

    key = key.upper()
    key_list = [ord(i) for i in key]
    # print(key_list)
    sorted_key_list = sorted(key_list)
    # print(sorted_key_list)
    # print(key_list.index(65))
    # print(key_list.index(66))
    col_index = [key_list.index(i)  for i in sorted_key_list]
    # print(col_index) 

    e_msg = []
    for i in col_index:
        for j in range(len(msg)):    #len(msg) = num_of_rows
            e_msg.append(msg[j][i])
    return "".join(e_msg)

def decryption(e_msg, key):
    rows = len(e_msg) // len(key)
    # print(rows)

    key = key.upper()
    key_list = [ord(i) for i in key]
    sorted_key_list = sorted(key_list)
    col_index = [sorted_key_list.index(i)+1 for i in key_list]
    # print(col_index)



    temp = [] 
    for i in col_index: 
        for j in range(((i-1) * rows), (i * rows)): 
            temp.append(e_msg[j]) 
     
    d_msg = [] 
    for i in range(rows): 
        count = 0 
        for j in range(len(key)): 
            if temp[count+i] == "x": 
                d_msg.append("") 
            else: 
                d_msg.append(temp[count+i]) 
                count += rows 
    return "".join(d_msg) 

def main():
    massage = input("Enter message to encrypt: ")
    key = input("Enter key: ")
    print()

    e_msg = encryption (massage, key)
    print("Encrypted message: ", e_msg)
    print()

    d_msg = decryption (e_msg, key)
    print("Decrypted message: ", d_msg)
    print()

if __name__ =="__main__":
    main()