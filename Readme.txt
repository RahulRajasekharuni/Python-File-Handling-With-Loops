Task
A video games club, AB Games, has many members who can connect to the AB Games servers and play many Play Station games (such as Assassin’s Creed, Call of Duty, Minecraft, Nino Kuni and Naruto) online even without needing to have a Play Station. Each time they play a game they pay $2 on top of their monthly membership fees.

Many members discontinue with AB Games after some time. AB Games is very keen to identify reasons why members discontinue and thereby reduce attrition.

AB Games have a rich database on their members having information of each member on Age, Win-Loss Ratio, Number of Log-ins, Gender, Income and Status (i.e. whether continued or discontinued). They then run a data mining algorithm called SysFor, which automatically discovers logic rules on why some members discontinue while others continue. AB Games runs SysFor and fortunately you DO NOT have to code SysFor.

Assume that SysFor produces logic rules from a dataset and the logic rules are stored by SysFor in a text file called Rules.txt as follows.

Age		Win-Loss	Log-in		Gender		Income		Status
--------------------------------------------------------------------------------------
35		5		512		Male		20000		?
20		2		200		Female		30000		?



GE stands for Greater than or Equal to, LT stands for Less Than, and the “-“ sign indicates has no impact.

Other than the two header lines the Rules.txt file has six lines meaning that there are six logic rules. Each rule tells us the properties of the members who continue/discontinue.

The first rule states that if the Age of a member is greater than or equal to 25, the member is Male, and his Win-Loss ratio is greater than or equal to 8, then the member continues with the club. For ease of understanding, it can also be represented as: If Age >= 25 & Gender = Male & Win-Loss >= 8 --> Continue. Similarly, the 2nd rule states that If Age >= 25 & Gender = Male & Win-Loss < 8 --> Discontinue.

AB Games also has a dataset on their current members for whom AB Games does not know whether they will continue or discontinue. The dataset is stored in a file called Members.txt as follows.

Age		Win-Loss	Log-in		Gender		Income		Status
--------------------------------------------------------------------------------------
35		5		512		Male		20000		Discontinue
20		2		200		Female		30000		Continue



In the Members.txt file there are two current members. The first member is 35 years old, has a Win-Loss ratio of 5, has logged in 512 times, is Male, and earns $20,000 per annum. The file also has similar information on the second member. However, the “?” mark for the variable Status indicates that AB Games at this stage does not know whether or not the members will continue with them.

Write a Python code that will match the members in the Members.txt file with the logic rules in the Rules.txt file to identify the Status of each member. Your Python code will then write a file called MemberReport.txt as follows.

 
Since the first member in the Members.txt file has age greater than 25 and win loss ratio less than 8 and he is a Male, he matches the 2nd rule in the Rules.txt file which suggests that he will discontinue. Similarly, the 2nd member matches the 4th rule which suggests that she will continue.

Note that although the structure and schema of the Rules.txt file and Members.txt file will remain unchanged AB Games can change the values in the files. Additionally, the Rules.txt file can have any number of rules. Similarly, the Members.txt file can also have any number of members. Your Python code should still produce correct MemberReport.txt file.

Your Python code should also generate a file called ReadableRules.txt which will convert the rules in Rules.txt into a more readable format as follows.
 

Rule 1: If Age >= 25 & Win-Loss >= 8 & Gender = Male --> Continue. 
Rule 2: If Age >= 25 & Win-Loss < 8 & Gender = Male --> Discontinue.
Rule 3: If Age >= 25 & Gender = Female --> Discontinue.
Rule 4: If Age < 25 & Log-in >= 150 --> Continue.
Rule 5: If Age < 25 & Win-Loss >= 5 & Log-in <150 --> Continue.
Rule 6: If Age < 25 & Win-Loss < 5 & Log-in < 150 --> Discontinue.


Rules.txt, Members.txt, ReadableRules.txt and MemberReport.txt files should be in the same folder as the Python code.

Use appropriate data structure in writing your code.

All exceptions need to be handled. Invalid inputs need to be handled and asked for a valid input again.

Use functions to make your program well designed, instead of just using a single main function. We expect you to use at least four (4) functions other than the main function.

Write an algorithm in structured English (pseudocode) that describes the steps required to perform the task specified. Some examples of pseudocode can be found at http://www.unf.edu/~broggio/cop2221/2221pseu.htm. 

Implement your algorithm in Python. 

Avoid duplicate code. 

Comment your code as necessary to explain it clearly.

Select 3 sets of test data that will demonstrate the correct “normal” operation of your program. 

Run your program using the test data you have selected and save the output it produces in a text file. 
