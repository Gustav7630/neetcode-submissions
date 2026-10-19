class Solution:
    def numDecodings(self, s: str) -> int:
        # bind 0s right
        # 0<n<27
        #12 ->3 a, b , ab
        #choose keep or leave 1
        # choose 2, only option
        # 121 can be split 1 2 1 12 21 = 5
        # max len 2
        #check self, see if can join forward
        #but this is for individual chars, need to add to all prior possibilities
        # 120121
        # 12 = 3  121 = 5
        # 3*5 ways
        #dp try each way

        #wrong approach, need to always guarentee one assignment
        #choose do we keep 1 or go to length 2



        #12 1 12 

        from functools import lru_cache
        @lru_cache(None)
        def search(index):

            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            # Decode one digit
            res = search(index + 1)

            # Decode two digits
            if index + 1 < len(s):
                segment = int(s[index:index + 2])

                if segment <= 26:
                    res += search(index + 2)

            return res

        return search(0)



