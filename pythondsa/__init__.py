''' 
Use of the functions 
'''

from timeit import default_timer as timer
import math

def evaluate_test_cases(fun_name, test_list):
    
    counter = 0
    
    for test_case in test_list:
        
        print("TEST CASE #", counter, sep='')
        
        Input = test_case["input"]
        Output = test_case["output"]
        
        start = timer()
        fun_output = fun_name(*Input.values())      
        end = timer()
        
        exec_time = math.ceil((end - start) * 10**6) / 1000
        
        if type(Output) == list:
            
            result = "PASSED" if (fun_output in Output) == True else "FAILED"
            
        else:
            result = "PASSED" if (fun_output == Output) == True else "FAILED"
            
        print("\nInput:\n", Input, sep='')
        print("\n\nExpected Output:\n", Output, sep='')
        print("\n\nActual Output:\n", fun_output, sep='')
        print("\n\nExecution Time:\n", exec_time, " ms", sep='')
        print("\n\nTest Result:\n", result, "\n\n\n", sep='')
        
        counter += 1