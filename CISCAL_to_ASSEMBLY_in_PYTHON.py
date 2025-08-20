import sys





#LEKTIKOS ANALYTHS

#alphabet characters
alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#natural numbers
numbers=['0','1','2','3','4','5','6','7','8','9']

#open test file
file = open(str(sys.argv[1]),'r')               #take file from command line


#transition table characters -> xarakthrew pinaka metabasevn

                            # Symbol

whitecharacter=0                 # " "

letters=1                   # [a,b,..,w,z]

number=2                    # [1,2,...,8,9]

plus=3                      # +
minus=4                     # -
multiply=5                  # *
divide=6                    # /

equal=7                     # =
lessThan=8                  # <
greaterThan=9               # >

EndOfFile=10                #

notAcceptableSymbol=11      #

comma=12                    # ,
questionMark=13             # ;

leftParenthesis=14          # (
rightParenthesis=15         # )
leftBracket=16              # [
rightBracket=17             # ]

blockOpening=18             # {
blockClosing=19             # }

lineChange= 20              # (Enter)

colon=21                    # :
period=22                   # .
hashtag=23


#Status -> Katastaseis

Status_start=0              # start

Status_letter=1             # a,b,...,y,z
Status_number=2             # 1,2,...

Status_lessThan=3           # <
Status_greaterThan=4        # >

Status_assignment=5         # :=
Status_comments=6           # #

#Tokens

identifier_Token=50         # name of anything we need
number_Token=51             # [1,2,...,8,9]

plus_Token=52               # +
minus_Token=53              # -
multiply_Token=54           # *
divide_Token=55             # /

equal_Token=56              # =
lessThan_Token=57           # <
greaterThan_Token=58        # >

EndOfFile_Token=59          # 

comma_Token=60              # ,
questionMark_Token=61       # ;

leftParenthesis_Token=62    # (
rightParenthesis_Token=63   # )
leftBracket_Token=64        # [
rightBracket_Token=65       # ]

blockOpening_Token=66       # {
blockClosing_Token=67       # }
lessORequal_Token=68        # <=
greaterORequal_Token=69     # >=

colon_Token=70              # :
assignment_Token=71         # :=
notEqual_Token=72           # !=
period_Token=73             # .


#DESMEUMENES LEKSEIS PROGRAMMATOS

desmeumenes_lexeis=['program' ,'declare','if','else',
                    'while','switchcase',
                    'forcase','incase','default','case',
                    'not','and','or',
                    'function','procedure','call','return','in','inout',
                    'input','print']

                                # Token

program_Token=100               # program
declare_Token=101               # declare

if_Token=102                    # if
else_Token=103                  # else
while_Token=104                 # while

switchcase_Token=105            # switchcase
incase_Token=106                # incase
forcase_Token=107               # forcase
case_Token=108                  # case

default_Token=109               # default
procedure_Token=110             # procedure
function_Token=111              # function
call_Token=112                  # call
return_Token=113                # return

in_Token=114                    # in
inout_Token=115                 # inout

and_Token=116                   # and
or_Token=117                    # or
not_Token=118                   # not

input_Token=119                 # input
print_Token=120                 # print

#Errors

not_Acceptable_Symbol_Error=-1                  # cannot recognise current symbol
digit_letter_Error=-2                           # found letter instead of number
colon_Error=-3                                  # we await :=, but found only :
number_Excepts_Space_Error=-4                   # found a number that is outside our allowed limits
over_30_characters_Error=-5                     # we can only handle up to 30 characters
statements_Open_on_EndOfFile_Error=-6           # we await the closure of brackets


transitionTable=[
        #Status_start -> we await a character
        [Status_start,Status_letter,Status_number,

         plus_Token,minus_Token,multiply_Token, divide_Token,

         equal_Token,Status_lessThan,Status_greaterThan,

         EndOfFile_Token,not_Acceptable_Symbol_Error,

         comma_Token,questionMark_Token,

         leftParenthesis_Token,rightParenthesis_Token,leftBracket_Token,rightBracket_Token,blockOpening_Token,blockClosing_Token,

         Status_start,Status_assignment,

         period_Token,Status_comments],
 
        # we move to the next status, by checking the next symbol

    #Status_letter
        [identifier_Token,Status_letter,Status_letter,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,not_Acceptable_Symbol_Error,
         identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token,identifier_Token],

    #Status_number
        [number_Token,digit_letter_Error, Status_number,number_Token,number_Token,number_Token,
         number_Token,number_Token,number_Token,number_Token,number_Token,not_Acceptable_Symbol_Error,
         number_Token,number_Token,number_Token,number_Token,number_Token,number_Token,number_Token,number_Token,
         number_Token,number_Token,number_Token,number_Token],

    #Status_lessThan
        [lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,
         lessThan_Token,lessORequal_Token,lessThan_Token,notEqual_Token,lessThan_Token,not_Acceptable_Symbol_Error,
         lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token,
         lessThan_Token,lessThan_Token,lessThan_Token,lessThan_Token],

    #Status_greaterThan
        [greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,
         greaterThan_Token,greaterORequal_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,not_Acceptable_Symbol_Error,
         greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token,
         greaterThan_Token,greaterThan_Token,greaterThan_Token,greaterThan_Token],

    #Status_assignment
        [colon_Error,colon_Error,colon_Error,colon_Error,colon_Error,colon_Error,
         colon_Error,assignment_Token,colon_Error,colon_Error,colon_Error,not_Acceptable_Symbol_Error,
         colon_Error,colon_Error,colon_Error,colon_Error,colon_Error,colon_Error,colon_Error,colon_Error,
         colon_Error,colon_Error,colon_Error,colon_Error],

    #Status_comments
        [Status_comments,Status_comments,Status_comments,Status_comments,Status_comments,Status_comments,
         Status_comments,Status_comments,Status_comments,Status_comments,statements_Open_on_EndOfFile_Error,Status_comments,
         Status_comments,Status_comments,Status_comments,Status_comments,Status_comments,Status_comments,Status_comments,Status_comments,
         Status_start,Status_comments,Status_comments,Status_start]

        ]


