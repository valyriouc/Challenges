#include<string>
#include<vector>

std::vector<std::string> solution(const std::string &s) {
    std::string original = s;
    std::vector<std::string> pairs; 

    if(original.length() % 2 != 0) {
        original.push_back('_');
    }

    int count = 0;
    std::string tmp;
    for(auto i : original) {
        tmp.append(i)
        count++;
        if (count == 2) {
            pairs.push_back(tmp);
            tmp = "";
            count = 0;
        }
    } 

    return pairs;
}
