use std::fs;

fn main () {
    let file_path = "./data/input_1.txt";
    let file_as_string = fs::read_to_string(file_path).unwrap();
    println!("{}", file_as_string);

}