line=1          # initialize line counter

def characterCheck(character, linecounter):                       # connect current symbol to character_Token

        if (character == ' ' or character == '\t'):
                character_Token = whitecharacter                  # whitecharacter -> ' '

        elif (character in alphabet):
                character_Token = letters                    # letters -> a,b,...,y,z
        elif (character in numbers):
                character_Token = number                     # numbers -> 1,2,...

        elif (character == '+'):
                character_Token = plus                       # plus -> +
        elif (character == '-'):
                character_Token = minus                      # minus -> -
        elif (character == '*'):
                character_Token = multiply                   # multiply -> *
        elif (character == '/'):
                character_Token = divide                     # divide -> /

        elif (character == '='):
                character_Token = equal                      # equal -> =
        elif (character == '<'):
                character_Token = lessThan                   # lessThan -> <
        elif (character == '>'):
                character_Token = greaterThan                # greaterThan -> >

        elif (character == ':'):
                character_Token = colon                      # colon -> :
        elif (character == ','):
                character_Token = comma                      # comma -> ,
        elif (character == ';'):
                character_Token = questionMark               # questionMark -> ?

        elif (character == '('):
                character_Token = leftParenthesis            # leftParenthesis -> (
        elif (character == ')'):
                character_Token = rightParenthesis           # rightParenthesis -> )
        elif (character == '['):
                character_Token = leftBracket                # leftBracket -> [
        elif (character == ']'):
                character_Token = rightBracket               # rightBracket -> ]
        elif (character == '{'):
                character_Token = blockOpening               # blockOpening -> {
        elif (character == '}'):
                character_Token = blockClosing               # blockClosing -> }

        elif (character == '\n'):
                linecounter = linecounter + 1           
                character_Token = lineChange                 # lineChange -> '\n'
        elif (character == ''):                              
                character_Token = EndOfFile                  #EndOfFile returns ''

        elif (character == '.'):
                character_Token = period                     # period -> .
        elif (character == '#'):
                character_Token = hashtag                    # hashtag -> #

        else:
                character_Token = notAcceptableSymbol        # something we dont recognise
        return character_Token


def lex():                                      #token finder (code,token,line) [(int,string,int)]
        
        global line                             #current line
        producedWord=''                         #produced token
        current= Status_start                   #sets situation to start
        
        linecounter= line                       #holds the number of checked lines
        resultlex=[]                            #list for the 3 parts of the token
        
        while(current>=0 and current<=6):                         #check if token is found
                character = file.read(1)                               #reads the next character
                
                character_Token = characterCheck(character,linecounter)          #calls characterCheck
                
                current=transitionTable[current][character_Token]                         #move from last status to next
                
                if(len(producedWord)<30):
                        if(current!=Status_start and current!=Status_comments):         #ignore start and comments
                                        producedWord+=character                                  #add the current character to the produced word
                
                else:
                        current=over_30_characters_Error                                #show error if more than acceptable length


#I have already found the token 
        
        if(current==identifier_Token or current==number_Token or current==lessThan_Token or current==greaterThan_Token ):
                if (character == '\n'):
                        linecounter -= 1
                character=file.seek(file.tell()-1,0)                 #returns last character read on File
                
                producedWord = producedWord[:-1]                        #cuts the +
                
        if(current==identifier_Token):
                if(producedWord in desmeumenes_lexeis):             #check for commited words

                        if(producedWord=='program'):                # program
                                current=program_Token
                        elif(producedWord=='declare'):              # declare
                                current=declare_Token

                        elif (producedWord == 'if'):                # if
                                current = if_Token
                        elif (producedWord == 'else'):              # else
                                current = else_Token

                        elif (producedWord == 'while'):             # while
                                current = while_Token
                        elif (producedWord == 'switchcase'):        # switchcase
                                current = switchcase_Token
                        elif (producedWord == 'forcase'):           # forcase
                                current = forcase_Token
                        elif (producedWord == 'incase'):            # incase
                                current = incase_Token
                        elif (producedWord == 'case'):              # case
                                current = case_Token
                        elif (producedWord == 'default'):           # default
                                current = default_Token

                        elif (producedWord == 'procedure'):         # procedure
                                current = procedure_Token
                        elif (producedWord == 'function'):          # function
                                current = function_Token

                        elif (producedWord == 'call'):              # call
                                current = call_Token
                        elif (producedWord == 'return'):            # return
                                current = return_Token

                        elif (producedWord == 'in'):                # in
                                current = in_Token
                        elif (producedWord == 'inout'):             # inout
                                current = inout_Token

                        elif (producedWord == 'and'):               # and
                                current = and_Token
                        elif (producedWord == 'or'):                # or
                                current = or_Token
                        elif (producedWord == 'not'):               # not
                                current = not_Token

                        elif (producedWord == 'input'):             # input
                                current = input_Token
                        elif (producedWord == 'print'):             # print
                                current = print_Token
        
        
        if (current == number_Token):                               #check for number belonging in [-32767,32767]
                if (producedWord.isdigit() >= pow(2,32)):               #pow(2,32)=2^32
                    current = number_Excepts_Space_Error            #note as error if outside accepted prices
        
        
        #CHECK FOR POSSIBLE ERRORS
        if(current==not_Acceptable_Symbol_Error):
                print("FOUND ERROR: Symbol is not recognised")
        elif(current==digit_letter_Error):
                print("FOUND ERROR: Letter spoted after digit")
        elif(current==colon_Error):
                print("FOUND ERROR: Colon symbol : is not followed by equal symbol = ")
        elif(current==number_Excepts_Space_Error):
                print("FOUND ERROR: The number is outside the space [-(2^32-1),2^32-1]")
        elif(current==statements_Open_on_EndOfFile_Error):
                print("FOUND ERROR: Comments { were opened, but were not closed properly")
        elif(current==over_30_characters_Error):
                print("FOUND ERROR: Current word consists of over 30 digits")
        
        # line 0 _Token, line 1 word, line 2 current line
        
        resultlex.append(current)               # add the 1st part to the list
        resultlex.append(producedWord)          # add the 2nd part to the list
        resultlex.append(linecounter)           # add the 3rd part to the list
        line=linecounter                        # sets starting line
        return resultlex                        #returns the list with the 3 tokens
      

        
