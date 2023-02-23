#include <vector>
#include <map>

#pragma region  

std::vector<int> bubble_sort(std::vector<int> input)
{
    bool is_sorted = true;
    do
    {
        is_sorted = true;
        for (int i = 0; i < input.size() - 1; i++)
        {
            if (input[i] > input[i + 1])
            {
                int tmp = input[i + 1];
                input[i + 1] = input[i];
                input[i] = tmp;
                is_sorted = false;
            }
        }
    } while (!is_sorted);
    
    return input;
}

std::vector<int> deleteNth(std::vector<int> arr, int n)
{
    std::vector<int> sorted_arr{bubble_sort(arr)};
    std::vector<int> output {};
    int current_element {0};
    int count {0};
    for (auto e : sorted_arr) {
        if (current_element != e) {
            current_element = e;
            count = 0;
        }
        if (count < n) {
            output.push_back(e);
            count++
        }
    }

    return output;
}

#pragma endregion

std::vector<int> deleteNth(std::vector<int> arr, int n)
{
    std::vector<int> output;
    std::map<int, int> tmp = {};
    for(auto i : arr) {
        if (tmp.find(i) != tmp.end()) {
            tmp.at(i) += 1;
        }
        else {
            tmp.insert({i, 1});
        }

        if (tmp.at(i) <= n) {
            output.push_back(i);
        }
    }

    return output;
}
