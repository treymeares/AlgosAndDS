class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        
        if color == newColor:
            return image
        
        visited = [((sr, sc))]
        unvisited = [(sr, sc)]
        
        while len(unvisited) > 0:
            r, c = unvisited.pop()
            
            if r >= rows or r < 0 or c >= cols or c < 0:
                continue
            
            if image[r][c] == color:
                image[r][c] = newColor
            else:
                continue
                
            if (r+1, c) not in visited:
                    visited.append((r+1, c))
                    unvisited.append((r+1, c))
                    
            if (r, c+1) not in visited:
                    visited.append((r, c+1))
                    unvisited.append((r, c+1))
                    
            if (r, c-1) not in visited:
                    visited.append((r, c-1))
                    unvisited.append((r, c-1))
                    
            if (r-1, c) not in visited:
                    visited.append((r-1, c))
                    unvisited.append((r-1, c))
                    
        return image