# Endiamesos kodikas -> makes quads

global cFile

global listOfTotalQuads		#list with all the progmam produced quads
listOfTotalQuads = []
countQuad = 1			#the identifier number for the quads

                               
def nextQuad():                  #returns next quads number when produced
	
        global countQuad
	
        return countQuad
    
                                                
                                                
def generateQuad(first, second, third, fourth):      #creates next quad and puts nextQuad() number on the lists first position. 
	
        global countQuad                        #We end up with 5 components on the list
        global listOfTotalQuads                 #the list for the total of quads
        list = []                               #list for each quad
	
        list = [nextQuad()]			                #puts the number
        list += [first] + [second] + [third] + [fourth]		#puts the other components
	
        countQuad +=1	                        #increase by 1 next quads number
        listOfTotalQuads += [list] 	        #Puts quad in the end of global listOfTotalQuads
        return list                             #return the quad
    
T_i = 1                                         #initialize T_i
listOfTemporaryVariables = []                        #initialize listOfTemporaryVariables

                                
def newTemp():                          #creates and returns a new temporary variable, on the form of T_1, T_2,.. .
	
        global T_i                      #counter for temporary variables
        global listOfTemporaryVariables      #list for temporary variables
    
        list = ['T_']
        list.append(str(T_i))           #creates string T_i by combining strings 'T_' and 1,2,3,...
        tempVariable="".join(list)      #puts space
        T_i +=1
    
        listOfTemporaryVariables += [tempVariable]           #Saves them in listOfTemporaryVariables
    
        return tempVariable
    
                                
def emptyList():                        #creates empty list of 4 tags
	
        pointerList = []	        #Initilization
    
        return pointerList
    
                                
def makeList(x):                        #creates empty list of 4 tags that contains only x.
    
	listThis = [x]
    
	return listThis
    
def merge(list1, list2):                #creates empty list of 4 tags from the connection of the lists list1, list2.
	
        list=[]
        list += list1 + list2
    
        return list
    
def backPatch(list, z):                  #backPatch checks each quad and adds quad z.'
	
	global listOfTotalQuads           #list is constructed by listOfTotalQuads quads of pointers, last component is blank.
	                               
    
	for i in range(len(list)):                                                              #checks every quad on the list
		for j in range(len(listOfTotalQuads)):                                            #checks every quad on the listOfTotalQuads
			if(list[i]==listOfTotalQuads[j][0] and listOfTotalQuads[j][4]=='_'):        #if '_' on 4rth component, add "z"
				listOfTotalQuads[j][4] = z
				break;	                                                        #to pass second loop faster and enter next i.
	return
    
def syntax_an():                        #we make a function (def) for each rule 
        
        global line
        global lexres
        lexres= lex()                   #we save the first word on lexres
        line = lexres[2]
        
def program():                          # start of program
        
        global line 
        global lexres
        
        if(lexres[0] == program_Token):                         #we identify the expected program word
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == identifier_Token):              #then set the expected identifier
                        id = lexres[1]                      
                        lexres = lex()                           
                        line = lexres[2]

                        block(id,1)                         
                        
                        if(lexres[0] == period_Token):          #then we find the expected . symbol
                                lexres = lex()
                                line = lexres[2]
                        
                                return
                        else:
                                print("FOUND ERROR: Period was not found", line)
                                exit(-1)
                        
                else:
                                print("FOUND ERROR: Can not locate file or program name",line)
                                exit(-1)
        else:
                print("FOUND ERROR: The word 'program' is not found on the start of the program",line)
                exit(-1)    
        
def block(name, flag):                  # initiates program or subprogram

        global line
        global lexres

        if(lexres[0] == blockOpening_Token):                    #we find the [ symbol
                lexres = lex()
                line  =  lexres[2]
                
                declarations()
                
                subprograms()
                
                generateQuad('begin_block',name,'_','_')        #initiates program or subprogram called name
                
                blockstatements()
                
                if(flag==1):
                        generateQuad('halt','_','_','_')        #ends program
                        generateQuad('end_block',name,'_','_')  #ends program or subprogram called name
                        
                if(lexres[0] == blockClosing_Token):            #then we find the expected ] symbol
                        lexres = lex()
                        line = lexres[2]
                        return 
                        
def declarations():                            #in case of declaration token we call it
        
        global lexres 
        global cFile                                 
        
        while(lexres[0] == declare_Token):                      #we find the word declare
                lexres = lex()
                line = lexres[2]
                
                cFile.write("int ")                  
                varlist()
                cFile.write(";\n\t")
                
                if(lexres[0] == questionMark_Token):            #then we find the expected ; symbol
                        lexres = lex()
                        line = lexres[2]
                        
                else:
                        print("FOUND ERROR: questionMark symbol was not found on the end of the varlist", line)
                        exit(-1)
        return
        
def varlist():                                 #in case of multiple identifiers we check the token and call lex()
        
        global lexres
        global cFile                                           
        
        if(lexres[0] == identifier_Token):                      #we set the identifier
                cFile.write(lexres[1])                          
                lexres = lex()
                line = lexres[2]
                
                while(lexres[0] == comma_Token):                #then we find the expected , symbol
                        cFile.write(lexres[1])                  
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == identifier_Token):      #then we set the expected next identifier
                                cFile.write(lexres[1])           
                                lexres = lex()
                                line = lexres[2]
                                
                        else:
                                print("FOUND ERROR: Coma was not found before the identifier or there are 2 or more identifiers not seperated by coma", line)
                                exit(-1)
                                
        return
        
def subprograms():              #in case of multiple subprograms, repeat subprrogram call
        
        global lexres
        
        while(lexres[0] == procedure_Token or lexres[0] == function_Token ):     #we find the word procedure or function
                subprogram()
        return
        
