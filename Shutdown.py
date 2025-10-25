ans = input("Do you want to Shut Down?")
def shutdown(ans):

 if ans == "yes":
    print("Shutting down")
 elif ans == "no":
    print("Error: pausing shut down")
 else:
    print("sorry")

shutdown()