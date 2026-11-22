# scripts/build_cbse9_mgm_ch11_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 11: The World of Algorithms
Part 3:
- Subtopic 11.3.1: Sieve of Eratosthenes for prime numbers
- Subtopic 11.3.2: Algorithms for divisibility tests and prime factorisation
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 11
CH_NAME = "The World of Algorithms"

# ==============================================================================
# SUBTOPIC 11.3.1: Sieve of Eratosthenes for prime numbers
# ==============================================================================
def gen_11_3_1():
    tc = "CBSE-9-MGM-11-11.3.1"
    tname = "Sieve of Eratosthenes for prime numbers"

    # Arch 0: Nature and historical origin of the Sieve of Eratosthenes
    arch0 = {
        'data': [
            ("Which ancient Greek mathematician and chief librarian of Alexandria invented the famous algorithm for finding all prime numbers up to a given limit?", "Eratosthenes of Cyrene (3rd century BC)", "Invented the Sieve of Eratosthenes"),
            ("How does the Sieve of Eratosthenes find all prime numbers up to N?", "By systematically marking (crossing out) all multiples of each prime starting from 2, leaving only primes uncrossed", "Sieve filtering mechanism"),
            ("Why is 1 immediately crossed out at the very beginning of the Sieve of Eratosthenes?", "Because 1 is neither prime nor composite by modern mathematical definition", "1 is a unit, not prime"),
            ("What is the first prime number whose multiples are crossed out in the Sieve?", "2 (the smallest and only even prime)", "Multiples of 2: 4, 6, 8, ..."),
            ("After crossing out multiples of 2, what is the next uncrossed number whose multiples are crossed out?", "3", "Multiples of 3: 6, 9, 12, ..."),
            ("Why does the algorithm NOT need to cross out multiples of 4 after 3?", "Because 4 is already crossed out as a multiple of 2", "Composite numbers already crossed"),
            ("When crossing out multiples of a prime p, at which multiple does the algorithm first need to start crossing out?", "p^2 (since all smaller multiples 2p, 3p, ... have already been crossed out by smaller primes)", "Optimization: start at p^2"),
            ("When finding primes up to 100, why do we only need to test and cross out multiples of primes up to 7 (2, 3, 5, 7)?", "Because the next prime is 11, and 11^2 = 121 > 100", "Square root stopping threshold"),
            ("What physical tool inspired the name 'Sieve' (koskinon in Greek)?", "A kitchen/grain sieve that filters out fine flour while holding back large chaff", "Metaphor of filtering numbers"),
            ("Is the Sieve of Eratosthenes still used in modern computational number theory?", "Yes, it is the benchmark and most efficient elementary algorithm for generating prime lists up to billions", "Enduring algorithmic importance")
        ],
        'tmpls': [
            "{0}",
            "In the mathematical study of the Sieve of Eratosthenes: {0}",
            "Identify the correct historical or algorithmic fact: {0}",
            "Which description characterizes: {0}?",
            "What is the mathematical reason for: {0}?",
            "Analyze the Sieve of Eratosthenes: {0}",
            "Determine the accurate step in the Sieve: {0}",
            "In NCERT Class 9 Ganita Manjari Chapter 11: {0}",
            "Select the accurate algorithmic insight: {0}",
            "Regarding prime generation algorithms: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Euclid of Alexandria",
                "Pythagoras of Samos",
                "Archimedes of Syracuse"
            ] if "Eratosthenes" in item[1] else [
                "By dividing every number by all integers up to N",
                "By testing random numbers",
                "Primes cannot be found by an algorithm"
            ],
            f"**Step 1: Understand the mechanism of the Sieve of Eratosthenes.**\nThe algorithm writes numbers from 2 to \\( N \\), and for each prime \\( p \\), eliminates all its composite multiples \\( p^2, p(p+1), \\dots \\).\n\n**Step 2: Detail the concept.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: The Square Root Stopping Criterion (Primes up to sqrt(N))
    arch1 = {
        'data': [
            (100, 7, "sqrt(100) = 10, primes <= 10 are 2, 3, 5, 7 (11^2 = 121 > 100)"),
            (50, 7, "sqrt(50) ≈ 7.07, primes <= 7 are 2, 3, 5, 7"),
            (30, 5, "sqrt(30) ≈ 5.47, primes <= 5 are 2, 3, 5"),
            (200, 13, "sqrt(200) ≈ 14.14, primes <= 14 are 2, 3, 5, 7, 11, 13"),
            (150, 11, "sqrt(150) ≈ 12.24, primes <= 12 are 2, 3, 5, 7, 11"),
            (400, 19, "sqrt(400) = 20, largest prime <= 20 is 19"),
            (25, 5, "sqrt(25) = 5, primes <= 5 are 2, 3, 5"),
            (120, 7, "sqrt(120) ≈ 10.95, primes <= 10 are 2, 3, 5, 7"),
            (500, 19, "sqrt(500) ≈ 22.36, primes <= 22 are 2, 3, 5, 7, 11, 13, 17, 19"),
            (1000, 31, "sqrt(1000) ≈ 31.62, largest prime <= 31 is 31")
        ],
        'tmpls': [
            "When using the Sieve of Eratosthenes to find all primes up to {0}, what is the largest prime number whose multiples must be crossed out?",
            "Up to which prime number do we need to cross out multiples to find all primes less than or equal to {0}?",
            "In sieving numbers up to {0}, the algorithm terminates crossing out when the prime reaches: {1}. Why?",
            "What is the maximum prime factor tested when sieving up to {0}?",
            "To identify all primes up to {0}, we test primes up to \\( \\sqrt{{{0}}} \\). What is the highest such prime?",
            "Determine the last prime whose multiples must be eliminated in a sieve of size {0}:",
            "Calculate the stopping prime for Sieve of Eratosthenes on bound {0}:",
            "Find the largest prime p such that \\( p^2 \\le {0} \\):",
            "What is the maximum prime whose multiples are sieved for N = {0}?",
            "Evaluate the threshold prime for N = {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 2}", f"{item[1] + 4}", f"{item[1] - 2 if item[1] > 2 else 3}"],
            f"**Step 1: Calculate \\( \\sqrt{{N}} \\) for \\( N = {item[0]} \\).**\nAny composite number \\( \\le N \\) must have at least one prime factor \\( \\le \\sqrt{{N}} \\).\n\n**Step 2: Find the largest prime \\( \\le \\sqrt{{{item[0]}}} \\).**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe largest prime is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Prime Counting (Prime Counting Function pi(N))
    arch2 = {
        'data': [
            (10, 4, "[2, 3, 5, 7]"),
            (20, 8, "[2, 3, 5, 7, 11, 13, 17, 19]"),
            (30, 10, "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]"),
            (50, 15, "15 primes up to 50"),
            (100, 25, "25 primes up to 100"),
            ("between 1 and 25", 9, "[2, 3, 5, 7, 11, 13, 17, 19, 23]"),
            ("between 50 and 100", 10, "25 - 15 = 10 primes: 53, 59, 61, 67, 71, 73, 79, 83, 89, 97"),
            ("between 20 and 40", 4, "[23, 29, 31, 37]"),
            ("between 90 and 100", 1, "Only one prime: 97"),
            ("between 1 and 15", 6, "[2, 3, 5, 7, 11, 13]")
        ],
        'tmpls': [
            "How many prime numbers are there up to {0}?",
            "Using the Sieve of Eratosthenes, count the total number of primes {0}:",
            "What is the value of \\( \\pi({0}) \\) (the number of primes <= {0})?",
            "Find the total number of prime numbers in the range {0}:",
            "Determine the count of prime numbers {0}:",
            "Calculate how many primes exist {0}:",
            "What is the total count of primes found by the sieve {0}?",
            "How many uncrossed numbers remain in the sieve {0}?",
            "Evaluate the number of primes {0}:",
            "Compute the prime count for {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 2}", f"{item[1] - 2 if item[1] > 2 else item[1] + 4}", f"{item[1] + 5}"],
            f"**Step 1: List all prime numbers {item[0]}.**\n{item[2]}.\n\n**Step 2: Count the primes.**\nTotal count = {item[1]}.\n\n**Step 3: State the answer.**\nThere are {item[1]} prime numbers."
        ),
        'diff': 'medium'
    }

    # Arch 3: Primality Testing via Trial Division up to sqrt(N)
    arch3 = {
        'data': [
            (97, "Prime", "sqrt(97) ≈ 9.8. Test primes 2, 3, 5, 7. None divide 97, so 97 is prime"),
            (91, "Composite (7 * 13)", "sqrt(91) ≈ 9.5. Testing 7 gives 91 / 7 = 13"),
            (87, "Composite (3 * 29)", "Sum of digits 8 + 7 = 15 (divisible by 3)"),
            (89, "Prime", "sqrt(89) ≈ 9.4. Primes 2, 3, 5, 7 do not divide 89"),
            (51, "Composite (3 * 17)", "5 + 1 = 6 (divisible by 3)"),
            (53, "Prime", "sqrt(53) ≈ 7.28. Primes 2, 3, 5, 7 do not divide 53"),
            (73, "Prime", "sqrt(73) ≈ 8.54. Primes 2, 3, 5, 7 do not divide 73"),
            (119, "Composite (7 * 17)", "sqrt(119) ≈ 10.9. Testing 7 gives 119 / 7 = 17"),
            (143, "Composite (11 * 13)", "143 = 11 * 13"),
            (127, "Prime", "sqrt(127) ≈ 11.26. Primes 2, 3, 5, 7, 11 do not divide 127")
        ],
        'tmpls': [
            "Determine whether {0} is prime or composite by testing prime factors up to \\( \\sqrt{{{0}}} \\):",
            "Is the number {0} prime or composite?",
            "Apply the primality testing algorithm to {0}:",
            "Using trial division up to \\( \\sqrt{N} \\), classify {0}:",
            "Evaluate whether {0} has any prime factors:",
            "Check if {0} is a prime number:",
            "Determine the status of {0} using prime division tests:",
            "Classify the integer {0}:",
            "What is the classification of {0} via prime testing?",
            "Run the primality test on {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Composite (divisible by 2)" if "Prime" in item[1] else "Prime",
                "Neither prime nor composite",
                "Even prime"
            ],
            f"**Step 1: Determine \\( \\sqrt{{{item[0]}}} \\).**\nTest prime divisors up to \\( \\lfloor\\sqrt{{{item[0]}}}\\rfloor \\).\n\n**Step 2: Carry out divisibility checks.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[0]} is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Twin Primes in the Sieve
    arch4 = {
        'data': [
            ("(3, 5)", 2, "3 and 5 are both prime and differ by 2"),
            ("(5, 7)", 2, "5 and 7 are both prime and differ by 2"),
            ("(11, 13)", 2, "11 and 13 are both prime and differ by 2"),
            ("(17, 19)", 2, "17 and 19 are both prime and differ by 2"),
            ("(29, 31)", 2, "29 and 31 are both prime and differ by 2"),
            ("(41, 43)", 2, "41 and 43 are both prime and differ by 2"),
            ("(59, 61)", 2, "59 and 61 are both prime and differ by 2"),
            ("(71, 73)", 2, "71 and 73 are both prime and differ by 2"),
            ("How many pairs of twin primes exist between 1 and 100?", 8, "Eight pairs: (3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73)"),
            ("What is the famous Twin Prime Conjecture in mathematics?", "There are infinitely many pairs of twin primes", "Famous unsolved conjecture")
        ],
        'tmpls': [
            "What are 'Twin Primes'? Verify if {0} is a twin prime pair:",
            "In prime number theory, {0}. What is the property?",
            "Identify the twin prime pair among the numbers: {0}:",
            "Examine the prime pair {0}:",
            "What makes {0} a pair of twin primes?",
            "Analyze the twin prime relationship in: {0}:",
            "Determine the true statement regarding: {0}:",
            "Which description characterizes: {0}?",
            "In NCERT Class 9 number theory: {0}",
            "Select the accurate twin prime fact: {0}"
        ],
        'calc': lambda item: (
            f"Twin Primes (difference = 2)" if isinstance(item[1], int) and item[1] == 2 else (f"{item[1]}" if isinstance(item[1], int) else item[1]),
            [
                "Co-primes only (not both prime)",
                "Difference of 4 (Cousin Primes)",
                "Twin primes must both be even"
            ] if isinstance(item[1], int) and item[1] == 2 else [
                "4",
                "12",
                "Twin primes end after 1,000"
            ],
            f"**Step 1: Recall the definition of Twin Primes.**\nTwo prime numbers are called Twin Primes if they differ by exactly 2 (i.e. \\( p_2 - p_1 = 2 \\)).\n\n**Step 2: Check the pair.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Algorithmic Complexity of Sieve of Eratosthenes
    arch5 = {
        'data': [
            ("What is the time complexity of the standard Sieve of Eratosthenes for numbers up to N?", "O(N log log N)", "Near-linear time complexity"),
            ("Why is the Sieve of Eratosthenes vastly faster than checking each number individually by trial division up to N?", "Trial division takes O(N * sqrt(N)) steps, whereas the Sieve takes O(N log log N) steps by avoiding repeated trial divisions", "Huge asymptotic speedup"),
            ("For N = 1,000,000, approximately how many operations does the Sieve of Eratosthenes perform compared to trial division?", "Sieve takes ~3 million operations, while trial division takes ~1 billion operations (over 300x faster)", "Quantitative performance comparison"),
            ("What is the space complexity of the basic Sieve of Eratosthenes storing an array of booleans from 2 to N?", "O(N) memory space", "Requires an array of size N"),
            ("How does the 'Segmented Sieve' optimize memory for very large N (e.g. N = 10^12)?", "It sieves the range in small blocks of size sqrt(N) that fit in CPU cache memory, using only O(sqrt(N)) space", "Cache-efficient segmented sieve"),
            ("Why does the inner loop of the sieve start at j = p^2 instead of j = 2p?", "Because all smaller composite multiples 2p, 3p, ..., (p-1)p have already been crossed out by smaller prime factors", "Inner loop optimization"),
            ("In the inner loop, what is the step size by which index j increments?", "j = j + p (stepping through consecutive multiples of p)", "Stride equal to p"),
            ("What data structure is typically used to implement the Sieve in code?", "A boolean array (or bitset) where index represents the number and value represents prime status (true/false)", "Boolean lookup table"),
            ("Which modern algorithm outperforms the Sieve of Eratosthenes asymptotically by eliminating redundant crossings?", "The Sieve of Atkin (O(N / log log N))", "Modern sieve algorithm"),
            ("Why does studying the Sieve of Eratosthenes in Class 9 provide a masterclass in algorithmic thinking?", "Because it replaces expensive individual division tests with cheap sequential addition/marking", "Core computational lesson")
        ],
        'tmpls': [
            "{0}",
            "In algorithmic analysis of prime sieves: {0}",
            "Regarding the computational efficiency of the Sieve of Eratosthenes: {0}",
            "Identify the algorithmic property: {0}",
            "Which statement accurately explains: {0}?",
            "What is the mathematical or computational reason: {0}?",
            "Analyze the sieve algorithm complexity: {0}",
            "Determine the accurate answer: {0}",
            "In computer science and Class 9 mathematics: {0}",
            "Select the accurate algorithmic insight: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "O(N^2) quadratic time",
                "O(2^N) exponential time",
                "Trial division is faster than the Sieve"
            ],
            f"**Step 1: Understand the complexity analysis of the Sieve of Eratosthenes.**\nThe sum of reciprocals of primes \\( \\sum_{{p \\le N}} \\frac{{1}}{{p}} \\sim \\ln(\\ln N) \\) leads to \\( O(N \\log \\log N) \\) operations.\n\n**Step 2: Detail the property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Prime Distributions and Gaps
    arch6 = {
        'data': [
            ("What is the ONLY even prime number?", "2", "All other even numbers are multiples of 2 and thus composite"),
            ("What is the only set of three consecutive odd prime numbers (prime triplet)?", "(3, 5, 7)", "Every third odd number is a multiple of 3, so no other triplet can exist"),
            ("Can there be any other prime triplet of the form (p, p+2, p+4) besides (3, 5, 7)?", "No, because among p, p+2, and p+4, exactly one must be a multiple of 3", "Modulo 3 proof of unique prime triplet"),
            ("What is the largest prime number less than 100?", "97", "97 is prime; 98, 99, 100 are composite"),
            ("What is the smallest two-digit prime number?", "11", "Smallest 2-digit prime"),
            ("What is the smallest three-digit prime number?", "101", "100 is composite, 101 is prime"),
            ("Can you find a sequence of 100 consecutive composite numbers with NO primes among them?", "Yes: (101! + 2), (101! + 3), ..., (101! + 101) are all composite", "Arbitrarily large prime gaps theorem"),
            ("What does the Prime Number Theorem state about the density of primes near N?", "The probability that a random number near N is prime is approximately 1 / ln(N)", "Asymptotic density of primes"),
            ("Are primes distributed evenly across the number line?", "No, they thin out logarithmically on average, but exhibit erratic local gaps", "Prime distribution law"),
            ("What is Goldbach's Conjecture regarding even numbers greater than 2?", "Every even integer greater than 2 can be written as the sum of two primes", "Goldbach's famous conjecture")
        ],
        'tmpls': [
            "{0}",
            "In the mathematical study of prime distributions: {0}",
            "Identify the unique prime property: {0}",
            "Which statement correctly characterizes: {0}?",
            "What is the mathematical fact regarding: {0}?",
            "Analyze the prime distribution: {0}",
            "Determine the accurate answer: {0}",
            "In foundational number theory: {0}",
            "Select the accurate prime property: {0}",
            "Evaluate the prime number concept: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "4",
                "(5, 7, 9)",
                "No consecutive composites can exceed 10"
            ],
            f"**Step 1: Understand the structure and distribution of primes.**\nPrimes follow strict modular arithmetic constraints while thinning out asymptotically.\n\n**Step 2: Detail the specific property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Sieve Implementation Pseudocode Tracing
    arch7 = {
        'data': [
            ("Sieve up to 20: Primes remaining after crossing multiples of 2 and 3:", "[2, 3, 5, 7, 11, 13, 17, 19]", "8 primes up to 20"),
            ("In an array isPrime[2..N] initialized to true, what is the value of isPrime[9] after crossing multiples of 3?", "false", "9 is crossed out as 3 * 3"),
            ("What is the value of isPrime[25] after crossing multiples of 5?", "false", "25 is crossed out as 5 * 5"),
            ("What is the value of isPrime[49] after crossing multiples of 7?", "false", "49 is crossed out as 7 * 7"),
            ("What is the value of isPrime[31] after the sieve finishes up to 50?", "true", "31 remains uncrossed (it is prime)"),
            ("How many times is the number 30 crossed out if multiples are marked naively?", "3 times (by 2, 3, and 5)", "30 = 2 * 3 * 5 has 3 distinct prime factors"),
            ("Why does marking multiples starting from p^2 avoid crossing out 30 when p = 5?", "Because 5^2 = 25, and 30 was already crossed out when p = 2 and p = 3", "Avoids duplicate work for small multiples"),
            ("How many primes are there between 70 and 80?", 3, "71, 73, 79 (3 primes)"),
            ("How many primes are there between 80 and 90?", 2, "83, 89 (2 primes)"),
            ("What is the sum of the first four prime numbers (2 + 3 + 5 + 7)?", 17, "2 + 3 + 5 + 7 = 17")
        ],
        'tmpls': [
            "Trace the Sieve of Eratosthenes algorithm: {0}:",
            "What is the output or status of the sieve trace: {0}?",
            "In tracking the execution of the sieve: {0}:",
            "Determine the algorithmic state: {0}:",
            "Evaluate the sieve execution result: {0}:",
            "Find the required quantity from the sieve trace: {0}:",
            "Calculate the result for: {0}:",
            "What value is returned by the sieve: {0}?",
            "Solve the algorithm trace: {0}:",
            "Follow the sieve instructions: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [
                "true" if str(item[1]) == "false" else ("false" if str(item[1]) == "true" else ("[2, 3, 5, 7, 11]" if "[" in str(item[1]) else (f"{int(item[1]) + 2}" if str(item[1]).lstrip('-').isdigit() else "4 times (by 2, 3, 5, 6)"))),
                f"{int(item[1]) - 1}" if str(item[1]).lstrip('-').isdigit() else ("[2, 3, 5, 7, 11, 13]" if "[" in str(item[1]) else ("undefined" if str(item[1]) in ["true", "false"] else "Because 5 is an odd number")),
                "0" if str(item[1]).lstrip('-').isdigit() else ("Neither prime nor composite" if str(item[1]) in ["true", "false"] else ("[2, 3, 5, 7]" if "[" in str(item[1]) else "None of the above"))
            ],
            f"**Step 1: Follow the Sieve of Eratosthenes algorithm step-by-step.**\n\n**Step 2: Trace the variable states.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 11.3.2: Algorithms for divisibility tests and prime factorisation
# ==============================================================================
def gen_11_3_2():
    tc = "CBSE-9-MGM-11-11.3.2"
    tname = "Algorithms for divisibility tests and prime factorisation"

    # Arch 0: Divisibility Tests for Powers of 2 (2, 4, 8)
    arch0 = {
        'data': [
            ("A number is divisible by 2 if and only if:", "Its last digit is even (0, 2, 4, 6, 8)", "Divisibility by 2 rule"),
            ("A number is divisible by 4 if and only if:", "The number formed by its last two digits is divisible by 4 (or ends in 00)", "Divisibility by 4 rule"),
            ("A number is divisible by 8 if and only if:", "The number formed by its last three digits is divisible by 8 (or ends in 000)", "Divisibility by 8 rule"),
            ("Why does the divisibility test for 4 only look at the last two digits?", "Because 100 is divisible by 4 (100 = 4 * 25), so all hundreds, thousands, etc. are automatically multiples of 4", "Modulo 100 argument"),
            ("Why does the divisibility test for 8 only look at the last three digits?", "Because 1000 is divisible by 8 (1000 = 8 * 125)", "Modulo 1000 argument"),
            ("Is 35,724 divisible by 4?", "Yes, because the last two digits 24 are divisible by 4 (24 / 4 = 6)", "24 / 4 = 6"),
            ("Is 148,632 divisible by 8?", "Yes, because the last three digits 632 are divisible by 8 (632 / 8 = 79)", "632 / 8 = 79"),
            ("Is 4,591,818 divisible by 4?", "No, because the last two digits 18 are not divisible by 4 (18 / 4 = 4.5)", "18 is not divisible by 4"),
            ("What is the general pattern for divisibility by 2^k?", "Check whether the number formed by the last k digits is divisible by 2^k", "General 2^k rule"),
            ("Is 78,540 divisible by both 2 and 4?", "Yes, it ends in 0 (even) and last two digits 40 are divisible by 4", "Satisfies both tests")
        ],
        'tmpls': [
            "{0}",
            "In algorithmic divisibility tests: {0}",
            "Apply the divisibility rule for powers of 2: {0}",
            "Which rule or evaluation is correct for: {0}?",
            "What is the mathematical justification in: {0}?",
            "Analyze the divisibility test: {0}",
            "Determine the accurate divisibility result: {0}",
            "In NCERT Class 9 arithmetic algorithms: {0}",
            "Select the accurate mathematical explanation: {0}",
            "Check divisibility by 2, 4, or 8: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The sum of all its digits must be even",
                "Its first digit must be divisible by 4",
                "All its digits must be even"
            ],
            f"**Step 1: State the relevant divisibility rule.**\n- By 2: last digit.\n- By 4: last 2 digits.\n- By 8: last 3 digits.\n\n**Step 2: Evaluate the number.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Divisibility Tests for 3 and 9 (Sum of Digits)
    arch1 = {
        'data': [
            ("A number is divisible by 3 if and only if:", "The sum of all its digits is divisible by 3", "Sum of digits mod 3"),
            ("A number is divisible by 9 if and only if:", "The sum of all its digits is divisible by 9", "Sum of digits mod 9"),
            ("Why does the sum of digits test work for 3 and 9?", "Because 10 ≡ 1 (mod 9) and 10 ≡ 1 (mod 3), so any power 10^k leaves remainder 1", "10^k = 99...9 + 1"),
            ("Is 45,621 divisible by 3?", "Yes, because 4 + 5 + 6 + 2 + 1 = 18, which is divisible by 3 (18 / 3 = 6)", "Digit sum = 18"),
            ("Is 45,621 divisible by 9?", "Yes, because the digit sum is 18, which is divisible by 9 (18 / 9 = 2)", "Digit sum 18 is multiple of 9"),
            ("Is 72,531 divisible by 9?", "Yes, 7 + 2 + 5 + 3 + 1 = 18 (divisible by 9)", "Digit sum = 18"),
            ("Is 81,425 divisible by 3?", "No, because 8 + 1 + 4 + 2 + 5 = 20, which is not divisible by 3", "Digit sum 20"),
            ("If a number is divisible by 9, is it always divisible by 3?", "Yes, because any multiple of 9 is automatically a multiple of 3", "Transitivity: 3 | 9"),
            ("If a number is divisible by 3, is it always divisible by 9?", "No (counterexample: 6, 12, 15 are divisible by 3 but not by 9)", "3 does not imply 9"),
            ("What single digit x makes the number 5,2x4 divisible by 9?", "7 (since 5 + 2 + x + 4 = 11 + x = 18 -> x = 7)", "11 + x = 18 -> x = 7")
        ],
        'tmpls': [
            "{0}",
            "In algorithmic divisibility tests for 3 and 9: {0}",
            "Apply the sum of digits test: {0}",
            "What is the mathematical reason or result for: {0}?",
            "Identify the correct divisibility evaluation: {0}",
            "Analyze the digit sum rule: {0}",
            "Determine the accurate answer: {0}",
            "In Class 9 number theory and algorithms: {0}",
            "Select the accurate divisibility fact: {0}",
            "Check divisibility by 3 or 9: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The last digit must be 3 or 9",
                "The product of all digits must be 9",
                "The number must be odd"
            ] if not item[1].isdigit() else [
                "2",
                "4",
                "9"
            ],
            f"**Step 1: Compute the sum of the digits.**\n\n**Step 2: Test divisibility by 3 or 9.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Divisibility Tests for 5, 10, and 11
    arch2 = {
        'data': [
            ("A number is divisible by 5 if and only if its last digit is:", "0 or 5", "Divisibility by 5"),
            ("A number is divisible by 10 if and only if its last digit is:", "0", "Divisibility by 10"),
            ("A number is divisible by 11 if and only if:", "The difference between the sum of digits in odd places and sum of digits in even places is 0 or a multiple of 11", "Alternating digit sum test for 11"),
            ("Why does the alternating sum test work for 11?", "Because 10 ≡ -1 (mod 11), so 10^k alternates between +1 and -1", "10^k ≡ (-1)^k mod 11"),
            ("Is 1,331 divisible by 11?", "Yes: (1 + 3) - (3 + 1) = 4 - 4 = 0 (divisible by 11)", "Difference is 0 -> 11^3 = 1331"),
            ("Is 9,185 divisible by 11?", "No: (9 + 8) - (1 + 5) = 17 - 6 = 11, which IS divisible by 11! So 9,185 is divisible by 11", "Difference = 11, divisible!"),
            ("Is 61,809 divisible by 11?", "Yes: (6 + 8 + 9) - (1 + 0) = 23 - 1 = 22, which is divisible by 11 (22 / 11 = 2)", "Difference = 22"),
            ("Is 4,529 divisible by 11?", "No: (4 + 2) - (5 + 9) = 6 - 14 = -8 (not a multiple of 11)", "Difference = -8"),
            ("What single digit x makes the number 7x31 divisible by 11?", "9 (since (7 + 3) - (x + 1) = 10 - x - 1 = 9 - x = 0 -> x = 9)", "9 - x = 0 -> x = 9"),
            ("Is 50,005 divisible by 11?", "No: (5 + 0 + 5) - (0 + 0) = 10 - 0 = 10 (not divisible by 11)", "Difference is 10")
        ],
        'tmpls': [
            "{0}",
            "In algorithmic divisibility tests for 5, 10, and 11: {0}",
            "Apply the alternating sum rule for 11: {0}",
            "Determine the divisibility: {0}",
            "Which statement correctly evaluates: {0}?",
            "What is the mathematical justification for: {0}?",
            "Analyze the divisibility test for 11: {0}",
            "Find the unknown digit or status in: {0}:",
            "In Class 9 arithmetic rules: {0}",
            "Select the accurate divisibility result: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The sum of all digits must be 11",
                "The last two digits must be 11",
                "All digits must be equal"
            ] if not item[1].isdigit() else [
                "2",
                "5",
                "0"
            ],
            f"**Step 1: State the alternating sum rule for 11.**\n\\( \\Delta = \\sum \\text{{Odd place digits}} - \\sum \\text{{Even place digits}} \\).\n\n**Step 2: Evaluate \\( \\Delta \\).**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Composite Divisibility Rules (6, 12, 15, 18)
    arch3 = {
        'data': [
            ("A number is divisible by 6 if and only if it is divisible by both:", "2 and 3 (coprime factors of 6)", "6 = 2 * 3, gcd(2, 3) = 1"),
            ("A number is divisible by 12 if and only if it is divisible by both:", "3 and 4 (coprime factors of 12)", "12 = 3 * 4, gcd(3, 4) = 1"),
            ("Why CANNOT we test divisibility by 12 by checking divisibility by 2 and 6?", "Because 2 and 6 are NOT coprime (gcd(2, 6) = 2); e.g. 18 is divisible by 2 and 6 but NOT by 12", "Coprime factor rule requirement"),
            ("A number is divisible by 15 if and only if it is divisible by both:", "3 and 5 (coprime factors of 15)", "15 = 3 * 5, gcd(3, 5) = 1"),
            ("A number is divisible by 18 if and only if it is divisible by both:", "2 and 9 (coprime factors of 18)", "18 = 2 * 9, gcd(2, 9) = 1"),
            ("Is 7,524 divisible by 6?", "Yes, it is even (ends in 4) and digit sum 7+5+2+4 = 18 is divisible by 3", "Divisible by 2 and 3"),
            ("Is 3,456 divisible by 12?", "Yes, digit sum 18 is divisible by 3, and last two digits 56 are divisible by 4", "Divisible by 3 and 4"),
            ("Is 8,145 divisible by 15?", "Yes, it ends in 5, and digit sum 8+1+4+5 = 18 is divisible by 3", "Divisible by 5 and 3"),
            ("Is 5,472 divisible by 18?", "Yes, it is even and digit sum 5+4+7+2 = 18 is divisible by 9", "Divisible by 2 and 9"),
            ("What is the general Coprime Factor Divisibility Theorem?", "If a number is divisible by coprime integers m and n, it is divisible by their product m * n", "Fundamental theorem of composite divisibility")
        ],
        'tmpls': [
            "{0}",
            "In composite divisibility algorithms: {0}",
            "Apply the coprime factor rule: {0}",
            "Why must factors be coprime: {0}?",
            "Identify the correct test for composite divisibility: {0}",
            "Analyze the divisibility condition: {0}",
            "Determine the accurate composite test: {0}",
            "Which pair of tests confirms: {0}?",
            "In NCERT Class 9 modular divisibility: {0}",
            "Select the accurate composite divisibility fact: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "2 and 6",
                "1 and 12 only",
                "Any two factors regardless of common divisors"
            ],
            f"**Step 1: State the Coprime Factor Rule.**\nTo test divisibility by composite \\( C = m \\times n \\), \\( m \\) and \\( n \\) must be coprime (\\( \\gcd(m, n) = 1 \\)).\n\n**Step 2: Verify the conditions.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Prime Factorization by Division Ladder / Factor Tree
    arch4 = {
        'data': [
            (60, "2^2 * 3 * 5", "60 / 2 = 30; 30 / 2 = 15; 15 / 3 = 5; 5 / 5 = 1 -> 2^2 * 3 * 5"),
            (72, "2^3 * 3^2", "72 = 8 * 9 = 2^3 * 3^2"),
            (100, "2^2 * 5^2", "100 = 4 * 25 = 2^2 * 5^2"),
            (120, "2^3 * 3 * 5", "120 = 8 * 15 = 2^3 * 3 * 5"),
            (180, "2^2 * 3^2 * 5", "180 = 4 * 9 * 5 = 2^2 * 3^2 * 5"),
            (84, "2^2 * 3 * 7", "84 = 4 * 21 = 2^2 * 3 * 7"),
            (150, "2 * 3 * 5^2", "150 = 6 * 25 = 2 * 3 * 5^2"),
            (216, "2^3 * 3^3", "216 = 6^3 = 2^3 * 3^3"),
            (360, "2^3 * 3^2 * 5", "360 = 8 * 9 * 5 = 2^3 * 3^2 * 5"),
            (144, "2^4 * 3^2", "144 = 16 * 9 = 2^4 * 3^2")
        ],
        'tmpls': [
            "Express {0} as a product of its prime factors in exponential power form:",
            "Find the prime factorization of {0}:",
            "What is the canonical prime decomposition of {0}?",
            "Using the factor ladder algorithm, decompose {0} into primes:",
            "Determine the prime factorization of: {0}:",
            "Write {0} in the form \\( 2^a \\times 3^b \\times 5^c \\dots \\):",
            "Compute the prime factors of {0} in standard power notation:",
            "Evaluate the prime factor tree for {0}:",
            "Calculate the prime decomposition of {0}:",
            "Factorize {0} completely into prime numbers:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[1].replace('^2', '^3') if '^2' in item[1] else item[1] + " * 7",
                "2 * " + str(item[0] // 2),
                "Prime number (cannot be factored)"
            ],
            f"**Step 1: Divide by smallest prime factors sequentially.**\n{item[2]}.\n\n**Step 2: Collect identical prime factors into powers.**\n\n**Step 3: State the canonical prime factorization.**\nThe prime factorization of {item[0]} is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: The Fundamental Theorem of Arithmetic
    arch5 = {
        'data': [
            ("What does the Fundamental Theorem of Arithmetic state?", "Every composite number can be uniquely expressed as a product of primes, up to the order of the factors", "Unique Factorization Theorem"),
            ("Why is the phrase 'up to the order of factors' included in the Fundamental Theorem of Arithmetic?", "Because 2 * 3 * 5 is considered identical to 5 * 2 * 3 (multiplication is commutative)", "Commutativity of factors"),
            ("Why must the number 1 be excluded from being a prime for the Fundamental Theorem of Arithmetic to hold?", "Because if 1 were prime, prime factorizations would not be unique (e.g. 6 = 2*3 = 1*2*3 = 1*1*2*3... infinitely many representations)", "Preserving uniqueness of prime factorization"),
            ("Who first rigorously proved the Fundamental Theorem of Arithmetic in his Disquisitiones Arithmeticae (1801)?", "Carl Friedrich Gauss", "Proved by Gauss in 1801"),
            ("In which ancient work was the geometric equivalent of the Fundamental Theorem of Arithmetic first developed?", "Euclid's Elements (Book IX, Proposition 14)", "Euclidean origin"),
            ("What are the 'atomic building blocks' of all positive integers under multiplication?", "Prime numbers", "Primes as multiplicative building blocks"),
            ("Can two different positive integers have the exact same canonical prime factorization?", "No, each positive integer has ONE AND ONLY ONE unique prime factorization", "Bijective correspondence"),
            ("How does prime factorization determine the number of factors of an integer N = p^a * q^b * r^c?", "Total factors = (a + 1)(b + 1)(c + 1)", "Divisor count function d(N)"),
            ("How many positive factors does 72 = 2^3 * 3^2 have?", 12, "(3 + 1)(2 + 1) = 4 * 3 = 12 factors"),
            ("How many positive factors does 100 = 2^2 * 5^2 have?", 9, "(2 + 1)(2 + 1) = 3 * 3 = 9 factors")
        ],
        'tmpls': [
            "{0}",
            "In the Fundamental Theorem of Arithmetic: {0}",
            "What is the mathematical significance of: {0}?",
            "Identify the foundational principle: {0}",
            "Which statement correctly formulates: {0}?",
            "Analyze the unique factorization theorem: {0}",
            "Determine the accurate answer: {0}",
            "In Gaussian and Euclidean number theory: {0}",
            "Select the accurate insight: {0}",
            "Regarding prime factor uniqueness: {0}"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [
                f"{item[1] + 3}" if isinstance(item[1], int) else "Factorizations are never unique",
                f"{item[1] - 2}" if isinstance(item[1], int) else "1 is a prime number",
                "6" if isinstance(item[1], int) else "All integers have infinite prime factorizations"
            ],
            f"**Step 1: Understand the Fundamental Theorem of Arithmetic.**\nEvery composite number has a unique prime signature \\( N = p_1^{{a_1}} p_2^{{a_2}} \\dots p_k^{{a_k}} \\).\n\n**Step 2: Detail the concept.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Prime Factorization Algorithm for HCF and LCM
    arch6 = {
        'data': [
            ("A = 2^3 * 3^2 * 5 and B = 2^2 * 3^3 * 7", "HCF = 2^2 * 3^2 = 36", "LCM = 2^3 * 3^3 * 5 * 7 = 7560", "HCF takes lowest powers; LCM takes highest powers"),
            ("A = 2^4 * 3 * 5^2 and B = 2^2 * 3^2 * 5", "HCF = 2^2 * 3 * 5 = 60", "LCM = 2^4 * 3^2 * 5^2 = 3600", "Lowest powers for HCF, highest for LCM"),
            ("A = 2 * 3^3 * 5 and B = 2^3 * 3 * 7", "HCF = 2 * 3 = 6", "LCM = 2^3 * 3^3 * 5 * 7 = 7560", "Intersection vs union of prime powers"),
            ("A = 2^2 * 5^3 and B = 2^3 * 5 * 11", "HCF = 2^2 * 5 = 20", "LCM = 2^3 * 5^3 * 11 = 11000", "HCF = 20"),
            ("A = 3^2 * 7 and B = 2 * 3 * 7^2", "HCF = 3 * 7 = 21", "LCM = 2 * 3^2 * 7^2 = 882", "HCF = 21"),
            ("In prime power notation, how is the HCF (GCD) computed?", "Product of the SMALLEST power of each common prime factor involved in the numbers", "Rule for HCF from prime powers"),
            ("In prime power notation, how is the LCM computed?", "Product of the GREATEST power of each prime factor involved in the numbers", "Rule for LCM from prime powers"),
            ("If two numbers have no common prime factors (coprime), what is their HCF?", 1, "No common primes -> HCF = 1"),
            ("If two numbers are coprime (HCF = 1), what is their LCM?", "Their product a * b", "LCM = a * b when HCF = 1"),
            ("Can this prime power method compute HCF and LCM for three or more numbers simultaneously?", "Yes, by taking minimum powers across all numbers for HCF and maximum powers for LCM", "Generalization to 3+ numbers")
        ],
        'tmpls': [
            "{0}. What is the HCF?",
            "Given the prime factorizations: {0}. Find the HCF:",
            "Calculate the HCF from the prime decompositions: {0}:",
            "What is the greatest common factor for: {0}?",
            "Determine the HCF using prime powers: {0}:",
            "In prime factorization algorithms: {0}:",
            "Evaluate the common factor from prime powers: {0}:",
            "Find the highest common factor for: {0}:",
            "Compute the HCF for the decomposed numbers: {0}:",
            "Apply the prime power HCF rule to: {0}:"
        ],
        'calc': lambda item: (
            item[1].replace("HCF = ", "") if "HCF = " in str(item[1]) else str(item[1]),
            [
                "HCF = 1" if "HCF = 1" not in str(item[1]) else "HCF = 2",
                "Product of all numbers",
                "LCM = " + str(item[2]) if len(item) > 2 else "0"
            ],
            f"**Step 1: Identify all prime factors and their exponents.**\n\n**Step 2: Take the minimum exponent of each common prime factor for HCF.**\n{item[3] if len(item) > 3 else item[2]}.\n\n**Step 3: State the answer.**\nThe HCF is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Divisibility and Prime Algorithms in Cryptography and Computer Science
    arch7 = {
        'data': [
            ("Why are extremely large prime numbers (hundreds of digits long) critical to internet security and online banking?", "Because multiplying two large primes is trivial, but factoring their product back into primes is computationally infeasible (RSA encryption)", "Asymmetric one-way function"),
            ("What is a 'trapdoor function' in cryptography?", "A mathematical operation that is easy to compute in one direction but virtually impossible to invert without secret information (the prime factors)", "Trapdoor function definition"),
            ("Which primality test algorithm is commonly used in practice for 1000-digit numbers instead of the Sieve?", "The Miller-Rabin Primality Test (Probabilistic algorithm)", "Miller-Rabin randomized test"),
            ("In 2002, which three Indian computer scientists from IIT Kanpur shocked the world by discovering the first deterministic polynomial-time primality test (AKS Primality Test)?", "Manindra Agrawal, Neeraj Kayal, and Nitin Saxena (AKS Algorithm)", "Famous AKS breakthrough (Primes is in P)"),
            ("What prestigious international award was bestowed upon Agrawal, Kayal, and Saxena for their discovery that 'PRIMES is in P'?", "The Gödel Prize and Fulkerson Prize", "International recognition of AKS"),
            ("What is the primary difference between a 'primality test' and a 'factorization algorithm'?", "A primality test determines WHETHER a number is prime (yes/no) without finding its factors; factorization actually finds the prime factors", "Decision problem vs search problem"),
            ("Why is prime factorization so much harder than primality testing?", "Testing primality can be done in polynomial time (AKS algorithm), but no polynomial-time classical algorithm is known for prime factorization", "Complexity asymmetry"),
            ("Which theoretical future computer could factor large numbers in polynomial time using Shor's Algorithm?", "A Quantum Computer", "Shor's quantum algorithm (1994)"),
            ("What ensures that modern internet encryption remains secure today?", "The immense computational difficulty of factoring large composite numbers on classical supercomputers", "Security foundation of RSA"),
            ("What is the ultimate message of Chapter 11 'The World of Algorithms' in Ganita Manjari?", "That numbers, divisibility, and primes are not just abstract arithmetic, but the operational engine powering modern global technology and computation", "Philosophical capstone of Chapter 11")
        ],
        'tmpls': [
            "{0}",
            "In modern algorithmic number theory and cryptography: {0}",
            "What is the real-world impact of: {0}?",
            "Identify the historic or technical achievement: {0}",
            "Which concept explains: {0}?",
            "Analyze the cryptographic connection: {0}",
            "Determine the accurate answer: {0}",
            "In computer science and Indian mathematics: {0}",
            "Select the accurate algorithmic fact: {0}",
            "Evaluate the technological relevance: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Primes have no use outside pure mathematics",
                "All large numbers can be factored in 1 second",
                "Internet banking uses addition only"
            ],
            f"**Step 1: Understand the modern technological role of number theoretic algorithms.**\nPrime testing, factorization asymmetry, and modular arithmetic form the bedrock of global cybersecurity.\n\n**Step 2: Detail the historical or computational fact.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_11_3_1()
    q2 = gen_11_3_2()
    print(f"gen_11_3_1: {len(q1)} questions")
    print(f"gen_11_3_2: {len(q2)} questions")