def subprogram():               #in case of subprogram, we call block, in order to initiate it
        
        global lexres
        
        if(lexres[0]==procedure_Token):                                         #we find the word procedure
                lexres=lex()
                line=lexres[2]
                
                if(lexres[0]==identifier_Token):                                #then we set the expected identifier                 
                        id = lexres[1]                  
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == leftParenthesis_Token):                 #then we find the expected ( symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                formalparlist()
                                
                                if(lexres[0] == rightParenthesis_Token):        #the we find the expected ) symbol
                                        lexres = lex()
                                        line = lexres[2]
                                        block(id,0)
                                        
                                        return
                                else:
                                        print("FOUND ERROR: Right parenthesis is not closed properly after the formalparlist",line)
                                        exit(-1)
                        else:
                                print("FOUND ERROR: Left parenthesis is not opened properly before the formalparlist",line)
                                exit(-1)
                else:
                        print("FOUND ERROR: We await the identifier after the function", line)
                        exit(-1)
                        
        elif(lexres[0]== function_Token):
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0]==identifier_Token):                                #we set the expected identifier
                        id = lexres[1]                   
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == leftParenthesis_Token):                 #then we find the expected ( symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                formalparlist()
                                
                                if(lexres[0] == rightParenthesis_Token):        #then we find the expected ) symbol
                                        lexres = lex()
                                        line = lexres[2]
                                        block(id,0)
                                        
                                        return
                                else:
                                        print("FOUND ERROR: Right parenthesis is not closed properly after the formalparlist",line)
                                        exit(-1)
                        else:
                                print("FOUND ERROR: Left parenthesis is not opened properly before the formalparlist",line)
                                exit(-1)
                else:
                        print("FOUND ERROR: We await the identifier after the function ", line)
                        exit(-1)
                        
def formalparlist():            #in case of multiple items, we repeat formalparitem() call
        
        global lexres
        global line
        formalparitem()

        while(lexres[0] == comma_Token):                #we find the , symbol
                lexres  = lex()
                line = lexres[2]
                formalparitem()
                
        return
        
def formalparitem():            #we save the variables, after the words in or inout, as identifiers 
        
        global lexres
        global line

        if(lexres[0] == in_Token):                      #we find the word in
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0]== identifier_Token):       #then we set the expected variables name as identifier
                        lexres = lex()
                        line = lexres[2]
                        
                else:
                        print("FOUND ERROR: We await the variable name after the 'in' ", line)
                        exit(-1)
        elif(lexres[0] == inout_Token):                 #we find word inout
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == identifier_Token):      #then we set the expected variables name as identifier
                        lexres = lex()
                        line = lexres[2]
                        
                else:
                        print("FOUND ERROR: We await the variable name after the 'inout' ", line)
                        exit(-1)                                
                
        return

def statements():               #saves the statement and calls statement() to identify it
        
        global lexres
        global line
        
        if(lexres[0] == blockOpening_Token):                    #we find the [ symbol
                lexres = lex()
                line  =  lexres[2]
                
                statement()
                
                while(lexres[0] == questionMark_Token):         #then we find the expected ? symbol
                        lexres = lex()
                        line = lexres[2]
                         
                        statement()
                        
                if(lexres[0] == blockClosing_Token):            #then we find the expected ] symbol
                        lexres = lex()
                        line = lexres[2]
                        return
                         
                else:
                        print("FOUND ERROR: The block is not closed properly after the statements", line)
                        exit(-1)
        else:
        
                statement()
                
                if(lexres[0] == questionMark_Token):            #we find the expected ? symbol
                        lexres = lex()
                        line = lexres[2]
                        return
                else:
                        print("FOUND ERROR: There is no questionmark after the statement", line)
                        exit(-1)
                        
def blockstatements():             #in case of multiple statements, we repeat statement() call      
        
        global lexres
        global line
        statement()

        while(lexres[0] == questionMark_Token):                 #we find the ? symbol
                lexres = lex()
                line = lexres[2]
                statement()
                
def statement():                #initiate the statements action
        
        global lexres
        
        if(lexres[0]==identifier_Token):                #we find the identifier
                assignmentStat()
        elif(lexres[0]==if_Token):                      #we find the word if
                ifStat()
        elif(lexres[0]==while_Token):                   #we find the word while
                whileStat()
        elif(lexres[0]==switchcase_Token):              #we find the word switchcase
                switchcaseStat()
        elif(lexres[0]==forcase_Token):                 #we find the word forcase
                forcaseStat()
        elif(lexres[0]==incase_Token):                  #we find the word incase
                incaseStat()
        elif(lexres[0]==call_Token):                    #we find the word call
                callStat()
        elif(lexres[0]==return_Token):                  #we find the word return
                returnStat()
        elif(lexres[0]==input_Token):                   #we find the word input
                inputStat()
        elif(lexres[0]==print_Token):                   #we find the word print
                printStat()
        
        return
        
def assignmentStat():           #saves the word after the identifier
        
        global lexres
        global line
        
        if(lexres[0] == identifier_Token):              #we find the identifier
                myid = lexres[1]                       
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == assignment_Token):      #then we find the expected := sumbol
                        lexres = lex()
                        line = lexres[2]
                        
                        Eplace = expression()                 
                        generateQuad(':=', Eplace, '_', myid)
                        
                        return
                else:
                        print("FOUND ERROR: There must be an assignment symbol after the variable symbol.", line)
                        exit(-1) 
        else:
                print("FOUND ERROR: Does not exist",line)
                exit(-1)
                
