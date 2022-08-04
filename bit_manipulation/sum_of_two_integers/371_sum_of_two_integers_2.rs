impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        let mut answer: i32 = a ^ b;
        let mut carry: i32 = (a & b) << 1;
                
        while carry != 0 {
            let new_answer = answer ^ carry;
            carry = (answer & carry) << 1;
            
            answer = new_answer;            
        }
        
        answer      
    }
}