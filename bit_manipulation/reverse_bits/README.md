# Reverse Bits ([LC190](https://leetcode.com/problems/reverse-bits/))
Difficulty: **Easy**

## Problem

Reverse bits of a given 32 bits *unsigned* integer.

Constraints:
- The input must be a **binary string** of length `32`.

Follow up: If this function is called many times, how would you optimize it?

## Procedure

### Method 1: Bit Shifting "Conveyor Belts"

#### Visualization

Picture two conveyor belts, one with the `input`, and one with the `output`:

```
         MSB    LSB
          10110100
input   (o=======o)
             >>
                                    Start
output    (o========o)
               <<

             1011010
input   (o========o)                Step 1
                    0
output    (o========o)

              101101
input   (o========o)                Step 2
                   00
output    (o========o)

               10110
input   (o========o)                Step 3
                  001
output    (o========o)

...                                 ...

  
input   (o========o)                Finish
            00101101
output    (o========o)
```
The values in `input` are shifted right with `>>` and "fall off" `input`'s right side onto the right side of `output`.  The `output` conveyor then shifts each bit left with `<<`

#### Algorithm

Starting conditions:
- integer size: `32`
- `output = 0`:

For `i` in the range `32` (integer size):
1. Get the least significant bit (`lsb`) from `input`.
2. Bit shift `output` to the left by `1`.
3. Insert `lsb` into `output` using **or** logic (`output |= lsb`).
4. Bit shift `input` to the right by `1`.

Pitfalls:
- For this to work, you must shift `output` *before* inserting `lsb`.  It makes sense if you draw the process out step-by-step.

## Results (Python 3)

**Method 1**:  71 ms, 13.9 MB (5.94%, 50.51%)
