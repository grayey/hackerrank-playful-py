# Enter your code here. Read input from STDIN. Print output to STDOUT

import fileinput;


inputLines = fileinput.input();
no_of_entries = int(inputLines[0]);
phone_book = dict();


"""

Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

"""


for idx, entry in enumerate(inputLines):

    if idx < no_of_entries:
        item = entry.split();
        contact_name = item[0].rstrip();
        contact_phone = item[1];
        phone_book[contact_name] = contact_phone;
        continue;

    entry_name = entry.rstrip();

    try:
        output = f"{entry_name}={phone_book[entry_name]}";
    except KeyError:
        output = "Not found";
    print(output);



    
    
