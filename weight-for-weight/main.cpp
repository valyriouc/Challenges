#include<string>
#include<iostream>
#include<map>
#include<vector>

class WeightSort
{
public:
    static std::string orderWeight(const std::string &input) {
        std::map<int, std::vector<std::string>> mapping;
        int key = 0;
        bool added = false;
        std::string value = "";
        for(int i = 0; i <= input.length(); i++) {
            int e = int(input[i] - '0');
            if (e < 0 && !added) {
                try {
                    mapping.at(key).push_back(value);
                    bool isSorted = true;
                    do {
                        isSorted = true;
                        for (int i = 0; i < mapping.at(key).size() - 1; i++) {
                            if (mapping.at(key)[i] > mapping.at(key)[i+1]) {
                                std::string tmp = mapping.at(key)[i + 1];
                                mapping.at(key)[i + 1] = mapping.at(key)[i];
                                mapping.at(key)[i] = tmp;
                                isSorted = false;
                            }
                        }
                    } while(!isSorted);
                }catch(const std::out_of_range &e) {
                    mapping.insert(std::pair<int,std::vector<std::string>>(key, {value}));
                }
                key = 0;
                value = "";
                added = true;
                continue;
            }

            key += e;
            value += input[i];
            added = false;
        } 

        std::string output = "";
        bool first = true;
        for(std::pair<int, std::vector<std::string>> it : mapping) {
            for(std::string i : it.second) {
                if (first) {
                    first = false;
                    output += i;
                    std::cout << i << std::endl;
                }
                else {
                    output += " " + i;
                }
            }
        }

        return output;
    }
};

int main() {
    std::cout << WeightSort::orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123") << std::endl;
}