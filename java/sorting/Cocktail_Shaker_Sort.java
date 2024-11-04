public class Cocktail_Shaker_Sort {

    // 主排序方法
    public static void cocktailShakerSort(int[] array) {
        boolean swapped = true; // 标记是否有交换
        int start = 0; // 当前排序的开始索引
        int end = array.length - 1; // 当前排序的结束索引

        while (swapped) {
            swapped = false;

            // 从左到右进行冒泡
            for (int i = start; i < end; i++) {
                if (array[i] > array[i + 1]) {
                    swap(array, i, i + 1);
                    swapped = true;
                }
            }
            // 如果没有交换，说明数组已排序
            if (!swapped) {
                break;
            }

            // 更新结束索引
            end--;

            swapped = false;

            // 从右到左进行冒泡
            for (int i = end; i > start; i--) {
                if (array[i] < array[i - 1]) {
                    swap(array, i, i - 1);
                    swapped = true;
                }
            }
            // 更新开始索引
            start++;
        }
    }

    // 交换数组中两个元素的方法
    private static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    // 主方法
    public static void main(String[] args) {
        int[] array = {5, 3, 8, 4, 2, 7, 1, 6};
        System.out.println("原数组:");
        printArray(array);

        cocktailShakerSort(array);

        System.out.println("排序后数组:");
        printArray(array);
    }

    // 打印数组的方法
    private static void printArray(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
