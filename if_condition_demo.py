is_female = True
is_tall = False
if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You are a not female but you are tall")
else:
    print("You are either not a female or not tall")