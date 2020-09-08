class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                diff = min(height[stack[-1]], height[i]) - height[top]
                
                water += distance * diff

            stack.append(i)
        return water