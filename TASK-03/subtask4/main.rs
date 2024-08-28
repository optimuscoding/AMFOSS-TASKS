
use std::fs;
use std::io::{self, Write};

fn read_number_from_file(filename: &str) -> io::Result<usize> {
    let content = fs::read_to_string(filename)?;
    let number: usize = content.trim().parse().map_err(|_| io::Error::new(io::ErrorKind::InvalidData, "Invalid number"))?;
    Ok(number)
}

fn generate_diamond(n: usize) -> String {
    if n < 1 || n % 2 == 0 {
        return "Please enter a positive odd number.\n".to_string();
    }

    let mut pattern = String::new();
    let half = n / 2;


    for i in 0..n {
        if i <= half {
            let spaces = " ".repeat(half - i);
            let stars = "*".repeat(2 * i + 1);
            pattern.push_str(&format!("{}{}\n", spaces, stars));
        } else {
            let spaces = " ".repeat(i - half);
            let stars = "*".repeat(2 * (n - i - 1) + 1);
            pattern.push_str(&format!("{}{}\n", spaces, stars));
        }
    }

    pattern
}

fn write_diamond_to_file(filename: &str, pattern: &str) -> io::Result<()> {
    fs::write(filename, pattern)
}

fn main() -> io::Result<()> {
    let input_filename = "input.txt";
    let output_filename = "output.txt";

   
    let n = read_number_from_file(input_filename)?;

    let diamond_pattern = generate_diamond(n);

    
    write_diamond_to_file(output_filename, &diamond_pattern)?;

    Ok(())
}
