#reading movies.csv file and putting datas into a list.
import csv #Importing module to process a csv file
with open("movies.csv") as f: #opening csv file
             lines=[line.split(", ") for line in f] #splitting and putting the datas that are in movies.csv
             x=len(lines)#---------------------------------------------
             for i in range(0,x):                   #The last film of a line has '\n' character.
                          k=len(lines[i])           #That was making problem about reading datas
                          for j in range(0,k):   #from csv file truely. This code solve this problem.
                                       lines[i][j]=lines[i][j].strip()#-------------------------
temp = lines[0][0]
temp=temp[3:len(temp)]
lines[0][0]=temp
#reading movies.csv file and putting datas into a list.

#function that using to separate titles in menu
def reagent():
             print ('-------------------------------------------------------------------------------')
#function that using to separate titles in menu

#function for task 1    
def task1():
             global control#variable for actor's control
             control=False#initialization of control
             actor=input('Enter an actor or actress name (ex: Edward Norton): ' ) #taking an input from user
             if any(ch.isdigit() for ch in actor)==False: #--------------------------------------------------------------------#if user enter an input that has not digit (because if input has a digit, .title() method doesn't work)
                          if actor.istitle()==False: #dynamization of user's input                                                and input is not title form, program convert input to title form (brad pitt -------> Brad Pitt)
                                       actor=actor.title()#--------------------------------------------------------------------------------
             global savetask1#variable for writing task 1 results to output file.
             global givenActor1#variable for writing task 1 results to output file.
             savetask1=list()#initialization of savetask1
             givenActor1=actor#initialization of givenActor1
             actorNumbers=len(lines) #-------------------------------------------------------------------------------------------
             for i in range(0,actorNumbers):                      #firstly program scans to determine
                          if actor == lines[i][0]:                      #if the entered actor is there 
                                       control=True                                        #and then, program scans list of movies. 
             if control==True:                                                #if user's input is there, program enters that line
                          print("All movies of " +actor+": ")
                          for i in range(0,actorNumbers):                      #firstly, program scans list of movies. 
                                       if actor == lines[i][0]:                       #if user's input is there, program enters that line
                                                    actorNamePosition=lines[i].index(actor) #and scans that line according to line's length.
                                                    filmNumber=len(lines[i])                       # Finally, prints the films to the screen and
                                                    for y in range(actorNamePosition+1,filmNumber): #puts the film into a list for saving process
                                                                 print(lines[i][y])
                                                                 savetask1.append(lines[i][y]) #result puts into savetask1 for using in save process
             else:                                                            #if user's input is not there. Program gives error message.
                          print('Entered actor or actress not found.')
                          #---------------------------------------------------------------------------------------------------
#function for task 1

#function for task 2                              
def task2():
             global control#variable for actor's control
             control=False#initialization of control
             actor=input('Enter an actor or actress name (ex: Edward Norton): ' )#taking an input from user
             if any(ch.isdigit() for ch in actor)==False: #--------------------------------------------------------------------#if user enter an input that has not digit (because if input has a digit, .title() method doesn't work)
                          if actor.istitle()==False:#dynamization of user's input                                                and input is not title form, program convert input to title form (brad pitt -------> Brad Pitt)
                                       actor=actor.title()#--------------------------------------------------------------------------------
             global savetask2#variable for writing task 2 results to output file.
             savetask2=list()#initialization of savetask1
             global givenActor2#variable for writing task 2 results to output file.
             givenActor2=actor#initialization of givenActor2
             actorNumbers=len(lines)#------------------------------------------------------------------------------------------------------------
             for i in range(0,actorNumbers):                      
                          if actor == lines[i][0]:                      #firstly program scans to determine
                                       control=True                         #if the entered actor is there                 
             if control==True:
                          print("All the actors or actresses with whom  " +actor+" has acted: ")
                          for i in range(0,actorNumbers):                     #and then, program scans list of movies.
                                       if(actor.title() == lines[i][0]):      #if user's input is there, program enters that line
                                                    actorNamePosition=lines[i].index(actor) #and find the actor's location on the line
                                                    filmNumber=len(lines[i])               #and scans that line according to line's length.
                                                    for y in range(actorNamePosition+1,filmNumber):     #this for begins 'actorNamePosition+1' because first data is actor name
                                                                 temp=lines[i][y]                       #after that program keeps the film that in line
                                                                 for k in range(0, actorNumbers):       #and scans again all actor's line
                                                                              filmNumber=len(lines[k])  #if first film that kept by program and other film are same.
                                                                              for j in range(0,filmNumber):          #program prints other film's actor so, first item that in its line
                                                                                           if(temp ==lines[k][j] and actor!=lines[k][0]): #'actor!=lines[k][0]' this code for preventing the program rewriting the entered actor's name again.
                                                                                                        print(lines[k][0])
                                                                                                        savetask2.append(lines[k][0]) #result puts into savetask2 for using in save process.
             else:
                          print('Entered actor or actress not found.')         #if user's input is not there. Program gives error message.
                                       #---------------------------------------------------------------------------------------------------------------------------                                                          
