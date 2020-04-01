import pandas as pd
import itertools as it

#myXls = pd.ExcelFile('1sheet.xlsx')

#df1 = pd.read_excel(myXls, 'A1')
#df2 = pd.read_excel(myXls, 'Datamap')
#print(df1.columns)
#print(df2.columns)

conceptCount = 0

hlCount = 4 #input ("How many highlighter questions are in this study?\n")
conceptCount = 4 #input ("How many concepts are in this study?\n")
conLabel = "_C" #input ("Please enter the label of the first concept. (ie. _C or _Con)\n")

#print ("TYPE conceptCount: ", type(conceptCount))
#print ("TYPE firstConName: ", type(conLabel))
#No answer ie. "noanswerQC200_C1_rNone"
#tCON_eval_01_Con11

hlLabels=[]
hlTextLabel=["first", "second", "third", "fourth", "fifth", "sixth"]
# for y in range (0, int(hlCount)):
#     hlLabelCurrent = input ("Please enter the label of the " + hlTextLabel[y] + " highlighter question.\n")
#     hlLabels.append(hlLabelCurrent)

hlLabels=["QC200", "QC205" ,"QC210", "QC215"]
print (hlLabels)

conceptCount = int(conceptCount)
conArray=[]
conWordCount=[]
for x in range (1,conceptCount+1):
    for z in range (0, int(hlCount)):
        conArray.append((hlLabels[z] + conLabel + str(x)))
    currCon_WC = input ("How many rows are in Concept" + str(x) + "?\n")
    conWordCount.append(int(currCon_WC))

print (conArray)
print (conWordCount)


#This function will cycle through from r1 to r(x) for each highlighter for each concept dependent on the numbers of rows in each respective concept
def cycleWordRows(curQLabel, indexOfWordCountArray):
    for con1 in range (1,conWordCount[indexOfWordCountArray]+1):
        print (curQLabel + "r" + str(con1))

myCounter1 = 0
wordCountIdx = 0
for idx, q in enumerate(conArray):
    if myCounter1 < conceptCount:
        cycleWordRows(q, wordCountIdx)
    else:
        wordCountIdx = wordCountIdx + 1
        cycleWordRows(q, wordCountIdx)
        myCounter1 = 0
    myCounter1 = myCounter1 + 1

# for h,i,j,k in zip(conArray[0::4], conArray[1::4], conArray[2::4],conArray[3::4]):
#     print("THIS IS H: " + h)
#     print("THIS IS I: " + i)
#     print("THIS IS J: " + j)
#     print("THIS IS K: " + k)
