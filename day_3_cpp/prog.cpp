#include<iostream>
#include <fstream>
#include<vector>
#include<string.h>

using namespace std;

int main() {
    std::ifstream mrf;
    std::string line;
    std::vector<std::string> lines;
    std::vector<std::pair<int,int>> cases = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}};
    std::vector<int> trees_case;

    mrf.open("input.txt");
    while (mrf.is_open()) {
        if (!mrf.eof()) {
            mrf >> line;
            lines.push_back(line);
        } else 
            mrf.close();
    }
   
   for (pair<int,int> p: cases) {
       int cur_x = 0;
       int trees_found = 0;
       for (size_t i = 0; i < lines.size(); i+=p.second) {
           if (cur_x > 30) {
                int true_pos = cur_x % 31;
                if (lines[i].substr(true_pos, 1).compare("#") == 0) trees_found++;
           } else {
                if (lines[i].substr(cur_x, 1).compare("#") == 0) trees_found++;
           }
            cur_x += p.first;
       }
       trees_case.push_back(trees_found);
    }
   int mlt = 1;
   for (auto i: trees_case) mlt *= i; 
   cout << mlt << "\n";
}
