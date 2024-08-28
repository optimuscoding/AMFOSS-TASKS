def read_number_from_file(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            number = int(line)
            return number
    except (FileNotFoundError, ValueError):
        print(f"Error reading from file '{filename}'. Make sure the file exists and contains a valid number.")
        return None

def write_diamond_to_file(filename, n):
    try:
        with open(filename, 'w') as file:
            if n < 1 or n % 2 == 0:
                file.write("Please enter a positive odd number.\n")
                return
            
            half = n // 2
            
           
            for i in range(n):
                if i <= half:
                    spaces = ' ' * (half - i)
                    stars = '*' * (2 * i + 1)
                else:
                    spaces = ' ' * (i - half)
                    stars = '*' * (2 * (n - i - 1) + 1)
                
                file.write(f"{spaces}{stars}\n")
    except IOError:
        print(f"Error writing to file '{filename}'.")

def main():
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    
  
    n = read_number_from_file(input_filename)
    
   
    if n is not None:
        write_diamond_to_file(output_filename, n)

if __name__ == "__main__":
    main()
