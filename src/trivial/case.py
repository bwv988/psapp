from batch import Batch

class Case(object):
    """
    Assesses customers within a case.
    """

    def __init__(self, N):
        self.batch = Batch(N)       
    
    def assess_likes(self, likes):
        """
        Iterates over X, Y pairs of customer likes and updates the batch accordingly. 
        We count the grand total of successful updates per customer.
        This is to check later if each customer got at least one color they like.
        """
        successes = 0
        for i in range(0, len(likes) - 1, 2):
            X = likes[i]
            Y = Case.recode_col(likes[i + 1])
            successes += self.batch.set_col(X, Y)        
        return(successes > 0)
    
    def print_final_batch(self):
        """
        Produce output for paint batch.
        """
        # Re-code values.
        final_batch = list(map(lambda x: x - 1 if (x > 0) else 0, self.batch.get_batch()))
        # Print space-separated list.
        print(" ".join(map(str, final_batch)))

    @staticmethod
    def recode_col(c):
        """
        This is needed as we distinguish betweeen unset, glossy, and matte colors.
        """
        return(c + 1)

if __name__ == "__main__":
    pass