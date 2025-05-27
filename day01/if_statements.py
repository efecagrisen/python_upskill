
#single if statement
browser_name = "chrome"

if browser_name == "chrome":
    print("Chrome is selected")


print("-------------")

#if else statement (only 2 conditions)
if browser_name == "chrome":
    print("Chrome is selected")
else:
    print("Firefox is selected")

print("---")


#Multi branch if statement (multiple conditions)
browser_name = "safari"
if browser_name == "chrome":
    print("Chrome is selected")
elif browser_name == "firefox":
    print("Firefox is selected")
else:
    print("Safari is selected")



print("----------------------------------")

score = -200

if 0 >= score >= 100:

    #pass
    if score >= 60:
        #pass
        print("passed")
    else:
        #pass
        print("failed")

else:
    print("failed")



