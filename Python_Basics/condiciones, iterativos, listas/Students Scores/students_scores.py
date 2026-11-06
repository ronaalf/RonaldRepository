total_notes = int(input("Enter total number of grades: "))

note_counter = 1
number_falling_grades = 0
average_falling_grades = 0
number_passing_grades = 0
average_passing_grades = 0
average_total_grades = 0

while note_counter <= total_notes:
    current_note = int(input("Enter your grade score: "))

    note_counter = note_counter + 1

    if current_note < 70:
        number_falling_grades = number_falling_grades + 1
        average_falling_grades = average_falling_grades + current_note
    else:
        number_passing_grades = number_passing_grades + 1
        average_passing_grades = average_passing_grades + current_note
    average_total_grades = average_total_grades + (current_note / total_notes)

average_falling_grades = average_falling_grades / number_falling_grades

average_passing_grades = average_passing_grades / number_passing_grades

print(f"The student got passing grades in {number_passing_grades} subjects")
print(f"The passing grades average is {average_passing_grades}")
print(f"On the other hand, The student failed {number_falling_grades} subjects")
print(f"The failing grades average is {average_falling_grades}")
print(f"All grades the total average is {average_total_grades}")

