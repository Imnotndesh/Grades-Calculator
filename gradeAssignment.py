from tabulate import tabulate

class app:
    def grade_calculation(self,catOne,CatTwo,fullExam):
        # Cat totals calculation
        catSum = []
        indexCount = 0
        for item in catOne:
            catSum.append((catOne[indexCount]+catTwo[indexCount])/2)
            indexCount = indexCount+1
        
        #Cumulative total calculation 
        fullExamIndex = 0
        self.cumlTotal = []
        for item in fullExam:
            self.cumlTotal.append(round((catSum[fullExamIndex]+fullExam[fullExamIndex])*(100/130)))
            fullExamIndex = fullExamIndex + 1
        
        # Grade cases
        self.ovrgrades = []
        for item in self.cumlTotal:
            if item <= 29:
                self.ovrgrades.append("F")
            elif item <= 34 and item >= 30 :
                self.ovrgrades.append("D-")
            elif item <= 39 and item >= 35 :
                self.ovrgrades.append("D")
            elif item <= 44 and item >= 40 :
                self.ovrgrades.append("D+")
            elif item <= 49 and item >= 45 :
                self.ovrgrades.append("C-")
            elif item <= 54 and item >= 50 :
                self.ovrgrades.append("C")
            elif item <= 59 and item >= 55 :
                self.ovrgrades.append("C+")
            elif item <= 64 and item >= 60 :
                self.ovrgrades.append("B-")
            elif item <= 69 and item >= 65 :
                self.ovrgrades.append("B")
            elif item <= 74 and item >= 70 :
                self.ovrgrades.append("B+")
            elif item <= 79 and item >= 75 :
                self.ovrgrades.append("A-")
            else:
                self.ovrgrades.append("A")
        return self.cumlTotal,self.ovrgrades

## Creation of data rows for table
    def gen_table(self,catOne,catTwo,fullExam):
        self.grade_calculation(catOne,catTwo,fullExam)
        table_context = [['CAT1','CAT2','FULL EXAM','TOTAL','GRADE']]
        index = 0
        for items in catOne:
            table_context.append([catOne[index],catTwo[index],fullExam[index],self.cumlTotal[index],self.ovrgrades[index]])
            index = index+1
        print(tabulate(table_context,headers='firstrow'))
        
        
    
# Programm variables
catOne = [10,10,5,7,6]
catTwo = [8,11,6,30,7]
fullExam = [100,7,70,70,50]
app = app()
app.gen_table(catOne,catTwo,fullExam)

# # For manual entry:
# print("+---------------+")
# print("Manual Entry mode")
# catOne = []
# catTwo =[]
# fullExam =[]

# app=app()
# examEntries = int(input("Enter amount of exam entries (rows)" ))

# # CAT 1 entries
# startIndexCatOne = 0
# print('---Cat 1 entries---')
# while startIndexCatOne < examEntries:
#     catOneEntry = int(input(f'Entry number {startIndexCatOne}: '))
#     catOne.append(catOneEntry)
#     startIndexCatOne = startIndexCatOne + 1

# # CAT 2 entries
# startIndexCatTwo = 0
# print('---Cat 2 entries---')
# while startIndexCatTwo < examEntries:
#     catTwoEntry = int(input(f'Entry number {startIndexCatTwo}: '))
#     catTwo.append(catTwoEntry)
#     startIndexCatTwo = startIndexCatTwo + 1

# # Full exam entries
# startIndexFull = 0
# print('---Full Exam entries---')
# while startIndexFull < examEntries:
#     fullEntry = int(input(f'Entry number {startIndexFull}: '))
#     fullExam.append(fullEntry)
#     startIndexFull= startIndexFull + 1

    
# print("Entries Completed.")
# print("Generating......")
# print("+..................+")
# app.gen_table(catOne,catTwo,fullExam)
