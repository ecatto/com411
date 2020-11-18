import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_char
import basics.output.beep as beep_art
import basics.output.ascii_art as ascii_art

import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.data_types2 as data_types2
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input

import basics.decisions.simple_decision.if_statement as simple_if
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.modulo_operator as modulo
import basics.decisions.simple_decision.comparison_operator as comparison
import basics.decisions.simple_decision.counter as counter

import basics.decisions.and_operator as and_operator
import basics.decisions.or_operator as or_operator
import basics.decisions.nested_decisions.nested as nested
import basics.decisions.nested_decisions.nestception as nestception

import basics.repetitions.while_loop.simple as simple_while
import basics.repetitions.while_loop.count as while_count
import basics.repetitions.while_loop.ascii as while_ascii
import basics.repetitions.while_loop.len as while_len
import basics.repetitions.while_loop.sum100 as sum100
import basics.repetitions.while_loop.sum_user_numbers as sum_user
import basics.repetitions.while_loop.factorial as factorial

import basics.repetitions.for_loop.simple as simple_for
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.range as for_range
import basics.repetitions.for_loop.characters as for_char
import basics.repetitions.for_loop.reverse as for_reverse
import basics.repetitions.for_loop.membership_operators as membership

import basics.repetitions.nested_loop.nested as nested_loop
import basics.repetitions.nested_loop.nesting as nesting_loop
import basics.repetitions.nested_loop.nesting2 as nesting2_loop

import basics.functions.ascii as ascii_function
import basics.functions.asc_char as asc_char
import basics.functions.simple_function as simple_function
import basics.functions.function_with_nesting as nesting_function
import basics.functions.function_with_parameter as parameter_function
import basics.functions.function_with_loop as loop_function
import basics.functions.function_with_parameters as parameters_function
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_function
import basics.functions.function_calls as function_calls



