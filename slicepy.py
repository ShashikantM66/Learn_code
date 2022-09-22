# slice is used to slice any sequence (string, tuple, list, range, or bytes).
text = "python programming"
print(text)
text_slice = slice(6)
print(text[text_slice])

# syntax slice(start,stop,step)
py_string= "python"
python_text=slice(4)
print(py_string[python_text]) #pyth

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn
