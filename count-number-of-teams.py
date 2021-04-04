class Solution:
    
    
        
    def numTeams(self, rating: List[int]) -> int:
        
        #Brute Force Approach
        
        # length=len(rating)
        # count=0
        # for i in range(0,length):
        #     for j in range(i+1,length):
        #         if(rating[i]<rating[j]):
        #             for k in range(j+1,length):
        #                 if(rating[i]<rating[k]) and (rating[j]<rating[k]):
        #                     count+=1
        #         elif(rating[i]>rating[j]):
        #             for k in range(j+1,length):
        #                 if(rating[i]>rating[k]) and (rating[j]>rating[k]):
        #                     count+=1
        # return count
        
        
        # Optimized Approach 
        def count(rating):
            length=len(rating)
            result=[0]*length  #It stores the number of element that lower than rating[i] on the left
            output=0
            for i in range(length):
                for j in range(i):
                    if rating[i]>rating[j]:
                        result[i]+=1
                        output+=result[j]
            return output
        
        return count(rating) + count(rating[::-1])