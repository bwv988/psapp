class Batch(object):
    """
    This class represents a Paintshop production batch of N colors.
    """
    
    # A color can either be unset, glossy or matte. Later, we treat unset as glossy.
    # We use this coding to detect if we can satisfy a customer like, or not.
    UNSET = 0
    GLOSSY = 1
    MATTE = 2
        
    def __init__(self, N):       
        self.batch = [Batch.UNSET] * N
        
    def get_batch(self):
        return(self.batch)
            
    def set_col(self, X, Y):
        """
        This function sets paint color # X to the wanted type Y (encoded).
        It returns 1 for a successful update of the batch, and 0 in case 
        the updated cannot be made, due to a clash.
        """       
        current = self.batch[X - 1]
        
        if (current == Batch.UNSET):            
            self.batch[X - 1] = Y
        else:
            if (current != Y):
                # We cannot make this update.                
                return(0)
        return(1)
        
if __name__ == "__main__":
  pass
    