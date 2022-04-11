#!/usr/bin/python3
# Project 2: IVS-calculator - Tests                      
# Author: Lukas Csader 
# Mail: xcsade00@stud.fit.vutbr.cz 
# Date: 7.10.2021

import calculator

#Test class contains methods for testing and printing results
class Test:
    def __init__(self):
        self.test_count = 0
        self.pass_count = 0

    #Function comparing output with expected output
    #Arguments: test_name,input(from tested function), output(expected output)
    #Calls function print_result() to print result of the test 
    def expect_EQ(self,test_name,input,output):
        if input == output:
            self.print_result(test_name,input,output,False)
        else:
            self.print_result(test_name,input,output,True)
    
    #Function to print result of the test
    #Arguments: Test_name, input, output, error(True - print error message, False - test passed) 
    def print_result(self,test_name,input,output,error):
        self.test_count += 1
        if error:
            print('[FAILED]', test_name)
            print("Expected result:")
            print(output)
            print('Given result: ',''.join(str(input)))
        else:
            self.pass_count += 1
            print('[PASSED]', test_name)

    #Function to print stats
    #prints numbers of - passed tests / all tests (percentage of passed tests)
    def print_stats(self):
        print(" RESULTS ".center(40, '#'))
        print('Passed: {}/{} ({}%)'.format(self.pass_count, self.test_count, (self.pass_count / self.test_count) * 100))
        pass
if __name__ == '__main__':
    t1 = Test()
    print(" TEST_SUM ".center(40, '#'))
    t1.expect_EQ("Test_sum_2+2",calculator.res("2+2"),"4")
    t1.expect_EQ("Test_sum_2+0",calculator.res("2+0"),"2")
    t1.expect_EQ("Test_sum_-2+1",calculator.res("-2+1"),"-1")
    t1.expect_EQ("Test_sum_-2+1+10",calculator.res("-2+1+10"),"9")
    print(" TEST_SUB ".center(40, '#'))
    t1.expect_EQ("Test_sub_-2-1",calculator.res("-2-1"),"-3")
    t1.expect_EQ("Test_sub_2-2",calculator.res("2-2"),"0")
    t1.expect_EQ("Test_sub_9999-9998",calculator.res("9999-9998"),"1")
    t1.expect_EQ("Test_sub_100-101",calculator.res("100-101"),"-1")
    t1.expect_EQ("Test_sub_100-99-2",calculator.res("100-99-2"),"-1")
    print(" TEST_MUL ".center(40, '#'))
    t1.expect_EQ("Test_mul_100*0",calculator.res("100*0"),"0")
    t1.expect_EQ("Test_mul_100*1",calculator.res("100*1"),"100")
    t1.expect_EQ("Test_mul_100*-2",calculator.res("100*-2"),"-200")
    t1.expect_EQ("Test_mul_6*8",calculator.res("6*8"),"48")
    t1.expect_EQ("Test_mul_2*0.5",calculator.res("2*0.5"),"1.0")
    t1.expect_EQ("Test_mul_-2*-2",calculator.res("-2*-2"),"4")
    print(" TEST_DIV ".center(40, '#'))
    t1.expect_EQ("Test_div_100/0",calculator.res("100/0"),"ERROR")
    t1.expect_EQ("Test_div_100/1",calculator.res("100/1"),"100.0")
    t1.expect_EQ("Test_div_100/2",calculator.res("100/2"),"50.0")
    t1.expect_EQ("Test_div_7/4",calculator.res("7/4"),"1.75")
    t1.expect_EQ("Test_div_8/-4",calculator.res("8/-4"),"-2.0")
    t1.expect_EQ("Test_div_-8/-4",calculator.res("-8/-4"),"2.0")
    t1.expect_EQ("Test_div_0/-4",calculator.res("0/-4"),"0.0")
    t1.expect_EQ("Test_div_2/0.5",calculator.res("2/0.5"),"4.0")
    print(" TEST_SQ ".center(40, '#'))
    t1.expect_EQ("Test_sq_100**0",calculator.res("100**0"),"1")
    t1.expect_EQ("Test_sq_100**1",calculator.res("100**1"),"100")
    t1.expect_EQ("Test_sq_2**2",calculator.res("2**2"),"4")
    t1.expect_EQ("Test_sq_2**3",calculator.res("2**3"),"8")
    t1.expect_EQ("Test_sq_3**3",calculator.res("3**3"),"27")
    t1.expect_EQ("Test_sq_2**6",calculator.res("2**6"),"64")
    t1.expect_EQ("Test_sq_50**3",calculator.res("50**3"),"125000")
    t1.expect_EQ("Test_sq_2**-1",calculator.res("2**-1"),"0.5")
    print(" TEST_SQRT ".center(40, '#'))
    t1.expect_EQ("Test_sqrt_4**(1/2)",calculator.res("4**(1/2)"),"2.0")
    t1.expect_EQ("Test_sqrt_0**(1/2)",calculator.res("0**(1/2)"),"0.0")
    t1.expect_EQ("Test_sqrt_-2**(1/2)",calculator.res("-2**(1/2)"),"ERROR")
    t1.expect_EQ("Test_sqrt_-8**(1/3)",calculator.res("-8**(1/3)"),"-2.0")
    t1.expect_EQ("Test_sqrt_8**(1/3)",calculator.res("8**(1/3)"),"2.0")
    t1.expect_EQ("Test_sqrt_64**(1/2)",calculator.res("64**(1/2)"),"8.0")
    print(" TEST_FACT ".center(40, '#'))
    t1.expect_EQ("Test_factorial_2",calculator.factorial(2),2)
    t1.expect_EQ("Test_factorial_3",calculator.factorial(3),6)
    t1.expect_EQ("Test_factorial_-2",calculator.factorial(-2),"ERROR")
    t1.expect_EQ("Test_factorial_0",calculator.factorial(0),1)
    t1.expect_EQ("Test_factorial_9",calculator.factorial(9),362880)
    t1.expect_EQ("Test_factorial_1",calculator.factorial(1),1)
    
    t1.print_stats()