import calculator
# Project 2: IVS-calculator - Tests                      
# Author: Lukas Csader 
# Mail: xcsade00@stud.fit.vutbr.cz 
# Date: 7.10.2021

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
    