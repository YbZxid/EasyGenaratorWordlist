import itertools

def generate_wordlist(characters, min_length, max_length, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(characters, repeat=length):
                word = ''.join(combination)
                f.write(word + '\n')

if __name__ == "__main__":
    # Contoh penggunaan
    characters = input("Masukkan karakter yang kau nak gunakan (contoh: abc): ")
    min_length = int(input("Masukkan panjang minimum perkataan: "))
    max_length = int(input("Masukkan panjang maksimum perkataan: "))
    output_file = input("Masukkan nama fail output (contoh: wordlist.txt): ")
    
    generate_wordlist(characters, min_length, max_length, output_file)
    print(f"Wordlist berjaya dijana dalam {output_file}")
