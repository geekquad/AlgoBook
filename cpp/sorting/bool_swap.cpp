#include <iostream> 
#include <utility> 
 
 
int main()
{
    const int length(9);
    int array[length] = { 1, 2, 3, 4, 9, 8, 7, 5, 6 };
    int count = length; 
    for (int iteration = 0; iteration < length-1; ++iteration)
    {
 
        count--; 
        bool swap = false;
        for (int currentIndex = 0; currentIndex < count; ++currentIndex)
        {
 
            if (array[currentIndex] > array[currentIndex + 1])
            {
 
                std::swap(array[currentIndex], array[currentIndex + 1]);
                swap = true;
            }
            
        
        }
        if (swap == false)
        {
            std::cout << "stop at " << iteration+1 << ' ' << '\n';
            break;
        }
    }
 
    for (int index = 0; index < length; ++index)
        std::cout << array[index] << ' ';
 
    return 0;
}
