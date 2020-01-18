import random
import bisect


class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = []
    # Probability of the occurence of random_nums
    _probabilities = []

    # Probability ranges
    _probability_ranges = []

    def normalize_probabilities(self):
        """ 
            If the total of probabilitites does not sum up to 1, normalize them
            Compute ranges to use for next_rand
        """
        total_probability = sum(self._probabilities)
        self._probability_ranges = []

        element = 0
        for prb in self._probabilities:
            element += prb / total_probability
            self._probability_ranges.append(element)

    def __init__(self, number_probabilities: dict):
        """Init

        number_probabilities is a dictionary of values and its probabilities
        example [ 1 : 0.05, -1, 0.5, ..]
        """
        if (type(number_probabilities) is not dict):
            raise NameError('expected dictionary of value : probablity')

        self._probabilities = number_probabilities.values()
        self._random_nums = list(number_probabilities.keys())

        self.normalize_probabilities()

    def next_num(self):
        """Returns one of the randomNums.

        When this method is called multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """

        item = bisect.bisect_left(self._probability_ranges, random.random())
        return self._random_nums[item]


def generate_random_input(num_elements):
    input = {}
    for n in range(num_elements):
        element = random.randint(-10, 100)
        probability = random.random()
        input[element] = probability
    return input


def get_generator_output(generator, number_of_iterations):
    test_res = {}
    
    for i in range(number_of_iterations):
        r = generator.next_num()
        if r not in test_res:
            test_res[r] = 1
        else:
            test_res[r] += 1
    return test_res


def verify(input, result, allowed_error):
    if (input.keys() != result.keys()):
        print("Error! Elements do not match")
        print("Expected numbers: ", input.keys(), "Actual ", result.keys())
        return

    rs = sum(result.values())
    total_input_probability = sum(input.values())
    for num in result:
        actual_probability = result[num]/rs
        expected_probability = input[num] / total_input_probability
        if (abs(actual_probability - expected_probability) > allowed_error):
            print("Error! Probability is not correct")
            print("Element: ", num, "Expected", expected_probability,
                  "Actual ", actual_probability)


def unit_test_RandomGen(number_of_test_cases, max_number_of_elements=10):

    ALLOWED_ERROR = 0.01
    NUMBER_OF_ITERATIONS = 100000
    for i in range(number_of_test_cases):

        print("TEST", i+1)
        num_elements = random.randint(0, max_number_of_elements)

        input = generate_random_input(num_elements)
        generator = RandomGen(input)
        test_res = get_generator_output(generator, NUMBER_OF_ITERATIONS)
        verify(input, test_res, ALLOWED_ERROR)


unit_test_RandomGen(3, 15)
