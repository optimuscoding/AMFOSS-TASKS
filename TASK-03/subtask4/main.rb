def read_number_from_file(filename)
  begin
    File.open(filename, 'r') do |file|
      number = file.readline.strip.to_i
      return number
    end
  rescue Errno::ENOENT, ArgumentError
    puts "Error reading from file '#{filename}'. Make sure the file exists and contains a valid number."
    return nil
  end
end

def write_diamond_to_file(filename, n)
  begin
    File.open(filename, 'w') do |file|
      if n < 1 || n.even?
        file.puts "Please enter a positive odd number."
        return
      end

      half = n / 2


      (0...n).each do |i|
        if i <= half
          spaces = ' ' * (half - i)
          stars = '*' * (2 * i + 1)
        else
          spaces = ' ' * (i - half)
          stars = '*' * (2 * (n - i - 1) + 1)
        end
        file.puts "#{spaces}#{stars}"
      end
    end
  rescue IOError
    puts "Error writing to file '#{filename}'."
  end
end

def main
  input_filename = 'input.txt'
  output_filename = 'output.txt'

  n = read_number_from_file(input_filename)

  
  if n
    write_diamond_to_file(output_filename, n)
  end
end


main
