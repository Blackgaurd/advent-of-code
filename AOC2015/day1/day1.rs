use std::fs;

fn part1(input: &str) -> i32 {
    let mut count = 0;
    for ch in input.chars() {
        if ch == '(' {
            count += 1;
        } else {
            count -= 1;
        }
    }
    return count;
}

fn part2(input: &str) -> i32 {
    let mut floor = 0;
    for (idx, ch) in input.chars().enumerate() {
        if ch == '(' {
            floor += 1;
        } else {
            floor -= 1;
        }
        if floor == -1 {
            return idx as i32 + 1;
        }
    }
    return -1;
}

fn main() {
    let in_file = "./input.txt";
    let contents = fs::read_to_string(in_file).expect("input error");
    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}