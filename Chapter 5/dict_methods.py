marks = {
    "Sandeep": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Sandeep"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Sandeep": 99, "Renuka": 100})
# print(marks)

print(marks.get("Sandeep2")) # Prints None
print(marks["Sandeep2"]) # Returns an error