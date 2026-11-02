class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1
        max_area = 0
        while j > i:
            temp_area = (j-i)*min(heights[i],heights[j])
            if max_area < temp_area:
                max_area = temp_area
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_area

            

        