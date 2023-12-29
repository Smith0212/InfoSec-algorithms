def encrypt_rail_fence(text, rails): 
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction = -1  # Direction for zigzag pattern
    row, col = 0, 0 
    for char in text:
        if row == 0 or row == rails - 1: 
            direction *= -1
        fence[row][col] = char
        col += 1 
        row += direction 
 
    encrypted_text = ''.join([char for row in fence for char in row if char != '\n']) 
    return encrypted_text 

def decrypt_rail_fence(ciphertext, rails): 
    fence = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = -1
    row, col = 0, 0 
    for _ in range(len(ciphertext)):
        if row == 0 or row == rails - 1: 
            direction *= -1 
        fence[row][col] = '*'         
        col += 1 
        row += direction 
 
    index = 0
    for row in range(rails):
        for col in range(len(ciphertext)):
            if fence[row][col] == '*' and index < len(ciphertext): 
                fence[row][col] = ciphertext[index]
                index += 1 
 
    direction = -1
    row, col = 0, 0
    decrypted_text = '' 
    for _ in range(len(ciphertext)):
        if row == 0 or row == rails - 1: 
            direction *= -1
        if fence[row][col] != '\n': 
            decrypted_text += fence[row][col]
        col += 1 
        row += direction 
 
    return decrypted_text 
 
# Example usage 
message="NESOACADEMYISTHEBEST"
rails = 2 
 
encrypted_message = encrypt_rail_fence(message, rails)
print("Encrypted:", encrypted_message)  
decrypted_message = decrypt_rail_fence(encrypted_message, rails)
print("Decrypted:", decrypted_message)