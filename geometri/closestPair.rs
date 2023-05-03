use std::{cmp::Ordering};

#[allow(unused_macros)] //https://stackoverflow.com/questions/30355185/how-to-read-an-integer-input-from-the-user-in-rust-1-0
macro_rules! read {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("A String");
        let mut $out = inner.trim().parse::<$type>().expect("Parsable");
    };
}

#[allow(unused_macros)]
macro_rules! read_str {
    ($out:ident) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).expect("A String");
        let $out = inner.trim();
    };
}

#[allow(unused_macros)]
macro_rules! read_vec {
    ($out:ident as $type:ty) => {
        let mut inner = String::new();
        std::io::stdin().read_line(&mut inner).unwrap();
        let $out = inner
            .trim()
            .split_whitespace()
            .map(|s| s.parse::<$type>().unwrap())
            .collect::<Vec<$type>>();
    };
}

#[derive(Copy,Clone,PartialEq, PartialOrd, Debug)]
struct Point {
    x: f64,
    y: f64,
}

impl Eq for Point {}

impl Ord for Point {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        return self.x.total_cmp(&other.x).then(self.y.total_cmp(&other.y));
        //self.partial_cmp(&other).unwrap()
    }
}


fn comp_x(&a: &Point, &b: &Point) -> Ordering {
    return a.x.total_cmp(&b.x).then(a.y.total_cmp(&b.y)) ;
}

fn comp_y(&a: &Point, &b: &Point) -> Ordering {
    return a.y.total_cmp(&b.y).then(a.x.total_cmp(&b.x)) ;
}

fn new_point(x: f64, y:f64) -> Point{
    Point { x, y }
}

fn dist(a: Point, b: Point) -> f64{
    return ((a.x -b.x).powi(2)+(a.y-b.y).powi(2)).sqrt();
}

fn closest_pair(sorted_x: Vec<Point>, sorted_y: Vec<Point>) -> (Point, Point) {
    if sorted_x.len() <= 3 {
        let mut min_dist: f64 = f64::MAX;
        let mut min_pair: (Point, Point) = (new_point(0.0, 0.0), new_point(0.0, 0.0));
        for i in 0..sorted_x.len(){
            for j in (i+1)..sorted_x.len(){
                let d = dist(sorted_x[i], sorted_x[j]);
                if d < min_dist{
                    min_dist = d;
                    min_pair = (sorted_x[i],sorted_x[j]);
                }
            }
        }
        return min_pair;
    }
    let mid: usize = sorted_x.len()/2;
    let (left_x, right_x) = sorted_x.split_at(mid);
    let mut left_y: Vec<Point> = vec![];
    let mut right_y: Vec<Point> = vec![];
    for i in 0..sorted_y.len(){
        if sorted_y[i].x <= left_x.last().unwrap().x{
            left_y.push(sorted_y[i]);
        }else{
            right_y.push(sorted_y[i]);
        }
    }
    let left_pair: (Point, Point) = closest_pair(left_x.to_vec(), left_y.to_vec());
    let right_pair: (Point, Point) = closest_pair(right_x.to_vec(), right_y.to_vec());
    let d_left: f64 = dist(left_pair.0, left_pair.1);
    let d_right: f64 = dist(right_pair.0, right_pair.1);
    let mut d: f64 = d_left.min(d_right);
    let mut min_pair: (Point, Point) = if d_left < d_right {left_pair} else {right_pair};
    let mut strip: Vec<Point> = vec![];
    for i in 0..sorted_y.len(){
        if (sorted_y[i].x - sorted_x[mid].x).abs() < d{
            strip.push(sorted_y[i]);
        }
    }
    for i in 0..strip.len(){
        for j in (i+1)..strip.len(){
            if strip[j].y - strip[i].y >= d{ break;}
            let d_strip = dist(strip[i], strip[j]);
            if d_strip < d{
                d = d_strip;
                min_pair = (strip[i], strip[j]);
            }
        }
    }
    return min_pair;
}

fn main() {
    // Statements here are executed when the compiled binary is called.
    read!(r as i32);
    #[allow(while_true)]
    while true {
        if r == 0 { break;}
        let mut points_x: Vec<Point> = vec![];
        let mut points_y: Vec<Point> = vec![];
        for _ in 0..r{
            read_vec!(p as f64);
            points_x.push(new_point(p[0], p[1]));
            points_y.push(new_point(p[0], p[1]));
        } 
        points_x.sort_by(|a, b| comp_x(a,b));
        points_y.sort_by(|a, b| comp_y(a,b));
        let closest: (Point, Point) = closest_pair(points_x, points_y);
        println!("{} {} {} {}",closest.0.x,closest.0.y,closest.1.x,closest.1 .y);
        
        read!(_r as i32);
        r = _r;
        
    }
}