def run_block_a():
    print("""Which program in 'Block A: Basics' do you wish to run?
    \t 1. Output
    \t 2. input
    \t 3. If statements
    \t 4. Nested Ifs,and AND/ORs
    \t 5. Loops
    \t 6. Functions
    """)
    choice = input()

    if choice == "1":
      print("""Which program in 'Output' do you wish to run?
      \t 1. Simple message
      \t 2. Multiline message
      \t 3. Escape characters
      \t 4. Beep art
      \t 5. Ascii robot
      \t 6. Return to previous menu
      """)
      response = int(input())

      if (response == 1):
        simple_message.run()
      elif (response == 2):
        multiline_message.run()
      elif (response == 3):
        escape_char.run()
      elif (response == 4):
        beep_art.run()
      elif (response == 5):
        ascii_art.run()
      elif (response==6):
        run()
      else:
        print("Please choose a number between 1 and 6")

    if choice == "2":
      print("""Which program in 'Input' do you wish to run?
      \t 1. User input
      \t 2. AScii robot
      \t 3. Data types 
      \t 4. Data types 2 
      \t 5. String operators 
      \t 6. Return to previous menu
      """)
      response = int(input())

      if (response == 1):
        user_input.run()
      elif (response == 2):
        ascii_robot.run()
      elif (response == 3):
        data_types.run()
      elif (response == 4):
        data_types2.run()
      elif (response == 5):
        string_operators.run()
      elif (response==6):
        run()
      else:
        print("Please choose a number between 1 and 6")    

    if choice == "3":
      print("""Which program in 'If statements' do you wish to run?
      \t 1. Simple if
      \t 2. If else
      \t 3. If elif else
      \t 4. modulo
      \t 5. comparison
      \t 6. counter
      \t 7. Return to previous menu
      """)
      response = int(input())

      if (response == 1):
        simple_if.run()
      elif (response == 2):
        if_else.run()
      elif (response == 3):
        if_elif_else.run()
      elif (response == 4):
        modulo.run()
      elif (response == 5):
        comparison.run()
      elif (response==6):
        counter.run()
        or_operator.run()
      elif (response == 7):
        run()
      else:
        print("Please choose a number between 1 and 7")

    if choice == "4":
      print("""Which program in 'Nested Ifs,and AND/ORs' do you wish to run?
      \t 1. Nested
      \t 2. Nestception
      \t 3. AND
      \t 4. OR
      \t 5. Return to previous menu
      """)
      response = int(input())

      if (response == 3):
        and_operator.run()
      elif (response==4):
        or_operator.run()
      elif (response == 1):
        nested.run()
      elif (response == 2):
        nestception.run()
      elif (response == 5):
        run()
      else:
        print("Please choose a number between 1 and 5")

    if choice == "5":
      print("""Which program in 'Loops' do you wish to run?
      \t 1. While loops
      \t 2. For loops
      \t 3. Nested loops
      \t 5. Return to previous menu
      """)
      response = int(input())

      if (response == 1):
        print("""Which program in 'While Loops' do you wish to run?
        \t 1. Simple While loop
        \t 2. Counting while loop
        \t 3. ASCII loop
        \t 4. Repeated word (length of word)
        \t 5. Sum of first 100 numbers
        \t 6. Sum of user numbers
        \t 7. Factorial
        \t 8. Return to main menu
        """)
        reply = int(input())

        if (reply == 1):
          simple_while.run()
        elif (reply==2):
          while_count.run()
        elif (reply == 3):
          while_ascii.run()
        elif (reply == 4):
          while_len.run() 
        elif (reply == 5):
          sum100.run()
        elif (reply == 6):
          sum_user.run()
        elif (reply == 7):
          factorial.run()
        elif (reply == 8):
          run()
        else:
          print("Please choose a number between 1 and 8")

      if (response == 2):
        print("""Which program in 'For Loops' do you wish to run?
        \t 1. Simple For loop
        \t 2. Counting down for loop
        \t 3. Range
        \t 4. Characters
        \t 5. Reverse
        \t 6. Membership
        \t 7. Return to main menu
        """)
        response = int(input())

        if (response == 1):
          simple_for.run()
        elif (response==2):
          count_down.run()
        elif (response == 3):
          for_range.run()
        elif (response == 4):
          for_char.run()
        elif (response == 5):
          for_reverse.run()
        elif (response == 6):
          membership.run()
        elif (response == 8):
          run()
        else:
          print("Please choose a number between 1 and 7")
  
      if (response == 3):
        print("""Which program in 'Nested Loops' do you wish to run?
        \t 1. Nested loop
        \t 2. Nesting loop
        \t 3. Nesting loop 2
        \t 4. Return to main menu
        """)
        reply = int(input())

        if (reply == 1):
          nested_loop.run()
        elif (reply==2):
          nesting_loop.run()
        elif (reply == 3):
          nesting2_loop.run()
        elif (reply == 4):
          run()
        else:
          print("Please choose a number between 1 and 4")

    if choice == "6":
      print("""Which program in 'Functions' do you wish to run?
      \t 1. ASCII function
      \t 2. ASCII Character
      \t 3. Simple function
      \t 4. Nesting function
      \t 5. Function with 1 parameter_function
      \t 6. Function with loop
      \t 7. Function with 2 parameters
      \t 8. Multiple functions
      \t 9. Return function
      \t 10. Function calls
      \t 11. Return to previous menu
      """)
      response = int(input())

      if (response == 1):
        ascii_function.run()
      elif (response == 2):
        asc_char.run()
      elif (response == 3):
        simple_function.run()
      elif (response == 4):
        nesting_function.run()
      elif (response == 5):
        parameter_function.run()
      elif (response == 6):
        loop_function.run()
      elif (response == 7):
        parameters_function.run()
      elif (response == 8):
        multiple_functions.run()
      elif (response == 9):
       return_function.run()
      elif (response == 10):
        function_calls.run()

      elif (response==11):
        run()
      else:
        print("Please choose a number between 1 and 11")


def run():
    is_running = True

    while(is_running):
        print("\nWhat would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()