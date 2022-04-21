# Reorganize String
# String Hashing Sorting 


class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Find the count of each characters
        cnts = Counter(s)

        # 2. Inorder to create max heap need to take negative of each count
        #    -(max) = min
        freqs = [(-cnt, char) for char, cnt in cnts.items()]

        # 3. Create Min Heap of -ve cnts = Max Heap of +ve cnts
        heapq.heapify(freqs)

        #-- Now char with max count is at top of Heap

        res = ''  # reorganized string to be formed
        
        # 4. track the last character of reorganized string (inorder to avoid same adjacent character)
        prev = (0, '')  # last char of reorganized string & its current frequency
        
        # 5. Heap Consumption
        while freqs:  # while all character are not consumed
            
            # take the character with max count at present (in heap) 
            # ie most freq character, except prev
            cnt, char = heapq.heappop(freqs)
            
            res += char  # add the character in resulted string
          
            # NOTE : as -ve cnt are stored so doing `+`, but effectively its decreasing the frequency of {char}
            cnt += 1     # freq update for {char}, 

            if prev[0] != 0: # prev char can now participate in string formation
                heapq.heappush(freqs, prev)

            prev = cnt, char # update prev character

        if prev[0] == 0:  # all alternating character are accomodated
            return res 
        else:             # last character will be repeated so not possible
            return ''

X = Solution()
print(X.reorganizeString("aab"))