def ifStat():                   #if case
        
        global lexres
        global line
        
        if(lexres[0] == if_Token):                                      #we find the word if
                lexres= lex()
                line = lexres[2]
                
                if(lexres[0] == leftParenthesis_Token):                 #then we find the expected [ symbol
                        lexres = lex()
                        line = lexres[2]
                         
                        C = condition()                              
                        backPatch(C[0], nextQuad())
                        
                        if(lexres[0]== rightParenthesis_Token):          #then we find the expected ] symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                statements()                 
                                
                                ifList = makeList(nextQuad())           
                                generateQuad('jump', '_', '_', '_')
                                backPatch(C[1], nextQuad())
                                
                                elsepart()
                                
                                backPatch(ifList, nextQuad())          
                                
                                return
                        else:
                                print("FOUND ERROR: Parenthesis is not closed properly after the if case", line)
                                exit(-1)
                else:
                        print("FOUND ERROR: Parenthesis is not opened properly before the if case", line)
                        exit(-1)
        else:
                print("FOUND ERROR: A problem appeared while entering the if case",line)
                exit(-1)
                
def elsepart():                 #else case
        
        global lexres
        global line
        
        if(lexres[0] == else_Token):            #we find the word else
                lexres = lex()
                line = lexres[2]
                
                statements()
                
        return
        
def whileStat():                #while case
        
        global lexres
        global line
        
        if(lexres[0]== while_Token):                                    #we find the word while
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == leftParenthesis_Token):                  #then we find the expected [ symbol
                        lexres = lex()
                        line = lexres[2]
                        
                        Cquad=nextQuad()                     
                        C = condition()
                        backPatch(C[0], nextQuad())
                        
                        if(lexres[0] == rightParenthesis_Token):         #then we find the expected ] symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                statements()
                                
                                generateQuad('jump', '_', '_', Cquad)     #moves to Cquad
                                backPatch(C[1], nextQuad())
                                
                                return
                        else:
                                print("FOUND ERROR: The parenthesis on while case has not closed properly", line)
                                exit(-1)
                else:
                        print("FOUND ERROR: The parenthesis on while case has not opened properly",line)
                        exit(-1)
        else:
                print("FOUND ERROR: A problem appeared on the while case", line)
                exit(-1)
                
def switchcaseStat():                   # checks the conditions after the word case, and executes statements
                                        # when finished leaves from switchcase
        global lexres
        global line
        
        if(lexres[0] == switchcase_Token):                                     #we find the word swithcase
                lexres = lex()
                line = lexres[2]
                
                outList=emptyList()                      
                
                while(lexres[0] == case_Token):                                 #then we find the expected word case
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == leftParenthesis_Token):                 #then we find the expected [ symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                C = condition()
                                backPatch(C[0], nextQuad())                
                                
                                if(lexres[0] == rightParenthesis_Token):        #then we find the expected ] symbol
                                        lexres = lex()
                                        line = lexres[2]
                                        
                                        statements()                 
                                        
                                        outJump = makeList(nextQuad())             
                                        generateQuad('jump', '_', '_', '_')
                                        outList = merge(outList, outJump)
                                        backPatch(C[1], nextQuad())
                                        
                                        #return
                                        
                                else:
                                        print("FOUND ERROR: Right parenthesis was not found on forcase", line)
                                        exit(-1)
                        else:
                                print("FOUND ERROR: Left parenthesis was not found on forcase", line)
                                exit(-1)
                                
                if(lexres[0] == default_Token):                                 #we find the word default
                        lexres = lex()
                        line = lexres[2]
                        
                        statements()                
                        
                        backPatch(outList, nextQuad())          
                else:
                        print("FOUND ERROR: Default has not been started properly on forecase", line)
                        exit(-1)
        else:
                print("FOUND ERROR: Forcase does not start properly", line)
                exit(-1)
                
def forcaseStat():                      # checks the conditions after the word case, and executes statements
                                        # when finished returns to the start of forcaseStat
        global lexres
        global line

        if(lexres[0] == forcase_Token):                                         #we find the word forcase
                lexres = lex()
                line = lexres[2]
                
                quad=nextQuad()                                                                    
                
                while(lexres[0] == case_Token):                                 #then we find the expected word case
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == leftParenthesis_Token):                 #then we find the expected [ symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                C = condition()                          
                                backPatch(C[0], nextQuad())
                                
                                if(lexres[0] == rightParenthesis_Token):        #then we find the expected ] symbol
                                        lexres = lex()
                                        line = lexres[2]
                                        
                                        statements()                 
                                        
                                        generateQuad('jump','_','_',quad)       #moves to quad
                                        backPatch(C[1], nextQuad())
                                       
                                        
                                else:
                                        print("FOUND ERROR: Right parenthesis was not found on forcase", line)
                                        exit(-1)
                        else:
                                print("FOUND ERROR: Left parenthesis was not found on forcase", line)
                                exit(-1)
                                
                if(lexres[0] == default_Token):                                 #we find the word default
                        lexres = lex()
                        line = lexres[2]
                        
                        statements()
                else:
                        print("FOUND ERROR: Default has not been started properly on forecase", line)
                        exit(-1)
        else:
                print("FOUND ERROR: Forcase does not start properly", line)
                exit(-1)
                
def incaseStat():               # checks the conditions after the word case, and executes statements
                                # when finished, if at least on statement was executed, returns to the start of incaseStat, else leaves  
        global lexres
        global line
        
        if(lexres[0] == incase_Token):                                          #we find the word incase
                lexres = lex()
                line = lexres[2]
                
                quad=nextQuad()                      
                w = newTemp()
                generateQuad(':=','0','_',w)
                
                while(lexres[0] == case_Token):                                 #then we find the word case
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == leftParenthesis_Token):                 #then we find the expected [ symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                C = condition()                     
                                backPatch(C[0], nextQuad())
                                
                                if(lexres[0] == rightParenthesis_Token):        #then we find the expected ] symbol
                                        lexres = lex()
                                        line = lexres[2]
                                        
                                        statements()                 
                                        
                                        generateQuad(':=','1','_',w)              
                                        backPatch(C[1], nextQuad())
                                        
                                        #return
                                        
                                else:
                                        print("FOUND ERROR: Right parenthesis was not found on forcase", line)
                                        exit(-1)
                        else:
                                print("FOUND ERROR: Left parenthesis was not found on forcase", line)
                                exit(-1)
                                
                generateQuad('=',w,'1',quad)                                   
                
        else:
                print("FOUND ERROR: Forcase does not start properly", line)
                exit(-1)
                
