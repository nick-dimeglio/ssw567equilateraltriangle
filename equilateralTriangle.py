import math
import unittest


def classifyTriangle(a, b, c):

    # First, check to make sure each variable input is a valid integer/float input.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return ("NotATriangle")

    # for the sake of ease of writing the if statement for right triangles, I'll reorganize the variables to be sorted in order where c is the largest and a is the smallest.
    # While theoretically this is O(nlog(n)) time complexity, since it is only 3 variables long ever, I'm not too concerned.
    # I will also turn the a,b, and c variables into the absolute values of themselves, to allows for negative inputs to be considered, since -5 and 5 would be the same in terms of triangle lengths.
    a = abs(a)
    b = abs(b)
    c = abs(c)
    temparr = [a, b, c]
    temparr.sort()
    a, b, c = temparr[0], temparr[1], temparr[2]

    # First ensure that the triangle inequality theorem is true, meaning that the three lengths make a valid triangle before continuing.
    if (a+b > c):

        # checking cases in order of specificity, meaning that the higher in the if elif chain, the more specific it is.
        # Check for if it is equilateral, if it isnt, check for right, if it isnt, check for isosceles, if it isnt, return scalene.
        if a == b == c:
            return ("Equilateral")

        elif round((a ** 2), 5) + round((b ** 2), 5) == round((c ** 2), 5):
            return ("Right")
        elif a == b or b == c or a == c:
            return ("Isosceles")
        else:
            return ("Scalene")
    else:
        return ("NotATriangle")


#classifyTriangle(1, 1, math.sqrt(2))


class TestTriangles(unittest.TestCase):
    def testInvalid(self):
        self.assertEqual(classifyTriangle(
            "!", 3, "{"), "NotATriangle", "!, 3, and { are most definitely not a triangle.")
        self.assertEqual(classifyTriangle(2, 2, 10), "NotATriangle",
                         "2, 2, and 10 should not be a triangle as they fail a + b > c")

    def testValid(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right",
                         "3,4,5 is a right triangle.")
        self.assertEqual(classifyTriangle(1, 1, math.sqrt(
            2)), "Right", "Any triangle in the x : x : x*sqrt(2) should be a right triangle.")
        self.assertEqual(classifyTriangle(-15, 8, -17),
                         "Right", "-15,8,-17 is a right triangle.")

        self.assertEqual(classifyTriangle(3, 3, 3),
                         "Equilateral", "3,3,3 is equilateral.")
        self.assertEqual(classifyTriangle(-2, 2, -2),
                         "Equilateral", "-2,2,-2 is equilateral")
        self.assertEqual(classifyTriangle(-1.0, -1, -1.000), "Equilateral",
                         "These are all -1 and -1,-1,-1 is equilateral.")

        self.assertEqual(classifyTriangle(2, 2, 3), "Isosceles",
                         "Two sides are equal in 2,2,3, so it is isosceles.")
        self.assertEqual(classifyTriangle(-1.5, -1.5, -1.51), "Isosceles",
                         "Two sides are equal in -1.5,-1.5,-1.51 so it should be isosceles.")
        self.assertEqual(classifyTriangle(math.sqrt(2), math.sqrt(
            2), 1), "Isosceles", "Two sides are equal in this, so it should be isosceles.")

        self.assertEqual(classifyTriangle(5, 6, 7), "Scalene",
                         "Valid triangle without any special properties.")
        self.assertEqual(classifyTriangle(-5, 6.0, -7.0), "Scalene",
                         "Valid, albeit oddly defined, triangle that has no special properties.")
        self.assertEqual(classifyTriangle(8, -15, 20),
                         "Scalene", "Valid and non-special triangle.")


if __name__ == "__main__":
    unittest.main(exit=True)
