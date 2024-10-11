def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    count = 0  
    length = len(flowerbed)
    
    for i in range(length):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            if empty_left and empty_right:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    
    return count >= n

if __name__ == "__main__":
    flowerbed = list(map(int, input("Enter the flowerbed as a space-separated list of 0s and 1s: ").split()))
    n = int(input("Enter the number of flowers to plant: "))
    
    result = canPlaceFlowers(flowerbed, n)
    if result:
        print("Output: True")
    else:
        print("Output: False")