def returnStat():               #returns the text inside the parenthesis
        
        global lexres
        global line
        
        if(lexres[0] == return_Token):                                  #we find the word return
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == leftParenthesis_Token):                 #then we find the expected [ symbol
                        lexres = lex()
                        line = lexres[2]
                        
                        Eplace = expression()                        
                        generateQuad('retv', Eplace, '_', '_')
                        
                        if(lexres[0] == rightParenthesis_Token):        #then we find the expected ] symbol
                                lexres = lex()
                                line = lexres[2]
                                return
                        else:
                                print("FOUND ERROR: The parenthesis does not close properly on return",line)
                                exit(-1)
                else:
                        print("FOUND ERROR: The parenthesis does not close properly on return", line)
                        exit(-1)
                        
def callStat():                 #calls the identifier
        
        global lexres
        global line
        
        if(lexres[0] == call_Token):                                            #we find the word call
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == identifier_Token):                              #then we set the expected identifier
                        idName = lexres[1]               
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == leftParenthesis_Token):                 #then we find the expected [ symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                actualparlist()              
                                generateQuad('call', idName, '_', '_')          #we initiate idName function  
                                
                                if(lexres[0] == rightParenthesis_Token):        #then we find the expected ] symbol
                                        lexres = lex()
                                        line = lexres[2]
                                        return
                                else:
                                        print("FOUND ERROR: The parenthesis does not properly close on call",line)
                                        exit(-1)
                        else:
                                print("FOUND ERROR: The parenthesis does not properly open on call", line)
                                exit(-1)
                                
                else:
                        print("FOUND ERROR: Identifier was not found on call", line)
                        exit(-1)
        else:
                print("FOUND ERROR: Call does not properly start",line)
                exit(-1)
                
        return
        
def printStat():                #prints the text in parenthesis
        
        global lexres
        global line
        
        if(lexres[0] == print_Token):                                   #we find the word print
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == leftParenthesis_Token):                 #then we find the expected [ symbol
                        lexres = lex()
                        line = lexres[2]
                        
                        Eplace = expression()                      
                        generateQuad('out', Eplace, '_', '_')
                        
                        if(lexres[0] == rightParenthesis_Token):        #then we find the expected ] symbol
                                lexres = lex()
                                line = lexres[2]
                        
                        else:
                                print("FOUND ERROR: The parenthesis does not properly close on print",line)
                                exit(-1)
                else:
                        print("FOUND ERROR: The parenthesis does not properly open on print", line)
                        exit(-1)
        else:
                print("FOUND ERROR: The print does not properly start", line)
                exit(-1)
        return
        
def inputStat():                #saves the identifier in parenthesis
        
        global lexres
        global line
        
        if(lexres[0] == input_Token):                                           #we find the word input
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == leftParenthesis_Token):                         #then we find the expected [ symbol
                        lexres = lex()
                        line = lexres[2]
                        
                        if(lexres[0] == identifier_Token):                      #then we set the expected identifier
                                myid = lexres[1]                         
                                generateQuad('inp',myid,'_','_')
                                lexres = lex()
                                line = lexres[2]
                                                                         
                                if(lexres[0] == rightParenthesis_Token):        #then we find the expected ] symbol
                                        lexres = lex()
                                        line = lexres[2]
                                        return
                                        
                                else:
                                        print("FOUND ERROR: The parenthesis does not properly close on input",line)
                                        exit(-1)
                        else:
                                print("FOUND ERROR: Identifier was not found on input",line)
                                exit(-1)
                else:
                        print("FOUND ERROR: The parenthesis does not properly open on input", line)
                        exit(-1)
        else:
                print("FOUND ERROR: The input does not properly start", line)
                exit(-1)
                
def actualparlist():            #in case of multiple items we repeat actualparitem call
        
        global lexres
        global line 
         
        actualparitem()
        
        while(lexres[0] == comma_Token):        #we find the , symbol
                lexres  = lex()
                line = lexres[2]
                
                actualparitem()
                
        return
        
def actualparitem():            #sends the name and value of the identifier
        
        global lexres
        global line                
        
        if(lexres[0] == in_Token):                      #we find the word in
                lexres = lex()
                line = lexres[2]
                
                thisExpression = expression()                    
                generateQuad('par', thisExpression, 'CV', '_')          #sends thisExpression as a price (CV)
                
        elif(lexres[0] == inout_Token):                 #we find the word inout
                lexres = lex()
                line = lexres[2]
                
                if(lexres[0] == identifier_Token):      #then we set the expected identifier
                        name = lexres[1]                 
                        
                        lexres = lex()
                        line = lexres[2]
                        
                        generateQuad('par', name, 'REF', '_')           #sends name as a reference (REF)
                        
                else:
                        print("FOUND ERROR: We await the variable name after the 'inout' ", line)
                        exit(-1)                                    
                
        return          
        
def condition():                #checks the validity of conditions
        
        global lexres
        global line
        
        Ctrue = []                   
        Cfalse = []
        BT1 = boolterm()
        Ctrue = BT1[0]
        Cfalse = BT1[1]
        
        while(lexres[0]==or_Token):                     #we find the word or
                lexres=lex()
                line = lexres[2]
                
                backPatch(Cfalse, nextQuad())            
                
                BT2 = boolterm()
                
                Ctrue = merge(Ctrue, BT2[0])
                Cfalse = BT2[1]
                
        return Ctrue, Cfalse
        
def boolterm():                 #for multiple validity checks, we repeat boolfactor() call
        
        global lexres
        global line
        
        BTtrue = []                      
        BTfalse = []
        
        BF1 = boolfactor()
        BTtrue = BF1[0]
        BTfalse = BF1[1]
        
        while(lexres[0]==and_Token):                    #we find the word and
                lexres=lex()
                line = lexres[2]
                
                backPatch(BTtrue, nextQuad())            
                
                BF2 = boolfactor()
                
                BTfalse = merge(BTfalse, BF2[1])
                BTtrue = BF2[0]
        return BTtrue, BTfalse
        