#function for task 2

#function for task 3
def task3():
             global control#variable for actor's control
             control=False#initialization of control
             global savetask3#variable for writing task 2 results to output file.
             global givenFilm3#variable for writing task 2 results to output file.
             savetask3=list()#initialization of savetask1
             film=input('Enter a movie (ex: Se7en): ')#taking an input from user
             if any(ch.isdigit() for ch in film)==False:#--------------------------------------------------------------------#if user enter an input that has not digit (because if input has a digit, .title() method doesn't work)
                          if film.istitle()==False:#dynamization of user's input                                                and input is not title form, program convert input to title form (fight club -------> Fight Club)
                                       film=film.title()#--------------------------------------------------------------------------------
             givenFilm3=film#initialization of givenActor3
             filmNumbers=len(lines)#------------------------------------Film Controlling part-----------------------------
             for i in range(0,filmNumbers):
                          filmLength=len(lines[i])                            #program scans the list, if entered film is there
                          for k in range(1,filmLength):                         #control variable becomes True.
                                       if film==lines[i][k]:
                                                    control=True#------------------------------------Film Controlling part-----------------------------
             if control==True:                                       #------------------------if control variable is true-----------------------------------------------------
                          print("All actors and actresses in " +film+": ")
                          for i in range(0,filmNumbers):         #firstly, program scans list of movies.
                                       filmLength=len(lines[i])#if user's input is anywhere of the list, program enters that line
                                       for k in range(1,filmLength):          #and prints the actor of film to the screen
                                                    if film==lines[i][k]:     #finally, result puts into savetask3 for using in save process.
                                                                 print(lines[i][0])
                                                                 savetask3.append(lines[i][0]) 
                                                      #------------------------if control variable is true-----------------------------------------------------
             else:                     #-----------------------------if control variable is false---------------------------
                          print('Entered film not found. Please enter again') #program gives error message 
                                       #-----------------------------if control variable is false---------------------------
#function for task 3             
                          
                          
#function for initializing of task 4,5 and 6
def setTasksFirstMovie():
             control=False#variable for control the films 
             global firstFilm#variable for using in function of task 4,5 and 6
             global actorFirstFilm#variable for using in function of task 4,5 and 6
             actorFirstFilm=set()#initialization of actorFirstFilm
             firstFilm=input('Enter first movie (ex: Se7en): ')#taking an input from user
             if any(ch.isdigit() for ch in firstFilm)==False:#--------------------------------------------------------------------#if user enter an input that has not digit (because if input has a digit, .title() method doesn't work)
                          if firstFilm.istitle()==False:#dynamization of user's input                                                and input is not title form, program convert input to title form (fight club -------> Fight Club)
                                        firstFilm=firstFilm.title()#--------------------------------------------------------------------------------
             filmNumbers=len(lines)#------------------------------------Film Controlling part-----------------------------
             for i in range(0,filmNumbers):
                          filmLength=len(lines[i])                            #program scans the list, if entered film is there
                          for k in range(1,filmLength):                         #control variable becomes True.
                                       if firstFilm==lines[i][k]:
                                                    control=True#------------------------------------Film Controlling part-----------------------------
             if control==True:                                       #------------------------if control variable is true-----------------------------------------------------
                          for i in range(0,filmNumbers):                        #firstly, program scans list of movies.   
                                       filmLength=len(lines[i])               #if user's input is anywhere of the list, program enters that line
                                       for k in range(1,filmLength):              #and puts the actor of film into list
                                                    if firstFilm==lines[i][k]:
                                                                 actorFirstFilm.add(lines[i][0]) #------------------------if control variable is true---------------------------
             else:                     #-----------------------------if control variable is false---------------------------
                          print('Entered film not found. Please enter again') #program gives error message 
                          setTasksFirstMovie()                                             #and call the same function again
                                       #-----------------------------if control variable is false---------------------------
             
