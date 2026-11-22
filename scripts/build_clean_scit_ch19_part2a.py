# scripts/build_clean_scit_ch19_part2a.py
# Clean generator for MH-9-SCIT Chapter 19 Topic 19.2 (Subtopics 19.2.1 and 19.2.2)
# 2 subtopics x 80 = 160 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 19
CH_NAME = "Class 7 Science Foundation Core"

def gen_19_2_1():
    tc = "MH-9-SCIT-19-19.2.1"
    tname = "Types of motion: oscillatory, periodic, circular & speed calculations"
    archs = [
        # Arch 0: Classification of Motion (Linear, Circular, Oscillatory, Periodic, Random)
        {
            'data': [
                ("motion of a body along a straight line path, such as a vehicle moving on a straight road or a falling stone", "Linear (rectilinear) motion", "Circular motion", "Oscillatory motion", "Random motion"),
                ("motion of a body moving back and forth (to-and-fro) about a fixed central mean position, such as a child on a swing or pendulum", "Oscillatory motion", "Linear motion", "Circular motion", "Rotational motion"),
                ("motion that repeats itself at regular, equal intervals of time, such as the revolution of the Earth around the Sun", "Periodic motion", "Non-periodic motion", "Random motion", "Uniform rectilinear motion"),
                ("motion of a body traversing along the circumference of a curved circular trajectory, such as the tip of a clock's hands", "Circular motion", "Rectilinear motion", "Random Brownian motion", "Linear accelerated motion"),
                ("motion where the direction and speed of an object change continuously and unpredictably without any fixed path, such as a flying butterfly or dust particles", "Random motion", "Periodic motion", "Linear motion", "Circular motion"),
                ("motion of an object around its own internal central axis, such as a spinning top or the Earth rotating on its polar axis", "Rotational motion", "Revolutional motion", "Oscillatory motion", "Linear displacement"),
                ("motion where an object covers equal distances in equal intervals of time along a straight line", "Uniform motion", "Non-uniform motion", "Accelerated periodic motion", "Oscillatory motion"),
                ("motion where an object covers unequal distances in equal intervals of time, or changes direction continuously", "Non-uniform motion", "Uniform motion", "Constant velocity motion", "Static equilibrium"),
                ("the motion of the plucked strings of a musical sitar or guitar vibrating rapidly back and forth", "Oscillatory (vibratory) motion", "Linear motion", "Rotational motion", "Random motion"),
                ("the motion of the needle of a mechanical sewing machine moving up and down continuously at regular intervals", "Periodic oscillatory motion", "Rotational motion only", "Random motion", "Uniform rectilinear motion")
            ],
            'tmpls': [
                "Which kinematic motion classification corresponds to: {0}?",
                "Name the physical motion type defined as: {0}.",
                "In mechanics, which category describes: {0}?",
                "Identify the specific type of motion characterized by: {0}.",
                "Select the appropriate motion classification for: {0}.",
                "Which mechanical description accurately matches: {0}?",
                "Identify the kinematic definition corresponding to: {0}.",
                "Which kinematic state is characterized as: {0}?",
                "Which acoustic mechanical motion matches: {0}?",
                "Select the oscillatory motion example defined by: {0}."
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Motion Characteristic Analysis**\\nThe prompt describes {item[0]}.\\n**Step 2: Trajectory and Timing Pattern**\\nLinear motion follows a line, circular traverses a circle, oscillatory swings to-and-fro, periodic repeats in equal time periods, and random changes unpredictably.\\n**Step 3: Verification**\\nThe correct motion classification is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Speed, Distance, Time Concepts & Units
        {
            'data': [
                ("the physical quantity defined as the total distance covered by an object divided by the time taken to cover that distance", "Speed (\\(\\text{Speed} = \\frac{\\text{Distance}}{\\text{Time}}\\))", "Acceleration", "Momentum", "Mechanical Force"),
                ("the standard International System of Units (SI unit) for measuring speed", "Metre per second (\\(\\text{m/s}\\))", "Kilometre per hour (\\(\\text{km/h}\\))", "Centimetre per minute (\\(\\text{cm/min}\\))", "Metre per second squared (\\(\\text{m/s}^2\\))"),
                ("the multiplication conversion factor used to convert speed from kilometres per hour (\\(\\text{km/h}\\)) to metres per second (\\(\\text{m/s}\\))", "\\(\\frac{5}{18}\\)", "\\(\\frac{18}{5}\\)", "\\(\\frac{1000}{60}\\)", "\\(\\frac{1}{3600}\\)"),
                ("the dashboard instrument installed in automotive vehicles that displays the instantaneous vehicle speed in \\(\\text{km/h}\\)", "Speedometer", "Odometer", "Tachometer", "Galvanometer"),
                ("the dashboard instrument installed in automotive vehicles that records the cumulative total distance traversed in kilometres", "Odometer", "Speedometer", "Anemometer", "Hydrometer"),
                ("the physical quantity obtained by dividing total distance traversed by the total elapsed time for a trip involving varying speeds", "Average speed", "Instantaneous velocity", "Uniform acceleration", "Terminal speed"),
                ("the key physical distinction between speed and velocity in classical mechanics", "Speed is a scalar quantity (magnitude only); velocity is a vector quantity (magnitude and direction)", "Speed has direction while velocity does not", "Speed is measured in \\(\\text{m/s}^2\\) and velocity in \\(\\text{m/s}\\)", "Speed applies only to circular motion"),
                ("an object is said to possess uniform speed if its distance-time graph on Cartesian axes is", "A straight inclined line passing through the origin with a constant slope", "A horizontal line parallel to time axis", "A parabolic curved upward line", "A vertical line parallel to distance axis"),
                ("if an object is stationary at a fixed position, its distance-time graph is represented by", "A horizontal straight line parallel to the time axis", "A straight line sloping upwards", "A vertical line parallel to distance axis", "A downward curving parabola"),
                ("the slope (gradient) of a linear distance-time graph represents which physical quantity", "Speed (or magnitude of velocity)", "Acceleration", "Total distance", "Force exerted")
            ],
            'tmpls': [
                "Which physical property is defined as: {0}?",
                "Identify the SI standard measurement unit for: {0}.",
                "Which mathematical fraction factor is used for: {0}?",
                "Which automotive dashboard instrument corresponds to: {0}?",
                "Name the automotive dashboard meter characterized by: {0}.",
                "Which kinematic quantity represents: {0}?",
                "What is the fundamental physical distinction regarding: {0}?",
                "What geometric graph profile corresponds to: {0}?",
                "What distance-time graphical profile indicates: {0}?",
                "What physical property is quantified by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Physical Definition Identification**\\nThe question highlights {item[0]}.\\n**Step 2: Formula and Unit Relationships**\\nSpeed is scalar distance divided by time (\\(\\text{{m/s}}\\)); slope of distance-time graph yields speed.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Simple Pendulum, Time Period & Oscillations
        {
            'data': [
                ("a mechanical device consisting of a small metallic sphere (bob) suspended from a rigid support by a light, inextensible thread", "Simple pendulum", "Spring balance", "Tuning fork", "Sextant"),
                ("the time required by an oscillating simple pendulum to complete one full to-and-fro cycle (oscillation)", "Time period (\\(T\\))", "Oscillation frequency", "Amplitude", "Wavelength"),
                ("the number of complete oscillations executed by an oscillating body per unit time (one second), measured in Hertz (\\(\\text{Hz}\\))", "Frequency (\\(f = \\frac{1}{T}\\))", "Time period", "Phase angle", "Angular velocity"),
                ("the maximum displacement of the pendulum bob from its central mean resting position to either extreme position", "Amplitude", "Period", "Wavelength", "Node"),
                ("the Italian scientist who discovered that a pendulum of a given fixed length always takes the same time to complete an oscillation (isochronism)", "Galileo Galilei", "Isaac Newton", "Johannes Kepler", "Christiaan Huygens"),
                ("the Dutch scientist who first utilized Galileo's pendulum principles to invent the first high-precision mechanical pendulum clock in 1656", "Christiaan Huygens", "Galileo Galilei", "Robert Hooke", "Blaise Pascal"),
                ("how the time period of a simple pendulum depends mathematically on its length \\(L\\) and mass of the bob \\(m\\)", "Directly proportional to \\(\\sqrt{L}\\) and completely independent of the bob's mass \\(m\\)", "Directly proportional to the bob's mass \\(m\\)", "Inversely proportional to \\(L^2\\)", "Completely independent of length \\(L\\)"),
                ("if the length of a simple pendulum is quadrupled (\\(4\\times L\\)), its time period changes by a factor of", "Doubles (\\(2\\times T\\))", "Halves (\\(0.5\\times T\\))", "Quadruples (\\(4\\times T\\))", "Remains identical"),
                ("a pendulum whose time period is exactly 2 seconds (taking 1 second for each single swing in one direction) is called", "Seconds pendulum (approximate length \\(1\\text{ metre}\\))", "Millisecond pendulum", "Torsion pendulum", "Coupled oscillator"),
                ("the resting equilibrium point of a simple pendulum when it is stationary without swinging is called", "Mean position", "Extreme position", "Node point", "Apex")
            ],
            'tmpls': [
                "Which physical apparatus is defined as: {0}?",
                "Which oscillatory parameter is defined by: {0}?",
                "Identify the physical quantity measured in Hertz defined as: {0}.",
                "Which oscillatory geometric distance corresponds to: {0}?",
                "Name the historical physicist celebrated for: {0}.",
                "Identify the horological inventor recognized for: {0}.",
                "What is the physical mathematical dependence described by: {0}?",
                "Determine the proportional variation when: {0}.",
                "Which specific horological pendulum is defined as: {0}?",
                "Which equilibrium point corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Pendulum Mechanics Context**\\nThe query examines {item[0]}.\\n**Step 2: Mathematical and Physical Laws**\\nThe period \\(T = 2\\pi\\sqrt{{L/g}}\\) depends solely on length \\(L\\) and local gravity \\(g\\), regardless of bob mass.\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Natural Clocks, Historical Timekeepers & Sundials
        {
            'data': [
                ("an ancient timekeeping device that indicates the solar time of day by the shadow cast by an upright triangular gnomon onto a graduated dial", "Sundial", "Water clock (Clepsydra)", "Hourglass (sand clock)", "Astrolabe"),
                ("the ancient vessel designed to measure time by the regulated steady outflow or inflow of water through a calibrated orifice", "Water clock (Clepsydra)", "Sundial", "Telescope", "Barometer"),
                ("the historic astronomical observatory in New Delhi and Jaipur housing the massive stone sundial Samrat Yantra built by Maharaja Jai Singh II", "Jantar Mantar", "Qutub Minar", "Gol Gumbaz", "Brihadisvara"),
                ("the natural periodic celestial phenomenon that defined the traditional fundamental unit of one solar day", "One complete rotation of the Earth on its axis relative to the Sun", "One revolution of Moon around Earth", "One revolution of Earth around Sun", "One precession of equinoxes"),
                ("the natural periodic celestial phenomenon that defines one lunar month", "The time interval between one new moon (Amavasya) and the next new moon (~29.5 days)", "One complete orbit of Earth around Sun", "One solar rotation of Sun", "One equinox cycle"),
                ("the natural periodic celestial phenomenon that defines one solar year", "The time taken by the Earth to complete one full revolution around the Sun (~365.25 days)", "Twelve lunar rotations", "One rotation of Milky Way galaxy", "One axial nutation cycle"),
                ("the modern ultra-precise timekeeping standard that uses the invariant microwave frequency vibrations of cesium-133 atoms", "Atomic clock (Cesium fountain clock)", "Quartz crystal clock", "Mechanical pendulum clock", "Chronometer"),
                ("the electronic crystal commonly used in wristwatches and computers that vibrates at a precise piezoelectric frequency (32,768 Hz)", "Quartz crystal (Silicon dioxide, \\(SiO_2\\))", "Diamond crystal", "Calcite prism", "Tourmaline slice"),
                ("the major limitation of a solar sundial in everyday time measurement", "It cannot function during cloudy weather, rainfall, or after sunset at night", "It runs too fast in summer", "Its shadow reverses direction every hour", "It cannot be placed outdoors"),
                ("the primary time standard institution responsible for maintaining Indian Standard Time (IST) in New Delhi", "National Physical Laboratory (CSIR-NPL, New Delhi)", "ISRO Bengaluru", "Bhabha Atomic Research Centre", "Survey of India")
            ],
            'tmpls': [
                "Which historical timekeeping instrument is defined as: {0}?",
                "Name the ancient hydrostatic timekeeper described as: {0}.",
                "Which heritage astronomical monument represents: {0}?",
                "Which astronomical rotation event corresponds to: {0}?",
                "What celestial interval characterizes: {0}?",
                "Which orbital period defines: {0}?",
                "Which modern metrological standard represents: {0}?",
                "Which piezoelectric component corresponds to: {0}?",
                "What physical limitation applies to: {0}?",
                "Which national scientific institution oversees: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Horological / Metrological Concept**\\nThe statement details {item[0]}.\\n**Step 2: Evolution of Time Standards**\\nTime measurement transitioned from natural periodic celestial motions (solar day, lunar month, solar year) to sundials, pendulum clocks, quartz oscillators, and cesium atomic clocks.\\n**Step 3: Verification**\\nThe correct answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Speed Calculation Word Problems (Single Journey & Conversions)
        {
            'data': [
                ("A high-speed train travels a distance of \\(360\\text{ km}\\) in \\(4\\text{ hours}\\). Calculate the average speed of the train in \\(\\text{km/h}\\).", "\\(90\\text{ km/h}\\)", "\\(80\\text{ km/h}\\)", "\\(100\\text{ km/h}\\)", "\\(120\\text{ km/h}\\)"),
                ("Convert a speed of \\(72\\text{ km/h}\\) into metres per second (\\(\\text{m/s}\\)) using the conversion factor \\(\\frac{5}{18}\\).", "\\(20\\text{ m/s}\\)", "\\(25\\text{ m/s}\\)", "\\(15\\text{ m/s}\\)", "\\(30\\text{ m/s}\\)"),
                ("Convert a speed of \\(25\\text{ m/s}\\) into kilometres per hour (\\(\\text{km/h}\\)) using the conversion factor \\(\\frac{18}{5}\\).", "\\(90\\text{ km/h}\\)", "\\(75\\text{ km/h}\\)", "\\(100\\text{ km/h}\\)", "\\(80\\text{ km/h}\\)"),
                ("A cheetah sprints at a uniform speed of \\(30\\text{ m/s}\\) for \\(12\\text{ seconds}\\). What total distance does the cheetah cover?", "\\(360\\text{ metres}\\)", "\\(250\\text{ metres}\\)", "\\(300\\text{ metres}\\)", "\\(420\\text{ metres}\\)"),
                ("An airplane cruises at a speed of \\(900\\text{ km/h}\\). How much time does it require to fly a nonstop distance of \\(4500\\text{ km}\\)?", "\\(5.0\\text{ hours}\\)", "\\(4.0\\text{ hours}\\)", "\\(6.0\\text{ hours}\\)", "\\(3.5\\text{ hours}\\)"),
                ("A school bus travels at \\(36\\text{ km/h}\\). How many metres does it travel in \\(1\\text{ second}\\)?", "\\(10\\text{ metres}\\)", "\\(36\\text{ metres}\\)", "\\(5\\text{ metres}\\)", "\\(20\\text{ metres}\\)"),
                ("An athlete completes a \\(400\\text{ metre}\\) circular track sprint in \\(50\\text{ seconds}\\). Calculate the runner's average speed in \\(\\text{m/s}\\).", "\\(8.0\\text{ m/s}\\)", "\\(10.0\\text{ m/s}\\)", "\\(6.5\\text{ m/s}\\)", "\\(7.2\\text{ m/s}\\)"),
                ("A sound wave travels at \\(340\\text{ m/s}\\) through air. If thunder is heard \\(5\\text{ seconds}\\) after seeing a flash of lightning, calculate the distance to the lightning strike.", "\\(1700\\text{ metres } (1.7\\text{ km})\\)", "\\(1500\\text{ metres}\\)", "\\(680\\text{ metres}\\)", "\\(2000\\text{ metres}\\)"),
                ("Light travels through vacuum at \\(3 \\times 10^8\\text{ m/s}\\). If sunlight takes \\(500\\text{ seconds}\\) (~8 min 20 s) to reach Earth, calculate the distance between Sun and Earth.", "\\(1.5 \\times 10^8\\text{ km } (1.5 \\times 10^{11}\\text{ m})\\)", "\\(3.0 \\times 10^8\\text{ km}\\)", "\\(1.0 \\times 10^7\\text{ km}\\)", "\\(4.5 \\times 10^9\\text{ km}\\)"),
                ("A vehicle odometer reads \\(12,450\\text{ km}\\) at 8:00 AM and \\(12,690\\text{ km}\\) at 11:00 AM. What is the average speed of the vehicle during this 3-hour journey?", "\\(80\\text{ km/h}\\)", "\\(70\\text{ km/h}\\)", "\\(85\\text{ km/h}\\)", "\\(60\\text{ km/h}\\)")
            ],
            'tmpls': [
                "Calculate the average speed in the kinematics problem: {0}",
                "Perform the velocity conversion: {0}",
                "Evaluate the metric conversion calculation: {0}",
                "Determine the distance traversed: {0}",
                "Calculate the flight time duration: {0}",
                "Compute the distance covered per second: {0}",
                "Calculate the runner's average speed: {0}",
                "Determine the acoustic distance to the lightning strike: {0}",
                "Calculate the astronomical distance to the Sun: {0}",
                "Determine the vehicle's trip average speed: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nIdentify distance \\(d\\) and time \\(t\\) from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(\\text{{Speed}} = \\frac{{d}}{{t}}\\) or \\(\\text{{Distance}} = \\text{{Speed}} \\times t\\) with unit conversion factors.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Average Speed & Two-Leg Journey Calculations
        {
            'data': [
                ("A car travels the first \\(100\\text{ km}\\) at \\(50\\text{ km/h}\\) and the next \\(100\\text{ km}\\) at \\(100\\text{ km/h}\\). Calculate the average speed for the entire \\(200\\text{ km}\\) journey.", "\\(66.67\\text{ km/h}\\)", "\\(75.0\\text{ km/h}\\)", "\\(60.0\\text{ km/h}\\)", "\\(80.0\\text{ km/h}\\)"),
                ("A cyclist rides for \\(2\\text{ hours}\\) at \\(15\\text{ km/h}\\) and then for \\(3\\text{ hours}\\) at \\(20\\text{ km/h}\\). What is the average speed of the cyclist for the entire 5-hour journey?", "\\(18.0\\text{ km/h}\\)", "\\(17.5\\text{ km/h}\\)", "\\(16.0\\text{ km/h}\\)", "\\(19.0\\text{ km/h}\\)"),
                ("A motorist drives to an office at \\(40\\text{ km/h}\\) and returns home along the exact same route at \\(60\\text{ km/h}\\). Using the harmonic mean formula \\(v_{\\text{avg}} = \\frac{2v_1v_2}{v_1+v_2}\\), calculate the overall average speed.", "\\(48\\text{ km/h}\\)", "\\(50\\text{ km/h}\\)", "\\(52\\text{ km/h}\\)", "\\(45\\text{ km/h}\\)"),
                ("A train travels \\(60\\text{ km}\\) in \\(1.5\\text{ hours}\\) and stops at a station for \\(0.5\\text{ hours}\\), then travels another \\(80\\text{ km}\\) in \\(2\\text{ hours}\\). What is the average speed of the train including the stop?", "\\(35.0\\text{ km/h}\\)", "\\(40.0\\text{ km/h}\\)", "\\(30.0\\text{ km/h}\\)", "\\(45.0\\text{ km/h}\\)"),
                ("A boy walks \\(1200\\text{ metres}\\) from home to school in \\(20\\text{ minutes}\\). What is his average walking speed in \\(\\text{m/s}\\)?", "\\(1.0\\text{ m/s}\\)", "\\(2.0\\text{ m/s}\\)", "\\(0.6\\text{ m/s}\\)", "\\(1.5\\text{ m/s}\\)"),
                ("A delivery van covers a distance of \\(30\\text{ km}\\) at a speed of \\(30\\text{ km/h}\\) and the next \\(60\\text{ km}\\) at a speed of \\(60\\text{ km/h}\\). What is the overall average speed?", "\\(45.0\\text{ km/h}\\)", "\\(40.0\\text{ km/h}\\)", "\\(50.0\\text{ km/h}\\)", "\\(35.0\\text{ km/h}\\)"),
                ("An express bus travels \\(180\\text{ km}\\) in \\(3\\text{ hours}\\) and \\(220\\text{ km}\\) in the subsequent \\(4\\text{ hours}\\). Calculate the average speed over the total 7 hours.", "\\(57.14\\text{ km/h}\\)", "\\(60.0\\text{ km/h}\\)", "\\(55.0\\text{ km/h}\\)", "\\(52.5\\text{ km/h}\\)"),
                ("A runner runs at \\(6\\text{ m/s}\\) for \\(200\\text{ seconds}\\) and then walks at \\(2\\text{ m/s}\\) for \\(300\\text{ seconds}\\). What is the runner's average speed over the \\(500\\text{ seconds}\\)?", "\\(3.6\\text{ m/s}\\)", "\\(4.0\\text{ m/s}\\)", "\\(3.2\\text{ m/s}\\)", "\\(4.5\\text{ m/s}\\)"),
                ("A boat travels downstream \\(40\\text{ km}\\) in \\(2\\text{ hours}\\) and upstream \\(40\\text{ km}\\) in \\(4\\text{ hours}\\). What is the boat's round-trip average speed?", "\\(13.33\\text{ km/h}\\)", "\\(15.0\\text{ km/h}\\)", "\\(10.0\\text{ km/h}\\)", "\\(12.5\\text{ km/h}\\)"),
                ("Why is average speed for equal-distance segments calculated via harmonic mean rather than the simple arithmetic mean of the speeds?", "Because more time is spent travelling at the lower speed, skewing total elapsed time", "Because distance changes with speed", "Because speed is a vector quantity", "Because acceleration is non-zero")
            ],
            'tmpls': [
                "Calculate the composite average speed: {0}",
                "Determine the cyclist's trip average speed: {0}",
                "Evaluate the round-trip harmonic average speed: {0}",
                "Compute the average speed including transit halt: {0}",
                "Calculate the pedestrian velocity in standard units: {0}",
                "Evaluate the multi-segment delivery van speed: {0}",
                "Determine the express transit average speed: {0}",
                "Compute the runner's composite average speed: {0}",
                "Calculate the round-trip aquatic average speed: {0}",
                "What fundamental physics principle explains: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula for Multi-Leg Journey**\\nAverage speed \\(v_{{\\text{{avg}}}} = \\frac{{\\text{{Total Distance}}}}{{\\text{{Total Time taken}}}}\\).\\n**Step 2: Stepwise Calculation**\\nCalculate individual times \\(t_1, t_2\\), add to get total time, and divide total distance by total time.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Distance-Time Graph Interpretation & Slope Analysis
        {
            'data': [
                ("In a distance-time graph, if the plot is a straight line passing through the origin sloping upward at 45 degrees, the motion of the body is", "Uniform motion with constant speed", "Uniformly accelerated motion", "Body at complete rest", "Non-uniform motion with decreasing speed"),
                ("In a distance-time graph, if the line is completely horizontal and parallel to the time axis, what does it indicate about the state of the object?", "The object is at rest (speed is zero, position is unchanged)", "The object is moving with infinite speed", "The object is moving with uniform acceleration", "The object has circular motion"),
                ("On a distance-time graph, object A has a slope of \\(2\\) and object B has a slope of \\(5\\). Which object is moving faster?", "Object B (greater slope represents higher speed)", "Object A", "Both move at the exact same speed", "Cannot be determined without mass"),
                ("If a distance-time graph curves upward like a parabola (slope increases with time), what type of motion does it represent?", "Accelerated motion (speed is increasing continuously)", "Retarded motion (speed is decreasing)", "Uniform speed", "Object at rest"),
                ("If a distance-time graph curves downward becoming flatter with time (slope decreases with time), what type of motion does it represent?", "Decelerated (retarded) motion (speed is decreasing)", "Uniform motion", "Accelerated motion", "Periodic oscillation"),
                ("Calculate the speed of an object whose distance-time graph shows a distance change of \\(150\\text{ metres}\\) over a time interval of \\(10\\text{ seconds}\\).", "\\(15\\text{ m/s}\\)", "\\(1500\\text{ m/s}\\)", "\\(10\\text{ m/s}\\)", "\\(25\\text{ m/s}\\)"),
                ("In a distance-time graph, a vertical straight line perpendicular to the time axis is physically impossible because", "An object cannot be present at multiple distances at the same instantaneous moment of time (infinite speed)", "Time cannot move backward", "Distance cannot be positive", "Acceleration must be constant"),
                ("In a distance-time graph, can the plotted curve ever have a negative slope (going downward toward the time axis)?", "No, because total distance traversed cannot decrease with time", "Yes, whenever an object slows down", "Yes, when an object travels south", "Yes, during circular motion"),
                ("On a Cartesian distance-time graph, the independent variable plotted on the horizontal X-axis is always", "Time (\\(t\\))", "Distance (\\(d\\))", "Speed (\\(v\\))", "Force (\\(F\\))"),
                ("On a Cartesian distance-time graph, the dependent variable plotted on the vertical Y-axis is", "Distance (\\(d\\))", "Time (\\(t\\))", "Acceleration (\\(a\\))", "Velocity squared")
            ],
            'tmpls': [
                "Interpret the kinematics from the distance-time graph: {0}",
                "What physical state is revealed by the graph: {0}?",
                "Compare the slopes on the distance-time plot: {0}",
                "Identify the acceleration behavior from the curve: {0}",
                "Determine the deceleration dynamic from the plot: {0}",
                "Calculate the gradient velocity from the graph data: {0}",
                "Why is the following graphical scenario physically impossible: {0}?",
                "Explain the kinematic constraint regarding distance-time graphs: {0}",
                "Identify the standard Cartesian coordinate axis convention: {0}",
                "Which physical variable is plotted on the vertical axis: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Graph Axis and Slope Interpretation**\\nThe prompt examines {item[0]}.\\n**Step 2: Mathematical Gradient Analysis**\\nSlope of distance-time graph \\(\\frac{{\\Delta d}}{{\\Delta t}} = \\text{{Speed}}\\). Horizontal line has slope 0 (rest); steeper slope indicates higher speed.\\n**Step 3: Verification**\\nThe correct interpretation is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Pendulum Periods & Oscillations
        {
            'data': [
                ("A simple pendulum completes \\(20\\text{ oscillations}\\) in \\(40\\text{ seconds}\\). Calculate the time period \\(T\\) of the pendulum.", "\\(2.0\\text{ seconds}\\)", "\\(0.5\\text{ seconds}\\)", "\\(4.0\\text{ seconds}\\)", "\\(1.0\\text{ second}\\)"),
                ("A simple pendulum completes \\(20\\text{ oscillations}\\) in \\(40\\text{ seconds}\\). Calculate the frequency of oscillation in Hertz (\\(\\text{Hz}\\)).", "\\(0.5\\text{ Hz}\\)", "\\(2.0\\text{ Hz}\\)", "\\(1.0\\text{ Hz}\\)", "\\(4.0\\text{ Hz}\\)"),
                ("If a pendulum has a time period of \\(0.4\\text{ seconds}\\), how many complete oscillations will it execute in \\(1\\text{ minute } (60\\text{ seconds})\\)?", "\\(150\\text{ oscillations}\\)", "\\(120\\text{ oscillations}\\)", "\\(240\\text{ oscillations}\\)", "\\(60\\text{ oscillations}\\)"),
                ("A student measures the time taken for \\(50\\text{ oscillations}\\) of a pendulum to be \\(125\\text{ seconds}\\). What is the precise time period?", "\\(2.5\\text{ seconds}\\)", "\\(0.4\\text{ seconds}\\)", "\\(2.0\\text{ seconds}\\)", "\\(1.25\\text{ seconds}\\)"),
                ("A seconds pendulum has a time period of \\(2.0\\text{ seconds}\\). How many complete swings (oscillations) does it make in \\(1\\text{ hour } (3600\\text{ seconds})\\)?", "\\(1800\\text{ oscillations}\\)", "\\(3600\\text{ oscillations}\\)", "\\(900\\text{ oscillations}\\)", "\\(7200\\text{ oscillations}\\)"),
                ("If the length of a simple pendulum is increased from \\(1\\text{ m}\\) to \\(9\\text{ m}\\), its time period will increase by a factor of", "\\(3\\text{ times } (\\sqrt{9} = 3)\\)", "\\(9\\text{ times}\\)", "\\(4.5\\text{ times}\\)", "\\(2\\text{ times}\\)"),
                ("A pendulum on Earth has a time period of \\(2\\text{ seconds}\\). If taken to the Moon where gravity is \\(g/6\\), how does the time period change?", "Increases by \\(\\sqrt{6} \\approx 2.45\\) times (longer time period, slower swings)", "Decreases by 6 times", "Remains exactly 2 seconds", "Decreases to 0.33 seconds"),
                ("If the mass of a pendulum's metallic bob is doubled from \\(50\\text{ g}\\) to \\(100\\text{ g}\\) without changing thread length, its time period will", "Remain completely unchanged", "Double", "Halve", "Increase by \\(\\sqrt{2}\\)"),
                ("An oscillator completes \\(120\\text{ vibrations}\\) in \\(3\\text{ seconds}\\). What is the frequency of vibration in \\(\\text{Hz}\\)?", "\\(40\\text{ Hz}\\)", "\\(360\\text{ Hz}\\)", "\\(0.025\\text{ Hz}\\)", "\\(120\\text{ Hz}\\)"),
                ("A pendulum clock runs slow in hot summer seasons because", "Thermal expansion increases the length of the pendulum rod, increasing time period \\(T\\)", "The bob loses mass due to heat", "Air density increases resistance", "Gravity weakens in summer")
            ],
            'tmpls': [
                "Calculate the pendulum time period: {0}",
                "Determine the oscillation frequency: {0}",
                "Compute the total oscillations executed: {0}",
                "Calculate the experimental time period: {0}",
                "Evaluate the hourly oscillation count: {0}",
                "Determine the period factor change: {0}",
                "Evaluate the lunar gravitational effect on period: {0}",
                "Predict the effect of bob mass variation on period: {0}",
                "Compute the acoustic vibration frequency: {0}",
                "What thermal physical mechanism explains: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nTime period \\(T = \\frac{{\\text{{Total time}}}}{{\\text{{Number of oscillations}}}}\\) and frequency \\(f = \\frac{{1}}{{T}}\\).\\n**Step 2: Arithmetic Evaluation**\\nPerform the division or apply \\(T \\propto \\sqrt{{L/g}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_19_2_2():
    tc = "MH-9-SCIT-19-19.2.2"
    tname = "Force, work done & mechanical advantage of simple machines"
    archs = [
        # Arch 0: Force Definition, Types & Friction
        {
            'data': [
                ("a push or pull upon an object resulting from its interaction with another object that can change its speed, direction, or shape", "Force", "Work", "Energy", "Power"),
                ("the standard SI unit of force in the metric system", "Newton (\\(\\text{N}\\))", "Joule (\\(\\text{J}\\))", "Watt (\\(\\text{W}\\))", "Pascal (\\(\\text{Pa}\\))"),
                ("forces that require direct physical contact between interacting bodies, such as muscular force and frictional force", "Contact forces", "Non-contact forces", "Gravitational forces", "Magnetic forces"),
                ("forces that act at a distance without any physical contact, such as gravitational force, electrostatic force, and magnetic force", "Non-contact (field) forces", "Contact forces", "Mechanical forces", "Tensional forces"),
                ("the force exerted by the contact of two surfaces that always opposes the relative motion or tendency of motion between them", "Frictional force", "Gravitational force", "Centripetal force", "Buoyant force"),
                ("the correct ascending order of the three types of friction between two given solid surfaces", "Rolling friction < Sliding friction < Static friction", "Static friction < Sliding friction < Rolling friction", "Sliding friction < Rolling friction < Static friction", "Rolling friction < Static friction < Sliding friction"),
                ("the common engineering method of reducing sliding friction in machine bearings by using spherical steel balls", "Using ball bearings to convert sliding friction into much lower rolling friction", "Increasing machine speed", "Adding abrasive sand", "Roughening surface contact"),
                ("the streamlined body shape of birds, fish, and airplanes is an adaptation designed to", "Minimize fluid friction (drag) caused by air or water resistance", "Increase surface area for lift", "Maximize gravitational pull", "Increase friction for stopping"),
                ("the non-contact force that holds planets in their orbits around the Sun and pulls dropped objects toward Earth's surface", "Gravitational force", "Electrostatic force", "Nuclear strong force", "Atmospheric pressure"),
                ("the attractive or repulsive non-contact force acting between electric charges governed by Coulomb's law", "Electrostatic force", "Gravitational force", "Magnetic force", "Frictional force")
            ],
            'tmpls': [
                "Which fundamental physical concept is defined as: {0}?",
                "Identify the SI standard unit for: {0}.",
                "Which category of physical forces represents: {0}?",
                "Which category of action-at-a-distance forces corresponds to: {0}?",
                "Which resistive contact force is defined by: {0}?",
                "What is the correct physical hierarchy regarding: {0}?",
                "Which mechanical friction-reduction strategy describes: {0}?",
                "What aerodynamic purpose is achieved by: {0}?",
                "Which universal non-contact force corresponds to: {0}?",
                "Which electrostatic phenomenon represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Force Concept Identification**\\nThe prompt examines {item[0]}.\\n**Step 2: Force Mechanics and Friction**\\nForces are classified into contact and non-contact; friction opposes relative motion and static > sliding > rolling friction.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Work Done: Formula, Units & Zero Work Conditions
        {
            'data': [
                ("the product of the magnitude of applied force and the displacement of the object in the direction of the force", "Work done (\\(W = F \\times s\\))", "Power", "Momentum", "Pressure"),
                ("the standard SI unit of work and energy, defined as the work done when a force of 1 Newton displaces a body by 1 metre", "Joule (\\(\\text{J} = \\text{N}\\cdot\\text{m}\\))", "Watt", "Newton", "Erg"),
                ("the CGS unit of work, where \\(1\\text{ Joule} = 10^7\\text{ ergs}\\)", "Erg (\\(\\text{dyne}\\cdot\\text{cm}\\))", "Dyne", "Calorie", "Newton"),
                ("work done is considered physically zero when which condition occurs despite a large force being applied", "Displacement of the body is zero (\\(s = 0\\)), such as pushing a rigid immovable wall", "Force is doubled", "Object moves at high velocity", "Force acts along displacement"),
                ("work done by gravity on a satellite in a circular orbit around the Earth is zero because", "The gravitational force is perpendicular (\\(90^\\circ\\)) to the instantaneous displacement (\\(\\cos 90^\\circ = 0\\))", "There is no gravity in space", "The satellite has zero mass", "The satellite moves at speed of light"),
                ("the work done by a porter standing stationary on a railway platform holding a heavy \\(50\\text{ kg}\\) suitcase on his head", "Zero (since displacement \\(s = 0\\))", "\\(500\\text{ Joules}\\)", "\\(50\\text{ Joules}\\)", "\\(980\\text{ Joules}\\)"),
                ("work done is positive when the angle \\(\\theta\\) between applied force and displacement is", "Acute (\\(0^\\circ \\le \\theta < 90^\\circ\\)), where force has a component in the direction of motion", "Obtuse (\\(90^\\circ < \\theta \\le 180^\\circ\\))", "Exactly \\(90^\\circ\\)", "Zero only"),
                ("work done by the force of friction on a moving skidding car is negative because", "Frictional force acts in the exact opposite direction to the displacement (\\(\\theta = 180^\\circ\\), \\(\\cos 180^\\circ = -1\\))", "Friction increases kinetic energy", "Friction is perpendicular to displacement", "Friction produces sound"),
                ("the physical quantity defined as the rate of doing work, or work done per unit time", "Power (\\(P = \\frac{W}{t}\\), SI unit Watt)", "Energy", "Force", "Momentum"),
                ("the commercial unit of electrical energy equivalent to \\(1\\text{ kilowatt-hour (kWh)}\\)", "\\(3.6 \\times 10^6\\text{ Joules } (3.6\\text{ MJ})\\)", "\\(1000\\text{ Joules}\\)", "\\(3600\\text{ Joules}\\)", "\\(1.0 \\times 10^5\\text{ Joules}\\)")
            ],
            'tmpls': [
                "Which physical quantity in mechanics is defined as: {0}?",
                "Identify the SI unit defined by: {0}.",
                "Which CGS unit corresponds to: {0}?",
                "In which physical scenario is: {0}?",
                "Why is orbital gravitational work zero: {0}?",
                "What is the mechanical work done in: {0}?",
                "Under what angular condition is: {0}?",
                "Why is frictional work characterized as: {0}?",
                "Which rate quantity is defined as: {0}?",
                "What is the standard energy equivalence for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Work Done Mechanics Context**\\nThe statement details {item[0]}.\\n**Step 2: Mathematical Formula Evaluation**\\n\\(W = F \\cdot s \\cdot \\cos\\theta\\). If \\(s=0\\) or \\(\\theta=90^\\circ\\), \\(W=0\\). If \\(\\theta=180^\\circ\\), work is negative.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Simple Machines: Types, Classes of Levers & Principles
        {
            'data': [
                ("a mechanical device that enables work to be done more easily and conveniently by multiplying force or changing direction of applied effort", "Simple machine", "Perpetual motion engine", "Hydraulic generator", "Thermal conductor"),
                ("the ratio of the load overcome by a machine to the effort applied to overcome that load", "Mechanical Advantage (\\(\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}}\\))", "Velocity Ratio", "Machine Efficiency", "Output Power"),
                ("the ratio of the distance moved by the effort to the distance moved by the load in the same time", "Velocity Ratio (\\(\\text{VR} = \\frac{d_E}{d_L}\\))", "Mechanical Advantage", "Friction factor", "Efficiency"),
                ("the ratio of useful output work done by a machine to the input work supplied, expressed as a percentage", "Efficiency (\\(\\eta = \\frac{\\text{Output Work}}{\\text{Input Work}} \\times 100\\% = \\frac{\\text{MA}}{\\text{VR}} \\times 100\\%\\))", "Mechanical Advantage", "Velocity Ratio", "Leverage"),
                ("a class of lever where the fulcrum (pivot) is situated between the applied effort and the load (e.g., scissors, seesaw, crowbar)", "Class 1 lever (First-class lever)", "Class 2 lever", "Class 3 lever", "Compound pulley"),
                ("a class of lever where the load is situated between the fulcrum and the applied effort, giving \\(\\text{MA} > 1\\) (e.g., wheelbarrow, nutcracker, bottle opener)", "Class 2 lever (Second-class lever)", "Class 1 lever", "Class 3 lever", "Inclined plane"),
                ("a class of lever where the effort is applied between the fulcrum and the load, acting as a speed multiplier with \\(\\text{MA} < 1\\) (e.g., tweezers, human forearm, tongs)", "Class 3 lever (Third-class lever)", "Class 1 lever", "Class 2 lever", "Wedge"),
                ("a simple machine consisting of a flat sloping surface connecting a lower level to a higher level, used to raise heavy loads with smaller effort", "Inclined plane", "Lever", "Pulley", "Screw"),
                ("a simple machine that can be regarded as an inclined plane wound spirally around a central cylinder or rod", "Screw", "Wedge", "Wheel and axle", "Class 2 lever"),
                ("a simple machine consisting of two inclined planes placed back to back used for splitting or cutting materials, such as an axe or knife blade", "Wedge", "Screw", "Pulley", "First-class lever")
            ],
            'tmpls': [
                "Which mechanical device is defined as: {0}?",
                "Name the mechanical ratio defined by: {0}.",
                "Which kinematic ratio is defined as: {0}?",
                "Which machine performance percentage is defined as: {0}?",
                "Which class of lever corresponds to: {0}?",
                "Which class of lever is characterized by: {0}?",
                "Identify the lever category defined as: {0}.",
                "Which sloping simple machine matches: {0}?",
                "Which helical simple machine corresponds to: {0}?",
                "Which dual-inclined cutting tool represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Simple Machine Identification**\\nThe question targets {item[0]}.\\n**Step 2: Lever and Machine Classification**\\nLevers are classified by relative positions of Fulcrum (Class 1: F in middle), Load (Class 2: L in middle), and Effort (Class 3: E in middle).\\n**Step 3: Verification**\\nThe matching machine concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Pulleys & Wheel and Axle Systems
        {
            'data': [
                ("a grooved wheel turning about an axle passing through its center that changes the direction of applied effort", "Fixed pulley", "Movable pulley", "Block and tackle system", "Wheel and axle"),
                ("the mechanical advantage (MA) and velocity ratio (VR) of an ideal single fixed pulley (neglecting friction and rope weight)", "\\(\\text{MA} = 1\\) and \\(\\text{VR} = 1\\) (serves solely to change direction of effort conveniently)", "\\(\\text{MA} = 2\\) and \\(\\text{VR} = 2\\)", "\\(\\text{MA} = 0.5\\) and \\(\\text{VR} = 1\\)", "\\(\\text{MA} = 4\\) and \\(\\text{VR} = 1\\)"),
                ("a pulley whose axle moves along with the load, doubling the applied effort to give an ideal mechanical advantage of 2", "Single movable pulley", "Fixed pulley", "Inclined plane", "Screw jack"),
                ("a combination system containing multiple fixed and movable pulleys where mechanical advantage equals the total number of supporting rope strands \\(n\\)", "Block and tackle pulley system", "Single fixed pulley", "Wedge", "Wheel and axle"),
                ("a simple machine consisting of two rigidly attached concentric cylinders of different radii turning together about a common axis (e.g., steering wheel, doorknob, screwdriver)", "Wheel and axle", "Single fixed pulley", "Inclined plane", "Class 3 lever"),
                ("the mechanical advantage of a wheel and axle system where effort is applied on the outer wheel of radius \\(R\\) and load is lifted by the axle of radius \\(r\\)", "\\(\\text{MA} = \\frac{R}{r}\\) (greater than 1)", "\\(\\text{MA} = \\frac{r}{R}\\)", "\\(\\text{MA} = R \\times r\\)", "\\(\\text{MA} = 1\\) always"),
                ("why the efficiency of any practical, real-world machine is always strictly less than 100% (\\(\\eta < 100\\%\\))", "Due to energy lost overcoming friction between moving parts and the non-zero weight of machine components", "Because energy cannot be conserved", "Because mechanical advantage cannot exceed 1", "Due to atmospheric air pressure"),
                ("in a real machine where friction is present, the relationship between Mechanical Advantage (MA) and Velocity Ratio (VR) is always", "\\(\\text{MA} < \\text{VR}\\) (because \\(\\eta = \\frac{\\text{MA}}{\\text{VR}} < 1\\))", "\\(\\text{MA} > \\text{VR}\\)", "\\(\\text{MA} = \\text{VR}\\)", "\\(\\text{MA} = 0\\)"),
                ("the velocity ratio of a machine depends strictly on", "The geometry and dimensions of the machine components (independent of friction)", "The amount of friction present", "The load lifted", "The speed of the operator"),
                ("a machine whose efficiency is 100% with zero frictional loss and zero weight in moving parts is called", "An ideal (perfect) machine", "A real practical machine", "A perpetual motion machine", "A hydraulic press")
            ],
            'tmpls': [
                "Which pulley arrangement is defined as: {0}?",
                "What are the mechanical metrics for: {0}?",
                "Which mobile pulley system corresponds to: {0}?",
                "Which multi-strand pulley system represents: {0}?",
                "Which concentric mechanical system is defined by: {0}?",
                "What is the mathematical mechanical advantage for: {0}?",
                "What physical limitation explains why: {0}?",
                "What fundamental inequality holds for: {0}?",
                "What physical factor dictates: {0}?",
                "What theoretical concept represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Machine / Pulley Dynamics**\\nThe statement examines {item[0]}.\\n**Step 2: Physics of Machine Systems**\\nIn ideal machines \\(\\text{{MA}} = \\text{{VR}}\\); in real machines friction reduces MA such that \\(\\text{{MA}} < \\text{{VR}}\\) and efficiency \\(\\eta < 100\\%\\).\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Mechanical Advantage & Lever Calculations
        {
            'data': [
                ("A crowbar (Class 1 lever) has a total length of \\(150\\text{ cm}\\). The fulcrum is placed \\(30\\text{ cm}\\) from the load, leaving an effort arm of \\(120\\text{ cm}\\). Calculate its ideal Mechanical Advantage.", "\\(4.0\\)", "\\(5.0\\)", "\\(0.25\\)", "\\(3.0\\)"),
                ("Using a lever with a Mechanical Advantage of \\(5\\), what effort force is required to lift a load of \\(1000\\text{ N}\\)?", "\\(200\\text{ N}\\)", "\\(5000\\text{ N}\\)", "\\(100\\text{ N}\\)", "\\(250\\text{ N}\\)"),
                ("In a wheelbarrow (Class 2 lever), the load arm is \\(0.4\\text{ m}\\) and the effort arm is \\(1.2\\text{ m}\\). Calculate its ideal Mechanical Advantage.", "\\(3.0\\)", "\\(0.33\\)", "\\(4.8\\)", "\\(2.0\\)"),
                ("In a pair of tweezers (Class 3 lever), the load arm is \\(10\\text{ cm}\\) and the effort is applied at \\(5\\text{ cm}\\) from the fulcrum. What is the Mechanical Advantage?", "\\(0.5\\)", "\\(2.0\\)", "\\(1.0\\)", "\\(0.25\\)"),
                ("A force of \\(50\\text{ N}\\) is applied at the end of an effort arm of \\(2\\text{ m}\\) to balance a load placed on a load arm of \\(0.5\\text{ m}\\). Using the principle of moments (\\(\\text{Load} \\times \\text{Load Arm} = \\text{Effort} \\times \\text{Effort Arm}\\)), calculate the load.", "\\(200\\text{ N}\\)", "\\(100\\text{ N}\\)", "\\(50\\text{ N}\\)", "\\(400\\text{ N}\\)"),
                ("A nutcracker of length \\(16\\text{ cm}\\) has a walnut placed \\(4\\text{ cm}\\) from the hinge fulcrum. If an effort force of \\(25\\text{ N}\\) is applied at the handles, calculate the crushing force exerted on the walnut.", "\\(100\\text{ N}\\)", "\\(50\\text{ N}\\)", "\\(75\\text{ N}\\)", "\\(125\\text{ N}\\)"),
                ("A machine lifts a load of \\(600\\text{ N}\\) when an effort of \\(150\\text{ N}\\) is applied. What is the Mechanical Advantage of this machine?", "\\(4.0\\)", "\\(0.25\\)", "\\(750\\text{ N}\\)", "\\(2.5\\)"),
                ("If a machine has a Velocity Ratio of \\(5\\) and a Mechanical Advantage of \\(4\\), calculate the efficiency of the machine.", "\\(80\\%\\)", "\\(125\\%\\)", "\\(20\\%\\)", "\\(90\\%\\)"),
                ("A pulley system has an efficiency of \\(75\\%\\) and a Velocity Ratio of \\(4\\). Calculate the actual Mechanical Advantage of the system.", "\\(3.0\\)", "\\(4.0\\)", "\\(5.33\\)", "\\(2.5\\)"),
                ("An inclined plane has a length of \\(6\\text{ metres}\\) and raises a load to a vertical height of \\(2\\text{ metres}\\). Calculate the ideal Mechanical Advantage (\\(\\frac{\\text{Length}}{\\text{Height}}\\)).", "\\(3.0\\)", "\\(0.33\\)", "\\(12.0\\)", "\\(4.0\\)")
            ],
            'tmpls': [
                "Calculate the lever Mechanical Advantage: {0}",
                "Determine the effort force needed: {0}",
                "Evaluate the Class 2 lever MA: {0}",
                "Compute the Class 3 lever mechanical ratio: {0}",
                "Using the principle of moments, determine: {0}",
                "Calculate the crushing load on the walnut: {0}",
                "Evaluate the mechanical advantage metric: {0}",
                "Compute the machine efficiency percentage: {0}",
                "Calculate the actual operational mechanical advantage: {0}",
                "Determine the inclined plane MA: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract load, effort, arms, or mechanical parameters from the question.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(\\text{{MA}} = \\frac{{\\text{{Load}}}}{{\\text{{Effort}}}} = \\frac{{\\text{{Effort Arm}}}}{{\\text{{Load Arm}}}}\\) and \\(\\eta = \\frac{{\\text{{MA}}}}{{\\text{{VR}}}} \\times 100\\%\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Work Done Calculations (Horizontal & Vertical Gravity)
        {
            'data': [
                ("A horizontal force of \\(50\\text{ N}\\) moves a wooden crate through a distance of \\(6\\text{ metres}\\) along a frictionless floor. Calculate the work done on the crate.", "\\(300\\text{ Joules}\\)", "\\(56\\text{ Joules}\\)", "\\(250\\text{ Joules}\\)", "\\(3000\\text{ Joules}\\)"),
                ("Calculate the work done in lifting a \\(15\\text{ kg}\\) suitcase vertically upward through a height of \\(2\\text{ metres}\\) against gravity (taking \\(g = 9.8\\text{ m/s}^2\\)).", "\\(294\\text{ Joules}\\)", "\\(30\\text{ Joules}\\)", "\\(150\\text{ Joules}\\)", "\\(588\\text{ Joules}\\)"),
                ("Calculate the work done in lifting a \\(20\\text{ kg}\\) bag of cement vertically through a height of \\(5\\text{ metres}\\) (taking \\(g = 10\\text{ m/s}^2\\)).", "\\(1000\\text{ Joules}\\)", "\\(100\\text{ Joules}\\)", "\\(200\\text{ Joules}\\)", "\\(500\\text{ Joules}\\)"),
                ("A pump lifts \\(200\\text{ litres } (200\\text{ kg})\\) of water to an overhead tank at a height of \\(10\\text{ metres}\\) in \\(20\\text{ seconds}\\) (taking \\(g = 10\\text{ m/s}^2\\)). Calculate the work done by the pump.", "\\(20,000\\text{ Joules } (20\\text{ kJ})\\)", "\\(2,000\\text{ Joules}\\)", "\\(40,000\\text{ Joules}\\)", "\\(10,000\\text{ Joules}\\)"),
                ("For the water pump above doing \\(20,000\\text{ Joules}\\) of work in \\(20\\text{ seconds}\\), calculate the power output of the pump in Watts.", "\\(1000\\text{ Watts } (1\\text{ kW})\\)", "\\(500\\text{ Watts}\\)", "\\(2000\\text{ Watts}\\)", "\\(400\\text{ Watts}\\)"),
                ("An electric crane lifts a load of \\(5000\\text{ N}\\) through a vertical height of \\(12\\text{ metres}\\) in \\(30\\text{ seconds}\\). What is the useful work done by the crane?", "\\(60,000\\text{ Joules } (60\\text{ kJ})\\)", "\\(150,000\\text{ Joules}\\)", "\\(30,000\\text{ Joules}\\)", "\\(120,000\\text{ Joules}\\)"),
                ("A gardener pushes a lawnmower applying a force of \\(100\\text{ N}\\) directed at an angle of \\(60^\\circ\\) to the horizontal ground. If the lawnmower travels \\(10\\text{ metres}\\), calculate work done (\\(\\cos 60^\\circ = 0.5\\)).", "\\(500\\text{ Joules}\\)", "\\(1000\\text{ Joules}\\)", "\\(866\\text{ Joules}\\)", "\\(250\\text{ Joules}\\)"),
                ("A student carries a \\(5\\text{ kg}\\) backpack while walking a horizontal distance of \\(50\\text{ metres}\\) on a level floor. Calculate the work done by the student against gravitational force.", "\\(0\\text{ Joules } (\\text{force is vertical while displacement is horizontal, } \\theta = 90^\\circ)\\)", "\\(250\\text{ Joules}\\)", "\\(2450\\text{ Joules}\\)", "\\(500\\text{ Joules}\\)"),
                ("A braking force of \\(400\\text{ N}\\) acts on a moving cart, bringing it to rest after a displacement of \\(8\\text{ metres}\\). Calculate the work done by the braking force.", "\\(-3200\\text{ Joules}\\)", "\\(+3200\\text{ Joules}\\)", "\\(-50\\text{ Joules}\\)", "\\(0\\text{ Joules}\\)"),
                ("A boy of mass \\(45\\text{ kg}\\) climbs up a flight of stairs having \\(20\\text{ steps}\\), each \\(15\\text{ cm } (0.15\\text{ m})\\) high (taking \\(g = 10\\text{ m/s}^2\\)). Calculate total work done by the boy.", "\\(1350\\text{ Joules}\\)", "\\(900\\text{ Joules}\\)", "\\(1800\\text{ Joules}\\)", "\\(2700\\text{ Joules}\\)")
            ],
            'tmpls': [
                "Calculate horizontal mechanical work: {0}",
                "Evaluate vertical gravitational work: {0}",
                "Determine gravitational work on the mass: {0}",
                "Compute hydraulic pump work output: {0}",
                "Calculate pump power output: {0}",
                "Evaluate industrial crane work: {0}",
                "Calculate work done at an angle: {0}",
                "Determine gravitational work on horizontal path: {0}",
                "Evaluate frictional braking work: {0}",
                "Compute gravitational stair-climbing work: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract force \\(F\\) (or \\(m \\times g\\)), displacement \\(s\\), and angle \\(\\theta\\).\\n**Step 2: Arithmetic Evaluation**\\nCompute \\(W = F \\times s \\times \\cos\\theta\\) or \\(W = mgh\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Friction Principles, Drag & Real-World Machine Applications
        {
            'data': [
                ("the maximum value of static friction that comes into play just before a stationary object begins to slide over a surface", "Limiting friction", "Kinetic friction", "Rolling friction", "Viscous drag"),
                ("frictional resistance between two solid surfaces in direct contact is directly proportional to", "The normal reaction force pressing the surfaces together", "The apparent surface area in contact", "The speed of sliding motion", "The ambient atmospheric pressure"),
                ("the dimensionless coefficient \\(\\mu\\) representing the ratio of limiting friction \\(f_L\\) to the normal reaction force \\(R\\)", "Coefficient of friction (\\(\\mu = \\frac{f_L}{R}\\))", "Mechanical Advantage", "Elastic modulus", "Poisson's ratio"),
                ("why spikes are provided on the soles of athletic sprinting shoes and football cleats", "To increase grip and friction with the ground preventing slipping during rapid acceleration", "To reduce the shoe's weight", "To cushion impact forces", "To decrease surface roughness"),
                ("why tyres of automotive vehicles have deep grooves and tread patterns", "To channel water away and maintain high frictional grip on wet roads preventing skidding", "To make tyres look aesthetically pleasing", "To reduce fuel consumption only", "To increase tyre rotational speed"),
                ("the frictional force exerted by fluids (liquids and gases) on solid objects moving through them", "Fluid friction (Drag)", "Static friction", "Dry friction", "Limiting friction"),
                ("the three physical factors upon which fluid friction (drag) depends", "Speed of the object, shape of the object, and viscosity of the fluid", "Mass of the object only", "Color and temperature only", "Volume and sound frequency"),
                ("why meteoroids entering the Earth's upper atmosphere glow brightly and burn up as 'shooting stars'", "Intense atmospheric air friction generates extreme frictional heat", "They reflect direct sunlight", "They contain radioactive nuclear fuel", "They collide with satellites"),
                ("the substance introduced between moving machine parts to reduce friction and wear (e.g., grease, machine oil, graphite powder)", "Lubricant", "Abrasive", "Catalyst", "Electrolyte"),
                ("why talcum powder is sprinkled on a carrom board before playing", "To smooth the board surface and dramatically reduce sliding friction allowing coins to glide easily", "To increase friction so coins stop quickly", "To absorb moisture only", "To protect the wood from termites")
            ],
            'tmpls': [
                "Which threshold frictional limit is defined as: {0}?",
                "What is the physical proportionality governing: {0}?",
                "Which dimensionless mechanical ratio represents: {0}?",
                "What biomechanical objective explains: {0}?",
                "What safety and traction engineering rationale explains: {0}?",
                "Which fluid resistance phenomenon corresponds to: {0}?",
                "What physical factors govern: {0}?",
                "What atmospheric physical phenomenon causes: {0}?",
                "Which chemical friction-reducing substance is described by: {0}?",
                "What tribological purpose is achieved by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Tribology and Friction Mechanics**\\nThe question targets {item[0]}.\\n**Step 2: Surface Interactions and Fluid Drag**\\nFriction depends on surface microscopic asperities and normal force; fluid drag depends on shape streamlining, speed, and fluid viscosity.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Problems in Power, Multi-Pulley Systems & Machine Work
        {
            'data': [
                ("An electric motor lifts an elevator weighing \\(6000\\text{ N}\\) through a vertical height of \\(20\\text{ metres}\\) in \\(10\\text{ seconds}\\). Calculate the power consumed by the motor in Kilowatts.", "\\(12\\text{ kW } (12,000\\text{ W})\\)", "\\(6\\text{ kW}\\)", "\\(24\\text{ kW}\\)", "\\(1.2\\text{ kW}\\)"),
                ("A man does \\(1800\\text{ Joules}\\) of work in \\(1\\text{ minute } (60\\text{ seconds})\\). What is the power exerted by the man?", "\\(30\\text{ Watts}\\)", "\\(1800\\text{ Watts}\\)", "\\(60\\text{ Watts}\\)", "\\(108\\text{ Watts}\\)"),
                ("In a block and tackle pulley system having \\(4\\text{ pulleys}\\) (Velocity Ratio \\(VR = 4\\)), an effort of \\(250\\text{ N}\\) lifts a load of \\(800\\text{ N}\\). Calculate the efficiency of the pulley system.", "\\(80\\%\\)", "\\(85\\%\\)", "\\(75\\%\\)", "\\(90\\%\\)"),
                ("A block and tackle system with \\(5\\text{ pulleys}\\) (\\(VR = 5\\)) operates at \\(80\\%\\) efficiency. What maximum load can be lifted by applying an effort of \\(200\\text{ N}\\)?", "\\(800\\text{ N}\\)", "\\(1000\\text{ N}\\)", "\\(600\\text{ N}\\)", "\\(750\\text{ N}\\)"),
                ("A wheel and axle has a wheel radius of \\(40\\text{ cm}\\) and an axle radius of \\(8\\text{ cm}\\). If the machine is ideal, calculate its Mechanical Advantage.", "\\(5.0\\)", "\\(0.2\\)", "\\(320\\)", "\\(4.0\\)"),
                ("Using the wheel and axle above (\\(MA = 5\\)), what effort is required to raise a water bucket weighing \\(150\\text{ N}\\) from a well?", "\\(30\\text{ N}\\)", "\\(750\\text{ N}\\)", "\\(15\\text{ N}\\)", "\\(50\\text{ N}\\)"),
                ("Calculate the work done by a force of \\(80\\text{ N}\\) pushing an object a distance of \\(15\\text{ m}\\) against a frictional force of \\(30\\text{ N}\\). What is the net useful work done on the object?", "\\(750\\text{ Joules } (\\text{Net force } 50\\text{ N} \\times 15\\text{ m})\\)", "\\(1200\\text{ Joules}\\)", "\\(450\\text{ Joules}\\)", "\\(1650\\text{ Joules}\\)"),
                ("An engine delivers \\(20\\text{ horsepower (hp)}\\). Taking \\(1\\text{ hp} = 746\\text{ Watts}\\), calculate the engine's power rating in Kilowatts.", "\\(14.92\\text{ kW } (14,920\\text{ W})\\)", "\\(20.0\\text{ kW}\\)", "\\(10.5\\text{ kW}\\)", "\\(18.65\\text{ kW}\\)"),
                ("A machine has an efficiency of \\(60\\%\\). If the energy supplied to the machine is \\(5000\\text{ Joules}\\), calculate the useful work output obtained.", "\\(3000\\text{ Joules}\\)", "\\(2000\\text{ Joules}\\)", "\\(4000\\text{ Joules}\\)", "\\(2500\\text{ Joules}\\)"),
                ("In a hydraulic jack, a force of \\(100\\text{ N}\\) applied on a small piston of area \\(5\\text{ cm}^2\\) creates pressure. What lifting force is produced on a large piston of area \\(250\\text{ cm}^2\\)?", "\\(5000\\text{ N}\\)", "\\(2500\\text{ N}\\)", "\\(1000\\text{ N}\\)", "\\(12,500\\text{ N}\\)")
            ],
            'tmpls': [
                "Calculate motor power rating: {0}",
                "Determine the metabolic power output: {0}",
                "Evaluate the 4-pulley system efficiency: {0}",
                "Compute maximum load capacity for the pulley: {0}",
                "Calculate wheel and axle mechanical advantage: {0}",
                "Determine the required effort force: {0}",
                "Calculate the net useful work under friction: {0}",
                "Convert mechanical horsepower to kilowatts: {0}",
                "Evaluate useful work output from efficiency: {0}",
                "Determine hydraulic force multiplication: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract power, load, effort, areas, or machine parameters.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(P = \\frac{{W}}{{t}}\\), \\(\\text{{MA}} = \\frac{{L}}{{E}}\\), \\(\\eta = \\frac{{\\text{{MA}}}}{{\\text{{VR}}}}\\), or Pascal's law \\(\\frac{{F_1}}{{A_1}} = \\frac{{F_2}}{{A_2}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