def boolfactor():
        
        global lexres
        global line
        
        BFtrue = []                     
        BFfalse = []   
        
        if(lexres[0]==not_Token):                               #we find the word not
                lexres=lex()
                line = lexres[2]
                
                if(lexres[0]==leftBracket_Token):               #then we find the expected [ symbol
                        lexres = lex()
                        line = lexres[2]
                        
                        C = condition()                  
                        
                        if(lexres[0]==rightBracket_Token):      #then we find the expected ] symbol
                                lexres = lex()
                                line = lexres[2]
                                
                                BFtrue = C[1]                    
                                BFfalse = C[0]        
                                
                        else:
                                print("FOUND ERROR: The bracket does not properly close on the boolfactor case ",line)
                                exit(-1)
                else:
                        print("FOUND ERROR: We await a bracket opening after the not on boolfactor", line)
                        exit(-1)
        elif(lexres[0]==leftBracket_Token):                     #we find the [ symbol
                lexres = lex()
                line = lexres[2]
                
                C = condition()                             
                
                if(lexres[0]==rightBracket_Token):              #then we find the expected ] symbol
                        lexres = lex()
                        line = lexres[2]
                        
                        BFtrue = C[0]                        
                        BFfalse = C[1]
                        
                else:
                        print("FOUND ERROR: The bracket does not properly close on the boolfactor case", line)
                        exit(-1)
        else:
                
                Eplace1 = expression()                  
                
                relop = relationalOperation()           #moves to new space if conditions apply
                
                Eplace2 = expression()
                
                BFtrue=makeList(nextQuad())
                generateQuad(relop, Eplace1, Eplace2, '_')
                BFfalse=makeList(nextQuad())
                generateQuad('jump', '_', '_', '_')
                
        return BFtrue, BFfalse    
        
def expression():               #in case of plus or minus, repeat addOperation() call
        
        global lexres
        global line
        
        optionalSign()
        
        T1place = term()                 
        
        while(lexres[0]==plus_Token or lexres[0]==minus_Token):                 #we find the + or - symbol
                plusOrMinus = addOperation()
                
                T2place = term()             
                
                w = newTemp()
                generateQuad(plusOrMinus, T1place, T2place, w)
                T1place = w
                
        Eplace = T1place
        return Eplace              
        
def term():                     #in case of multiply or divide, repeat calladdOperation() call
        
        global lexres
        global line
        
        F1place = factor()               
        
        while(lexres[0]==multiply_Token or lexres[0]==divide_Token):            #we find the * or / symbol
                mulOrDiv = multiplyOperation()
                
                F2place = factor()                           
                
                w=newTemp()
                generateQuad(mulOrDiv, F1place, F2place, w)
                F1place = w
        Tplace =F1place
        return Tplace 
        
def factor():
        
        global lexres
        global line
        
        if(lexres[0]==number_Token):                            #we set the number
                fact = lexres[1]             
                lexres = lex()
                line = lexres[2]
                
        elif(lexres[0]==leftParenthesis_Token):                 #we find the [ symbol
                lexres = lex()
                line = lexres[2]
                
                Eplace = expression()                       
                fact = Eplace
                
                if(lexres[0]==rightParenthesis_Token):          #then we find the expected ] symbol
                        lexres = lex()
                        line = lexres[2]
                
                else:
                        print("FOUND ERROR: We await the right parenthesis ')' after the expression on FACTOR ",line)
                        exit(-1)
                        
        elif(lexres[0]==identifier_Token):                      #we set the identifier 
                fact_temp = lexres[1]                
                lexres = lex()
                line = lexres[2]
                fact = idtail()               
                
        else:
                print("FOUND ERROR: We await constant or expression or variable on factor",line)
                exit(-1)
                
        return fact                                 
        
def idtail():                        
                
        global lexres
        global line
        name = lexres[1]

        if(lexres[0] == leftParenthesis_Token ):                #we find the [ symbol
                lexres = lex()
                name = lexres[1]
                line = lexres[2]
                        
                actualparlist()                 
                w=newTemp()                                  
                generateQuad('par', w, 'RET', '_')           #sends w as a function's price (RET)     
                generateQuad('call', name, '_', '_')
                        
                if(lexres[0]==rightParenthesis_Token):          #then we find the expected ] symbol
                        lexres = lex()
                        line = lexres[2]
                                
                        return w                            
                else:
                        print("FOUND ERROR: We want the right parenthesis ')' after the actualparlist on IDTAIL ",line)
                        exit(-1)
                                
        else:                                                
                return name               
                        
def optionalSign():
        
        global lexres
        global line
        
        if(lexres[0] == plus_Token or lexres[0] == minus_Token):        #we find the + or - symbol
        
                addOperation()
        
        return                
        
def relationalOperation():              #identifies the operation

        global lexres 
        global line
        
        if(lexres[0]==equal_Token):                     #we find the = symbol         
                relop = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        elif(lexres[0]==lessThan_Token):                #we find the < symbol    
                relop = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        elif(lexres[0]==lessORequal_Token):             #we find the <= symbol  
                relop = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        elif(lexres[0]==notEqual_Token):                #we find the <> symbol
                relop = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        elif(lexres[0]== greaterThan_Token):            #we find the > symbol         
                relop = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        elif(lexres[0]==greaterORequal_Token):          #we find the >= symbol
                relop = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        else:
                print("FOUND ERROR:  =  h < h < =  h <> h > =  h >    is missing ",line)
                exit(-1)
        return relop                               
        
def addOperation():                             # +

        global lexres 
        global line
        
        if(lexres[0]==plus_Token):              #we find the + symbol                  
                addOp = lexres[1]            
                lexres = lex()
                line = lexres[2]
                
        elif(lexres[0]==minus_Token):           #we find the - symbol
                addOp = lexres[1]            
                lexres = lex()
                line = lexres[2]
                
        return addOp                        
        
