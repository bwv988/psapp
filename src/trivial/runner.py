from case import Case

class Runner(object):
    """
    Run the whole thing.
    """
    def __init__(self):
        pass
    
    def run(self):
        """
        In this function we read the input from stdin line by line.
        For each customer we update the production batch as we receive the customer likes.
        We stop processing the case once we encounter the first customer that cannot be satisfied.
        """
        # Read the number of cases.
        C = int(input())

        # FIXME: Ugly type conversations and no checks whatsoever!
        for c in range(1, C + 1):
            # Process each case individually.
            N = int(input())
            M = int(input())
            my_case = Case(N)
                       
            success = True
            for _ in range(1, M + 1):
                # Process each customer in turn and update the production batch.
                raw = input().split()
                # We don't need to read T.                
                likes = list(map(int, (raw[1:])))

                # Success means: We could satisfy at least one customer like.
                success = my_case.assess_likes(likes)
                if(not(success)):
                    # If we can't satisfy the first customer, we can stop here immediately.                    
                    break
            
            # Produce output for current case.
            print("Case #" + str(c) + ": ", end="")
            
            if(success):                            
                my_case.print_final_batch()
            else:
                print("IMPOSSIBLE")

if __name__ == "__main__":
    r = Runner()
    r.run()