from File import File
import subprocess
import os
import os.path

class Evaluator:

    base_test_url = "/home/saumya/Desktop/test_cases"
    result = {'compilation-error':0, 'runtime-error':1, 'successful':2, 'unsuccessful':3}

    def __init__(self, sourcefile, ques_no):
        self.sourcefile = sourcefile
        self.ques_no = str(ques_no)
        self.isCompiled = False

       
    def executeSource(self):
        if self.sourcefile.getLanguage() == "java":
            compile_command = "cd %s; javac %s "%(self.sourcefile.getLocalDestinationDir() , self.sourcefile.getFileName())
            run_command = "cd %s; java %s "%(self.sourcefile.getLocalDestinationDir(), self.sourcefile.getClassName())
        if self.sourcefile.getLanguage() == "py":
            compile_command ="python -m py_compile %s"
            run_command =  "cd %s; python %s "%(self.sourcefile.getLocalDestinationDir() , self.sourcefile.getFileName())
        if self.sourcefile.getLanguage() == "cpp":
            compile_command = "cd %s; g++ %s -w -o %s.out"%(self.sourcefile.getLocalDestinationDir() , self.sourcefile.getFileName() , 
                self.sourcefile.getClassName())
            run_command = "cd %s; ./%s.out "%(self.sourcefile.getLocalDestinationDir(), self.sourcefile.getClassName())
        if self.sourcefile.getLanguage() == "c":
            compile_command = "cd %s; gcc %s -w -o %s.out ;"%(self.sourcefile.getLocalDestinationDir() , self.sourcefile.getFileName() , 
                self.sourcefile.getClassName())
            run_command = "cd %s; ./%s.out "%(self.sourcefile.getLocalDestinationDir(), self.sourcefile.getClassName())
    

        result_list = []
        if not self.isCompiled:
            compile_output = self.execute(compile_command)
            if compile_output[0]!=0:
                result_list.append(0)        #compiletime error
                return result_list       
            self.isCompiled = True
            


        DIR = Evaluator.base_test_url + "/" + self.ques_no + "/" + "inputs"
        length = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        for case_number in range(1,length+1):
            input_file_path = Evaluator.base_test_url + "/" + self.ques_no + "/" + "inputs" + "/" + str(case_number)
            if not os.path.isfile(input_file_path): 
                break
            else:
                file_object = open(input_file_path, 'r')
                test_input = file_object.read().strip()
                print test_input

            output_file_path = Evaluator.base_test_url + "/" + self.ques_no + "/" + "outputs" + "/" + str(case_number)
            file_object = open(output_file_path, 'r')
            test_output = file_object.read().strip()
            print test_output

            

            run_output = self.execute(run_command, test_input)
            if run_output[0]!=0:
                result_list.append(1)    #runtime error
                return result_list
            else:
               
                if run_output[1].strip() == test_output:
                    result_list.append(2)
                else:
                    result_list.append(3)
        return result_list
                

    def execute(self, command, input= "", env={}):
        p = subprocess.Popen([command], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.stdin.write(input)
        proc_stdout, proc_stderr = p.communicate()
        return ( p.returncode, proc_stdout, proc_stderr)


    

if __name__ == "__main__":
    #f = File("promises", "Promise.java")
    f = File("master", "setup.py")
    f.downloadFile()
    e = Evaluator(f)
    print e.executeSource()



