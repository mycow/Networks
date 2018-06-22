def multiplex(messages):
    index=0
    initial=60400
    count=0
    with open('infile', 'w') as f:
        while checkEmpty(messages) != 1:    #run until all lists are empty
            for message in messages:
                for i in range(5):          #run through each list 5 times
                    if not message:
                        f.write("{} :No messages\n" .format(initial + index))      #write no message if nothing
                        count += 1
                        break
                    else:
                        f.write("{} :{}\n" .format(initial + index,message.pop(0)))    #pop item put in file
                        count += 1
                index += 1
            index=0
    return count


def demultiplex(input_file='muxed_stream'):
    msg0 = []
    msg1 = []
    msg2 = []
    msg3 = []
    msg4 = []
    line = ""

    with open('infile', 'r') as f:
        for mess in f:
            line = mess
            if "No messages" != line[7:-1]:
                if "60400" == line[0:5]:   #msg0 fill
                    msg0.append(line[7:-1])
                elif "60401" == line[0:5]:   #msg1 fill
                    msg1.append(line[7:-1])
                elif "60402" == line[0:5]:   #msg2 fill
                    msg2.append(line[7:-1])
                elif "60403" == line[0:5]:   #msg3 fill
                    msg3.append(line[7:-1])
                else:   #msg4 fill
                    msg4.append(line[7:-1])

    messages = (msg0, msg1, msg2, msg3, msg4)   #compile list of lists
    print(messages)
    return messages

def checkEmpty(list):   #check list empty or not
    for i in list:
        if len(i) != 0:
            return 0
    return 1

## YOU DON'T NEED TO EDIT ANYTHING BELOW HERE

def test_case_1():
    """Testing Multiplexing with tons of messages."""

    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ('1', '2', '3', '4', '5', '6', '7', '8', '9'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'),
        ('1', '2', '3', '4'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')
    )

    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]

    multiplex(messages_copy)
    messages_received = demultiplex('muxed_stream')

    assert len(messages_received[0]) == 9
    assert len(messages_received[1]) == 17
    assert len(messages_received[2]) == 20
    assert len(messages_received[3]) == 16
    assert len(messages_received[4]) == 24

def test_case_2():
    """Testing multiplexing with tons of lost messages."""

    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ("This ain't", "no intro,", " this the entree"),
        (),
        (),
        (),
        ("Hit that", "intro with Kanye ", "and sound like Andre"),
        ("Tryna", "turn", "my", "baby", "mama", "to", "my", "fiancee"),
        ("She like"," music, she from", "Houston",  "like Auntie Yonce"),
        ("Man my daughter couldn't", "have a better mother"),
        ("If she ever", "find another, he", "better", "love", "her")
    )

    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]

    multiplex(messages_copy)
    messages_received = demultiplex('muxed_stream')

    assert len(messages_received[0]) == 3
    assert len(messages_received[1]) == 0
    assert len(messages_received[2]) == 0
    assert len(messages_received[3]) == 0
    assert len(messages_received[4]) == 22


if __name__ == '__main__':
    test_case_1()
    test_case_2()