def setTasksSecondMovie():
             control=False#variable for control the films 
             global secondFilm  #variable for using in function of task 4,5 and 6
             global actorSecondFilm#variable for using in function of task 4,5 and 6
             actorSecondFilm=set()#initialization of actorFirstFilm
             secondFilm=input('Enter second movie (ex: Se7en): ')#taking an input from user
             if any(ch.isdigit() for ch in secondFilm)==False:#--------------------------------------------------------------------#if user enter an input that has not digit (because if input has a digit, .title() method doesn't work)
                          if secondFilm.istitle()==False:#dynamization of user's input                                                and input is not title form, program convert input to title form (fight club -------> Fight Club)
                                        secondFilm=secondFilm.title()#--------------------------------------------------------------------------------
             filmNumbers=len(lines)#------------------------------------Film Controlling part-----------------------------
             for i in range(0,filmNumbers):
                          filmLength=len(lines[i])                            #program scans the list, if entered film is there
                          for k in range(1,filmLength):                                    #control variable becomes True.
                                       if secondFilm==lines[i][k]:
                                                    control=True#------------------------------------Film Controlling part-----------------------------
             if control==True:                                   #------------------------if control variable is true-----------------------------------------------------
                          for i in range(0,filmNumbers):                      #firstly, program scans list of movies.  
                                       filmLength=len(lines[i])             #if user's input is anywhere of the list, program enters that line
                                       for k in range(1,filmLength):                       #and puts the actor of film into list
                                                    if secondFilm==lines[i][k]:
                                                                 actorSecondFilm.add(lines[i][0])#------------------------if control variable is true---------------------------
             else:                     #-----------------------------if control variable is false---------------------------
                       print('Entered film not found. Please enter again')#program gives error message
                       setTasksSecondMovie()                                         #and call the same function again
                                        #-----------------------------if control variable is false---------------------------
#function for initializing of task 4,5 and 6

#function for task 4               
def task4():
             global savetask4#variable for writing task 4 results to output file.
             global givenFilm4First#variable for writing task 4 results to output file.
             global givenFilm4Second#variable for writing task 4 results to output file.
             setTasksFirstMovie()#calling the function
             setTasksSecondMovie()#calling the function
             givenFilm4First=firstFilm#initialization of givenFilm4First
             givenFilm4Second=secondFilm#initialization of givenFilm4Second
             actorsOfTwoMovies=set()#initialization of actorsOfTwoMovies
             actorsOfTwoMovies=actorSecondFilm.union(actorFirstFilm)#using union method for union of actors of two movies
             savetask4=list(actorsOfTwoMovies)#initialization of savetask4
             print("All actors and actresses in " +firstFilm+" and " +secondFilm+": ")
             for item in actorsOfTwoMovies:#printing result to the screen
                          print(item)
#function for task 4

#function for task 5             
def task5():
             global savetask5#variable for writing task 5 results to output file.
             global givenFilm5First#variable for writing task 5 results to output file.
             global givenFilm5Second#variable for writing task 5 results to output file.
             setTasksFirstMovie()#calling the function
             setTasksSecondMovie()#calling the function
             givenFilm5First=firstFilm#initialization of givenFilm5First
             givenFilm5Second=secondFilm#initialization of givenFilm5Second
             actorsOfTwoMovies=set()#initialization of actorsOfTwoMovies
             actorsOfTwoMovies=actorSecondFilm.intersection(actorFirstFilm)#using intersection method for intersection of actors of two movies
             savetask5=list(actorsOfTwoMovies)#initialization of savetask5
             print("Common actors and actresses in " +firstFilm+" and " +secondFilm+": ")
             for item in actorsOfTwoMovies:#printing result to the screen
                          print(item)
             if len(savetask4) == 0:#condition that intersection of actors of two movies is empty
                          print('There is no any common actor between two movies.')
#function for task 5             

#function for task 6        
def task6():
             global savetask6#variable for writing task 6 results to output file.
             global givenFilm6First#variable for writing task 6 results to output file.
             global givenFilm6Second#variable for writing task 6 results to output file.
             setTasksFirstMovie()#calling the function
             setTasksSecondMovie()#calling the function
             givenFilm6First=firstFilm#initialization of givenFilm6First
             givenFilm6Second=secondFilm#initialization of givenFilm6Second
             difference1=set()#initialization of difference1. a difference b (A-B)
             difference2=set()#initialization of difference2. b difference a (B-A)
             actorsOfTwoMovies=set()#initialization of actorsOfTwoMovies
             difference1=actorSecondFilm.difference(actorFirstFilm)#using difference method for symmetric difference of first movie actors from second movie actors
             difference2=actorFirstFilm.difference(actorSecondFilm)#using difference method for symmetric difference of second movie actors from first movie actors
             actorsOfTwoMovies=difference1.union(difference2)#union of difference1 and difference2
             savetask6=list(actorsOfTwoMovies)#initialization of savetask6
             print("all actors and actresses in either of the movies " +firstFilm+" and " +secondFilm+": ")
             for item in actorsOfTwoMovies:#printing result to the screen
                          print(item)
