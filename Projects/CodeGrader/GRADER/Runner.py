from Db import Db
from File import File
from Evaluator import Evaluator
import time

class Runner:
    def executeFlow(self):

            self.db = Db()
            query_get_submission = "SELECT submission_id, file_name, question_id FROM submission WHERE status='pending' ORDER BY time_of_submission ASC LIMIT 1"
            results = self.db.executeQuery(query_get_submission)
            if results == ():
                return

            else:
                self.sub_id = str(results[0][0])
                file_name = results[0][1]
                question_id = results[0][2]

                query_update_status = "UPDATE submission SET status='processing' WHERE submission_id =" + self.sub_id
                self.db.executeQuery(query_update_status)

                submission_file = File(self.sub_id, file_name)
                submission_file.downloadFile()
                evaluate = Evaluator(submission_file, question_id)
                result = evaluate.executeSource()
                count_success = 0
                count_total = 0
                if result == [0]:
                    self.final_result = "compilation error"
                if result == [1]:
                    self.final_result = "runtime error"
                else:
                    for success in result:
                        count_total = count_total + 1
                        if success == 2:
                            count_success= count_success + 1
                    self.final_result = str(count_success)+" out of "+ str(count_total) + " are correct "

            self.updateDatabase()


    def updateDatabase(self):

        query_update_database = "UPDATE submission SET status='processed', result = \"" + self.final_result + "\"WHERE submission_id = "+ self.sub_id
        self.db.executeQuery(query_update_database)



if __name__ == "__main__":
    flow = Runner()
    while(True):
     flow.executeFlow()
     time.sleep(5)


    




