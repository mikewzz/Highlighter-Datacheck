# Highlighter-Datacheck
Highlighter Datacheck
- Necessities
- Be able to check c1 & c2 do not have overlapping data in the same columns for each record
- Be able to check that 'noanswer' is successful punching and clearing all columns for each record
- Be able to check that if all columns selected at c1, then c2 is skipped (Should be a flag for this to see if way too many peopel are selecting "all" then there is likely an issue)
- Compare the 'datamap' of each datafile we download and compare with materials to ensure the correct columns/text are being displayed
            - Flag 

- Function
- Take xlsx datafile input
- User input of column label index of first concept highlighter row/column

# March 28, 2020

- Variables that we need to establish
    - How many concepts are there in this study
    - How many rows are there in each concept
    - Is there logic connecting the first and second highlighters where a check needs to take place
    - Is there a None option that we need to check for

# April 2, 2020

- Created a function to return indexes of the first row of each highlighter question; hl_index
    - Based on the user inputted dynamic highlighter labels
- Imported numpy for this function
- Next we need to be able to write a function to check for any overlapping columns within each ROW (record)
