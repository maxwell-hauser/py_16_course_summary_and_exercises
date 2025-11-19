"""
============================================================
CHAPTER 16: Course Summary and Exercises
Computer Systems and Logic - Comprehensive Review
============================================================

This module provides interactive demonstrations and examples
covering all major topics from the Computer Systems and Logic
course, including digital logic, combinational circuits,
sequential circuits, and data representation.
"""

def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60 + "\n")

def print_subheader(title):
    """Print a formatted subsection header."""
    print(f"\n--- {title} ---")

# ============================================================
# EXERCISE 1: NUMBER SYSTEMS AND CONVERSIONS
# ============================================================

def ex1_number_systems():
    """Demonstrate number system conversions."""
    print_header("Exercise 1: Number Systems and Conversions")
    
    # Binary to Decimal
    print_subheader("Binary to Decimal Conversion")
    binary = "10110101"
    decimal = int(binary, 2)
    print(f"Binary {binary} = Decimal {decimal}")
    
    # Decimal to Hexadecimal
    print_subheader("Decimal to Hexadecimal")
    dec_num = 255
    hex_num = hex(dec_num)
    print(f"Decimal {dec_num} = Hexadecimal {hex_num}")
    
    # Octal representation
    print_subheader("Octal Representation")
    oct_num = oct(64)
    print(f"Decimal 64 = Octal {oct_num}")

# ============================================================
# EXERCISE 2: ASCII, PARITY, AND BCD
# ============================================================

def ex2_ascii_parity_bcd():
    """Demonstrate ASCII encoding, parity bits, and BCD."""
    print_header("Exercise 2: ASCII, Parity, and BCD")
    
    # ASCII Encoding
    print_subheader("ASCII Character Encoding")
    char = 'A'
    ascii_val = ord(char)
    binary_repr = format(ascii_val, '08b')
    print(f"Character '{char}' = ASCII {ascii_val} = Binary {binary_repr}")
    
    # Even Parity
    print_subheader("Even Parity Bit Calculation")
    data = "1011010"
    ones_count = data.count('1')
    parity_bit = '0' if ones_count % 2 == 0 else '1'
    print(f"Data: {data}")
    print(f"Number of 1s: {ones_count}")
    print(f"Even parity bit: {parity_bit}")
    print(f"Transmitted data: {data}{parity_bit}")
    
    # BCD Encoding
    print_subheader("Binary Coded Decimal (BCD)")
    decimal_digit = 9
    bcd = format(decimal_digit, '04b')
    print(f"Decimal {decimal_digit} = BCD {bcd}")

# ============================================================
# EXERCISE 3: BOOLEAN ALGEBRA
# ============================================================

def ex3_boolean_algebra():
    """Demonstrate boolean algebra operations."""
    print_header("Exercise 3: Boolean Algebra Simplification")
    
    print_subheader("Boolean Operations")
    A, B, C = True, False, True
    
    print(f"A = {A}, B = {B}, C = {C}")
    print(f"A AND B = {A and B}")
    print(f"A OR B = {A or B}")
    print(f"NOT A = {not A}")
    print(f"A XOR B = {A != B}")
    
    print_subheader("De Morgan's Laws")
    print(f"NOT(A AND B) = {not(A and B)}")
    print(f"(NOT A) OR (NOT B) = {(not A) or (not B)}")
    print(f"These are equal: {not(A and B) == ((not A) or (not B))}")
    
    print_subheader("Truth Table: A AND B OR C")
    print("A | B | C | A AND B | Result")
    print("-" * 35)
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                and_result = a and b
                final = and_result or c
                print(f"{int(a)} | {int(b)} | {int(c)} |    {int(and_result)}    |   {int(final)}")

# ============================================================
# EXERCISE 4: MULTIPLEXERS
# ============================================================

def ex4_multiplexers():
    """Demonstrate multiplexer functionality."""
    print_header("Exercise 4: Logic Functions and Multiplexers")
    
    print_subheader("4-to-1 Multiplexer")
    inputs = [3, 7, 2, 5]  # I0, I1, I2, I3
    
    print("Inputs: I0=3, I1=7, I2=2, I3=5")
    print("\nSelect | Output")
    print("-" * 16)
    
    for select in range(4):
        output = inputs[select]
        select_binary = format(select, '02b')
        print(f"  {select_binary}   |   {output}")

# ============================================================
# EXERCISE 5: COMBINATIONAL CIRCUITS
# ============================================================

