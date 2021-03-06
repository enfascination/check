### Boilerplate
from IPython.core.display import display, HTML

### answers object.  Each q has a code (key) and a correct answer (value).
answers = {}
# Arithmetic
answers['try_it_out'] = {'l':2, 'correct':8}
answers['leading_zero'] = {'l':2, 'correct':1,'minmul':1,'maxmul':3}
answers['big_numbers'] = {'l':2, 'correct':50000000000}
answers['arithmetic1'] = {'l':2, 'correct':3*4+5+6}
answers['arithmetic2'] = {'l':2, 'correct':(4*5)-(4-3),(4*5)-4-3:'Did you forget parentheses?'}
answers['spaces_in_arithmetic1'] = {'l':2, 'correct':4,'minmul':1,'maxmul':4}
answers['spaces_in_arithmetic2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':4}
answers['parentheses'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
# Modules
answers['import_syntax1'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3}
answers['import_syntax2'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3}
answers['scientific_notation'] = {'l':2, 'correct':3,'minmul':1,'maxmul':5}
# Output
answers['code_blocks_output1'] = {'l':2, 'correct':3,'minmul':1,'maxmul':7}
answers['code_blocks_output2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':7}
answers['code_blocks_output3'] = {'l':2, 'correct':7,'minmul':1,'maxmul':7}
answers['code_blocks_output4'] = {'l':2, 'correct':5,'minmul':1,'maxmul':7}
answers['code_blocks_output5'] = {'l':2, 'correct':5,'minmul':1,'maxmul':7}
# Variables
answers['variable_names1'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names2'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names3'] = {'l':2, 'correct':2,'minmul':1,'maxmul':2}
answers['variable_names4'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names5'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names6'] = {'l':2, 'correct':1,'minmul':1,'maxmul':2}
answers['variable_names7'] = {'l':2, 'correct':2,'minmul':1,'maxmul':2}
answers['variable_names_cont1'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3}
answers['variable_names_cont2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':3}
answers['variable_assignment1'] = {'l':2, 'correct':5,'minmul':1,'maxmul':5}
answers['variable_assignment2'] = {'l':2, 'correct':3,'minmul':1,'maxmul':5}
answers['variable_assignment3'] = {'l':2, 'correct':2,'minmul':1,'maxmul':5}
answers['variable_name_quality1'] = {'l':2, 'correct':3,'minmul':1,'maxmul':4}
answers['reassignment1'] = {'l':2, 'correct':1,'minmul':1,'maxmul':3,'listans':[5,55,555]}
answers['reassignment2'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3,'listans':[5,55,555]}
answers['reassignment3'] = {'l':2, 'correct':2,'minmul':1,'maxmul':3,'listans':[10,30]}
answers['reassignment4'] = {'l':2, 'correct':1,'minmul':1,'maxmul':3,'listans':[10,30]}
answers['reassignment5'] = {'l':2, 'correct':9}
answers['reassignment6'] = {'l':2, 'correct':5}
answers['reassignment7'] = {'l':2, 'correct':7}

answers['errors1'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['type1'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['type2'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['type3'] = {'l':3,'correct':1,'minmul':1,'maxmul':5}
answers['booleans1'] = {'l':3,'correct':2,'minmul':1,'maxmul':3}
answers['booleans2'] = {'l':3,'correct':4,'minmul':1,'maxmul':4}
answers['booleans3'] = {'l':3,'correct':1,'minmul':1,'maxmul':4}
answers['writing_strings1'] = {'l':3,'correct':'Hi Python'}
answers['writing_strings2'] = {'l':3,'correct':'abcdefghijklmnopqrstuvwxyz'}
answers['string_length1'] = {'l':3,'correct':3,'minmul':1,'maxmul':4}
answers['string_length2'] = {'l':3,'correct':7}
answers['string_length3'] = {'l':3,'correct':0}
answers['string_length4'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['quote_types1'] = {'l':3,'correct':3,'minmul':1,'maxmul':5}
answers['substrings_in_strings1'] = {'l':3,'correct':4,'minmul':1,'maxmul':5}
answers['substrings_in_strings2'] = {'l':3,'correct':6,'minmul':1,'maxmul':6}
answers['combining_strings1'] = {'l':3,'correct':2,'minmul':1,'maxmul':5}
answers['combining_strings2'] = {'l':3,'correct':3,'minmul':1,'maxmul':4}
answers['comparing_things1'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things2'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things3'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things4'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things5'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things6'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things7'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things8'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things9'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things10'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things11'] = {'l':3,'correct':2,'minmul':1,'maxmul':2}
answers['comparing_things12'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['comparing_things13'] = {'l':3,'correct':3,'minmul':1,'maxmul':4}
answers['comparing_things14'] = {'l':3,'correct':1,'minmul':1,'maxmul':2}
answers['compare_v_assign1'] = {'l':3,'correct':1,'minmul':1,'maxmul':3}
answers['compare_v_assign2'] = {'l':3,'correct':3,'minmul':1,'maxmul':5}
answers['relative_comparisons1'] = {'l':3,'correct':2,'minmul':1,'maxmul':4}
answers['relative_comparisons2'] = {'l':3,'correct':4,'minmul':1,'maxmul':4}


###  styling of user feedback
stylehtml =  """
<style>
  h1 {    
    display:inline-block;
    padding: 10px;
  }
  h1.right {    
    background-color: #dff0d8;    
    border-color: #d0e9c6;    
    color: #3c763d;    
  }
  h1.wrong {    
    background-color: #fcf8e3;    
    border-color: #faf2cc;    
    color: #8a6d3b; 
  }
  h1.error {    
    background-color: #fcf8e3;    
    border-color: #faf2cc;    
    color: #8a6d3b; 
  }
  h2.wrong {    
    background-color: #fcf8e3;    
    border-color: #faf2cc;    
    color: #8a6d3b; 
  }
</style>
"""
correct = HTML( stylehtml + '<h1 class="right">Correct!</h1>')
incorrect = HTML( stylehtml + '<h1 class="wrong">Try again.</h1>')
def broken_key(key):
  return HTML(stylehtml + '<h1 class="error">check(\'{}\',...) error name \'{}\' was modified!</h1>'.format(key,key))

def incorrect_with_hint(hint):
  return HTML(stylehtml + '<h1 class="wrong">Try again.</h1>\n<h2 class="wrong">Hint: {}</h2>'.format(hint))

def check(key, answer):
  if answer == ...:
    return
  if key not in answers:
    display(broken_key(key))
    return
  test = answer == answers[key]
  answers[key]['entered'] = answer
  if test:
    display( correct )
  elif not isinstance(answers[key],dict):
    display( incorrect )
  else:
    test = answer == answers[key]['correct']
    if test:
      display( correct )
    elif 'minmul' in answers[key]:
      if not isinstance(answer,int) or int(answer) < answers[key]['minmul'] or int(answer) > answers[key]['maxmul']:
        if 'listans' in answers[key] and answer in answers[key]['listans']:
          display(incorrect_with_hint('Make sure to select the multiple choice number, not associated answer.'))
        else:
          display(incorrect_with_hint('Select the multiple choice number between {} and {}.'.format(answers[key]['minmul'],answers[key]['maxmul'])))
    elif 'attempts' in answers[key]:
      if answer in answers[key]:
        display(incorrect_with_hint(answers[key][answer]))
      elif answers[key] > 3 and 'hint' in answers[key]:
        display(incorrect_with_hint(answers[key]['hint']))
      else:
        display( incorrect )
      answers[key]['attempts'] += 1
    else:
      display( incorrect )
      answers[key]['attempts'] = 1
  return( test )

def checkcheck(lesson):
  nCorrect = 0
  nTotal = 0
  for qid, q in answers.items():
    if q['l'] == lesson:
      nTotal += 1
      if 'entered' in q and q['correct'] == q['entered']:
        nCorrect += 1
  return( nCorrect, nTotal )

if __name__ == "__main__":
  test = 2
  if test == 0:
    print( checkcheck(1) )
  elif test == 1:
    check('try_it_out', 8 )
    # Arithmetic
    check('leading_zero', 1 )
    check('big_numbers', 50000000000)
    check('arithmetic1', (3*4)+(5+6) )
    check('arithmetic2', (4*5)-(4-3) )
    check('spaces_in_arithmetic1', 4)
    check('spaces_in_arithmetic2', 3)
    check('parentheses', 1)
    # Modules
    check('import_syntax1', 2)
    check('import_syntax2', 2)
    check('scientific_notation', 3)
    # Output
    check('code_blocks_output1', 3)
    check('code_blocks_output2', 3)
    check('code_blocks_output3', 7)
    check('code_blocks_output4', 5)
    check('code_blocks_output5', 5)
    # Variables
    check('variable_names1', 1)
    check('variable_names2', 1)
    check('variable_names3', 2)
    check('variable_names4', 1)
    check('variable_names5', 1)
    check('variable_names6', 1)
    check('variable_names7', 2)
    check('variable_names_cont1', 2)
    check('variable_names_cont2', 3)
    check('variable_assignment1', 5)
    check('variable_assignment2', 3)
    check('variable_assignment3', 2)
    check('variable_name_quality1', 3)
    check('reassignment1', 1)
    check('reassignment2', 2)
    check('reassignment3', 2)
    check('reassignment4', 1)
    check('reassignment5', 9)
    check('reassignment6', 5)
    check('reassignment7', 7)
    print( checkcheck(1) )
  elif test == 2:
    # Errors
    check('errors1', 4)
    # Type
    check('type1', 4)
    check('type2', 4)
    check('type3', 1)
    # Booleans
    check('booleans1', 2)
    check('booleans2', 4)
    check('booleans3', 1)
    # Strings
    check('writing_strings1', 'Hi Python')
    check('writing_strings2', 'abcdefghijklmnopqrstuvwxyz')
    check('string_length1', 3)
    check('string_length2', 7)
    check('string_length3', 0)
    check('string_length4', 4)
    check('quote_types1', 3)
    check('substrings_in_strings1', 4)
    check('substrings_in_strings2', 6)
    check('combining_strings1', 2)
    check('combining_strings2', 3)
    # Comparisons
    check('comparing_things1', 1)
    check('comparing_things2', 2)
    check('comparing_things3', 1)
    check('comparing_things4', 2)
    check('comparing_things5', 1)
    check('comparing_things6', 2)
    check('comparing_things7', 1)
    check('comparing_things8', 2)
    check('comparing_things9', 2)
    check('comparing_things10', 2)
    check('comparing_things11', 2)
    check('comparing_things12', 1)
    check('comparing_things13', 3)
    check('comparing_things14', 1)
    check('compare_v_assign1', 1)
    check('compare_v_assign2', 3)
    check('relative_comparisons1', 2)
    check('relative_comparisons2', 4)
    print( checkcheck(2) )
