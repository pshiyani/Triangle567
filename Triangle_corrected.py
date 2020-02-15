"""
SSW_567
Author - Priyankaben Shiyani
Project Description: Triangle Classification Implementation
"""
def Classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle and this function will 
    tell us whether the triangle is scalene,isosceles, equilateral or right triangle
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return 'InvalidInput'
    else:
        [a, b, c] = sorted([a, b, c])
        """sum of two side should be > then third side"""
        if (a > 200 or b > 200 or c > 200) or (a <= 0 or b <= 0 or c <= 0):
            return 'InvalidInput'
        else:
            if ((a + b) > c)and ((a + c) > b) and ((b + c) > a):
                if round(((a ** 2) + (b ** 2)), 2) == round((c ** 2), 2):
                    """check triangle is Right Isosceles or Right Scalene"""
                    if a == b or b == c or c == a:
                        return 'Right Isosceles'
                    else:
                        return 'Right Scalene'
                elif a == b == c:
                    """ check if triangle is Equilateral"""
                    return 'Equilateral'
                elif a == b or b == c or c == a:
                    """ check triangle is Isosceles or Scalene """
                    return 'Isosceles'
                else:
                    return 'Scalene'
            else:
                """If it is not triangle"""
                return 'NotATriangle'