def multiplyOperation():                        # *

        global lexres 
        global line
        
        if (lexres[0] == multiply_Token):         #we find the * symbol  
                oper = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        elif (lexres[0] == divide_Token):         #we find the / symbol    
                oper = lexres[1]            
                lexres = lex()
                line = lexres[2]
        
        return oper                          
        
                

def intCode(intF):                              #Write listOfTotalQuads at intFile.int                           

	for i in range(len(listOfTotalQuads)):
		quad = listOfTotalQuads[i]
		intF.write(str(quad[0]))
		intF.write(":  ")
		intF.write(str(quad[1]))
		intF.write("  ")
		intF.write(str(quad[2]))
		intF.write("  ")
		intF.write(str(quad[3]))
		intF.write("  ")
		intF.write(str(quad[4]))
		intF.write("\n")
        
        
def cCode():                                #the text for the c file              

	global listOfTemporaryVariables
	
	if(len(listOfTemporaryVariables)!=0):
		cFile.write("int ")
	
	for i in range(len(listOfTemporaryVariables)):          #Temp_i variables.
		cFile.write(listOfTemporaryVariables[i])

		if(len(listOfTemporaryVariables) == i+1):
			cFile.write(";\n\n\t")
		else:
			cFile.write(",")
            
	for j in range(len(listOfTotalQuads)):
		if(listOfTotalQuads[j][1] == 'begin_block'):
			cFile.write("L_"+str(j+1)+":\n\t")
		elif(listOfTotalQuads[j][1] == ":="):
			cFile.write("L_"+str(j+1)+": "+ listOfTotalQuads[j][4]+"="+listOfTotalQuads[j][2]+";\n\t")
		elif(listOfTotalQuads[j][1] == "+"):
			cFile.write("L_"+str(j+1)+": "+ listOfTotalQuads[j][4]+"="+listOfTotalQuads[j][2]+"+"+listOfTotalQuads[j][3]+";\n\t")
		elif(listOfTotalQuads[j][1] == "-"):
			cFile.write("L_"+str(j+1)+": "+ listOfTotalQuads[j][4]+"="+listOfTotalQuads[j][2]+"-"+listOfTotalQuads[j][3]+";\n\t")
		elif(listOfTotalQuads[j][1] == "*"):
			cFile.write("L_"+str(j+1)+": "+ listOfTotalQuads[j][4]+"="+listOfTotalQuads[j][2]+"*"+listOfTotalQuads[j][3]+";\n\t")
		elif(listOfTotalQuads[j][1] == "/"):
			cFile.write("L_"+str(j+1)+": "+ listOfTotalQuads[j][4]+"="+listOfTotalQuads[j][2]+"/"+listOfTotalQuads[j][3]+";\n\t")
		elif(listOfTotalQuads[j][1] == "jump"):
			cFile.write("L_"+str(j+1)+": "+"goto L_"+str(listOfTotalQuads[j][4])+ ";\n\t")
		elif(listOfTotalQuads[j][1] == "<"):
			cFile.write("L_"+str(j+1)+": "+"if ("+listOfTotalQuads[j][2]+"<"+listOfTotalQuads[j][3]+") goto L_"+str(listOfTotalQuads[j][4])+";\n\t")
		elif(listOfTotalQuads[j][1] == ">"):
			cFile.write("L_"+str(j+1)+": "+"if ("+listOfTotalQuads[j][2]+">"+listOfTotalQuads[j][3]+") goto L_"+str(listOfTotalQuads[j][4])+";\n\t")
		elif(listOfTotalQuads[j][1] == ">="):
			cFile.write("L_"+str(j+1)+": "+"if ("+listOfTotalQuads[j][2]+">="+listOfTotalQuads[j][3]+") goto L_"+str(listOfTotalQuads[j][4])+";\n\t")
		elif(listOfTotalQuads[j][1] == "<="):
			cFile.write("L_"+str(j+1)+": "+"if ("+listOfTotalQuads[j][2]+"<="+listOfTotalQuads[j][3]+") goto L_"+str(listOfTotalQuads[j][4])+";\n\t")
		elif(listOfTotalQuads[j][1] == "<>"):
			cFile.write("L_"+str(j+1)+": "+"if ("+str(listOfTotalQuads[j][2])+"!="+str(listOfTotalQuads[j][3])+") goto L_"+str(listOfTotalQuads[j][4])+";\n\t")
		elif(listOfTotalQuads[j][1] == "="):
			cFile.write("L_"+str(j+1)+": "+"if ("+listOfTotalQuads[j][2]+"=="+listOfTotalQuads[j][3]+") goto L_"+str(listOfTotalQuads[j][4])+";\n\t")
		elif(listOfTotalQuads[j][1] == "out"): #print to apotelesma tou expression.
			cFile.write("L_"+str(j+1)+": "+"printf(\""+listOfTotalQuads[j][2]+"= %d\", "+listOfTotalQuads[j][2]+");\n\t")
		elif(listOfTotalQuads[j][1] == 'halt'):
			cFile.write("L_"+str(j+1)+": {}\n\t")

def files():                                                 

        global cFile            #intFile.int & cFile.c

        intFile = open('intFile.int', 'w+')             #Open files to write
        cFile = open('cFile.c', 'w+')
        
        cFile.write("int main(){\n\t")
        
        syntax_an()                             #we activate the syntax method
        program()
        print("Telos syntax")
        intCode(intFile)
        cCode()
        
        cFile.write("\n}")
        
        cFile.close()                           #Close open file
        intFile.close()
files()

def printListOfTotalQuads():                     #Prints listOfTotalQuads               

	for i in range(len(listOfTotalQuads)):
		print (str(listOfTotalQuads[i][0])+" "+str(listOfTotalQuads[i][1])+" "+str(listOfTotalQuads[i][2])+" "+str(listOfTotalQuads[i][3])+" "+str(listOfTotalQuads[i][4]))
printListOfTotalQuads()

print("No problems appeared")