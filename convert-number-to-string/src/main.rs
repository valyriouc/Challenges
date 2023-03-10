fn number_to_string(i: i32) -> String {
    i.to_string()
}

fn main() {
    let i = number_to_string(200);
    println!("The value is {i}");
}