def ex5_combinational_circuits():
    """Demonstrate combinational circuit operations."""
    print_header("Exercise 5: Combinational Logic Circuits")
    
    print_subheader("4-bit Binary Adder")
    a = 0b1010  # 10 in decimal
    b = 0b0111  # 7 in decimal
    sum_result = a + b
    
    print(f"A:       {format(a, '04b')} ({a})")
    print(f"B:       {format(b, '04b')} ({b})")
    print(f"Sum:     {format(sum_result, '05b')} ({sum_result})")
    
    print_subheader("4-bit Comparator")
    x, y = 12, 9
    print(f"X = {x}, Y = {y}")
    print(f"X > Y:  {x > y}")
    print(f"X = Y:  {x == y}")
    print(f"X < Y:  {x < y}")
    
    print_subheader("Priority Encoder (8-to-3)")
    inputs = [0, 0, 0, 1, 0, 1, 0, 0]  # I7...I0
    print(f"Inputs: {inputs}")
    
    for i in range(len(inputs) - 1, -1, -1):
        if inputs[i] == 1:
            output = format(i, '03b')
            print(f"Highest priority input: I{i}")
            print(f"Output: {output}")
            break

# ============================================================
# EXERCISE 6: SEQUENTIAL CIRCUITS
# ============================================================

def ex6_sequential_circuits():
    """Demonstrate sequential circuit behavior."""
    print_header("Exercise 6: Sequential Circuits")
    
    print_subheader("D Flip-Flop Operation")
    print("Clock | D | Q(next)")
    print("-" * 21)
    
    q = 0
    test_inputs = [1, 1, 0, 1, 0, 0, 1]
    
    for d in test_inputs:
        q = d  # D flip-flop: Q follows D on clock edge
        print(f"  ↑   | {d} |   {q}")
    
    print_subheader("4-bit Counter")
    print("Clock | Count (Binary) | Count (Decimal)")
    print("-" * 42)
    
    count = 0
    for clk in range(16):
        binary = format(count, '04b')
        print(f"  {clk:2d}  |     {binary}      |      {count:2d}")
        count = (count + 1) % 16

# ============================================================
# EXERCISE 7: ADVANCED DIGITAL DESIGN
# ============================================================

def ex7_advanced_design():
    """Demonstrate advanced digital design concepts."""
    print_header("Exercise 7: Advanced Digital Design")
    
    print_subheader("State Machine: Traffic Light Controller")
    states = ["GREEN", "YELLOW", "RED"]
    durations = [30, 5, 25]  # seconds
    
    print("State Transitions:")
    for i, state in enumerate(states):
        next_state = states[(i + 1) % len(states)]
        print(f"{state:8s} ({durations[i]:2d}s) -> {next_state}")
    
    print_subheader("Simple Memory Array (4x4 bits)")
    memory = [
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    
    print("Address | Data")
    print("-" * 16)
    for addr, data in enumerate(memory):
        data_str = ''.join(map(str, data))
        print(f"  {format(addr, '02b')}    | {data_str}")
    
    print_subheader("Timing Analysis")
    clock_period = 10  # ns
    propagation_delay = 2.5  # ns
    setup_time = 0.5  # ns
    
    print(f"Clock Period: {clock_period} ns")
    print(f"Propagation Delay: {propagation_delay} ns")
    print(f"Setup Time: {setup_time} ns")
    print(f"Maximum Frequency: {1000 / clock_period:.1f} MHz")
    print(f"Available time for logic: {clock_period - propagation_delay - setup_time} ns")

# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """Run all exercise demonstrations."""
    print("\n" + "=" * 60)
    print("COMPUTER SYSTEMS AND LOGIC".center(60))
    print("Course Summary and Exercises".center(60))
    print("=" * 60)
    
    exercises = [
        ("Number Systems and Conversions", ex1_number_systems),
        ("ASCII, Parity, and BCD", ex2_ascii_parity_bcd),
        ("Boolean Algebra Simplification", ex3_boolean_algebra),
        ("Logic Functions and Multiplexers", ex4_multiplexers),
        ("Combinational Logic Circuits", ex5_combinational_circuits),
        ("Sequential Circuits", ex6_sequential_circuits),
        ("Advanced Digital Design", ex7_advanced_design)
    ]
    
    print("\nAvailable Exercises:")
    for i, (title, _) in enumerate(exercises, 1):
        print(f"  {i}. {title}")
    print("  0. Run all exercises")
    
    try:
        choice = input("\nEnter your choice (0-7): ").strip()
        
        if choice == '0':
            for _, func in exercises:
                func()
                input("\nPress Enter to continue to next exercise...")
        elif choice.isdigit() and 1 <= int(choice) <= 7:
            exercises[int(choice) - 1][1]()
        else:
            print("\nInvalid choice. Running all exercises...")
            for _, func in exercises:
                func()
                input("\nPress Enter to continue to next exercise...")
    
    except KeyboardInterrupt:
        print("\n\nExiting...")
    except Exception as e:
        print(f"\nError: {e}")
    
    print("\n" + "=" * 60)
    print("Thank you for reviewing Computer Systems and Logic!".center(60))
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
