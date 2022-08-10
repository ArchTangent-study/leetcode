use std::collections::HashMap;

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut timer: i32 = 0;
        let mut total_count: i32 = 0;
        let mut count: HashMap<char, i32> = HashMap::new();
        let mut ready: HashMap<char, i32> = HashMap::new();

        for task in tasks.iter() {
            total_count += 1;

            *count.entry(*task).or_insert(0) += 1;

            // NOTE: -1 means all tasks start ready (timer of 0 is > -1)
            ready.entry(*task).or_insert(-1);
        }

        while total_count > 0 {
            // Perform ready task with highest count
            let mut highest: Option<char> = None;
            let mut high_count = 0;

            for (task, ready_time) in &ready {
                if timer > *ready_time {
                    let ct = count[task];
                    if ct > high_count {
                        high_count = ct;
                        highest = Some(*task);
                    }
                }
            }

            // At least one task was ready
            if let Some(task) = highest {
                ready.insert(task, timer + n);
                count.insert(task, high_count - 1);
                total_count -= 1;
            } 


            // Update timer to (a) perform task or (b) idle
            timer += 1;
        }            

        timer
    }
}