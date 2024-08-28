use std::fs;
use std::io::{self, Write};

fn main() -> io::Result<()> {

    let content = fs::read_to_string("input.txt")?;

 
    fs::write("output.txt", content)?;

    println!("File content copied successfully.");
    Ok(())
}