#function for task 6

#function for task 7
def task7():
             save=open("savefile.txt", "w")#initalization of writing a file method.
             save.write("-----------------------------------------------------------------\n")
             save.write("1. List all movies of given actor or actress.\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("Given actor or actress's name: ")
             save.write(givenActor1)
             save.write("\n")
             save.write("Result:\n")
             k=len(savetask1)
             for i in range(0,k):
                          temp=savetask1[i]
                          save.write(temp)
                          save.write("\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("2. Given an actor or actress's name, find all the actors or actresses with whom he/she has acted.\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("Given actor or actress's name: ")
             save.write(givenActor2)
             save.write("\n")
             save.write("Result:\n")
             k=len(savetask2)
             for i in range(0,k):
                          temp=savetask2[i]
                          save.write(temp)
                          save.write("\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("3. List all actors and actresses in a movie.\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("Given movie: ")
             save.write(givenFilm3)
             save.write("\n")
             save.write("Result:\n")
             k=len(savetask2)
             for i in range(0,k):
                          temp=savetask2[i]
                          save.write(temp)
                          save.write("\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("4. List all actors and actresses in two movies.\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("Given first movie: ")
             save.write(givenFilm4First)
             save.write("\n")
             save.write("Given second movie: ")
             save.write(givenFilm4Second)
             save.write("\n")
             save.write("Result:\n")
             k=len(savetask4)
             for i in range(0,k):
                          temp=savetask4[i]
                          save.write(temp)
                          save.write("\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("5. List common actors and actresses in two movies.\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("Given first movie: ")
             save.write(givenFilm5First)
             save.write("\n")
             save.write("Given second movie: ")
             save.write(givenFilm5Second)
             save.write("\n")
             save.write("Result:\n")
             k=len(savetask5)
             for i in range(0,k):
                          temp=savetask5[i]
                          save.write(temp)
                          save.write("\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("6. List all actors and actresses in either of the movies but not both.\n")
             save.write("-----------------------------------------------------------------\n")
             save.write("Given first movie: ")
             save.write(givenFilm6First)
             save.write("\n")
             save.write("Given second movie: ")
             save.write(givenFilm6Second)
             save.write("\n")
             save.write("Result:\n")
             k=len(savetask6)
             for i in range(0,k):
                          temp=savetask6[i]
                          save.write(temp)
                          save.write("\n")
#function for task 7             

#function for menu             
def menu():
             print('--------------------------------------------------------SEARCHIN MOVIES-------------------------------------------------------')
             print('1. List all movies of given actor or actress.(Press1)')
             print("2. Given an actor or actress's name, find all the actors or actresses with whom he/she has acted.(Press 2)")
             print('3. List all actors and actresses in a movie.(Press 3)')
             print('4. List all actors and actresses in two movies.(Press 4)')
             print('5. List common actors and actresses in two movies.(Press 5)')
             print('6. List all actors and actresses in either of the movies but not both.(Press 6)')
             print('7. Save results to a file.(Press 7)')
             print('0.Exit.(Press 0)')
             menuChooser=input()
             if menuChooser == '1':
                          reagent()
                          task1()
                          reagent()
                          print('Press any key for back to the menu')
                          input()
                          menu()
             elif menuChooser =='2':
                          reagent()
                          task2()
                          reagent()
                          print('Press any key for back to the menu')
                          input()
                          menu()
             elif menuChooser =='3':
                          reagent()
                          task3()
                          reagent()
                          print('Press any key for back to the menu')
                          input()
                          menu()
             elif menuChooser =='4':
                          reagent()
                          task4()
                          reagent()
                          print('Press any key for back to the menu')
                          input()
                          menu()
             elif menuChooser =='5':
                          reagent()
                          task5()
                          reagent()
                          print('Press any key for back to the menu')
                          input()
                          menu()
             elif menuChooser =='6':
                          reagent()
                          task6()
                          reagent()
                          print('Press any key for back to the menu')
                          input()
                          menu()
             elif menuChooser =='7':
                          task7()
                          print('Datas saved successfully.')
                          print('Press any key for back to the menu')
                          input()
                          menu()
             elif menuChooser =='0':
                          exit()
             else:
                          menu()
#function for menu

menu()


                          
