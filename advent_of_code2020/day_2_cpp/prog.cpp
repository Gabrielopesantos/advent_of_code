#include<bits/stdc++.h>
#include<typeinfo>

using namespace std;

int main() {
    int countpt1 = 0;
    int countpt2 = 0;
    vector<string> lst;

    FILE* fp = fopen("input.txt", "r");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    char* line = NULL;
    size_t len = 0;
    while ((getline(&line, &len, fp)) != -1) {
        // printf("%s", line);
        lst.push_back(line);
    }
    fclose(fp);
    if (line)
        free(line);

    for (string line: lst) {
        
        int end = line.find("-");
        int min = std::stoi(line.substr(0, end));
        line.erase(0, end + 1);

        end = line.find(" ");
        int max = std::stoi(line.substr(0, end));
        line.erase(0, end + 1);

        char ch_to_check = line[0];
        line.erase(0, 3);
        // pt1 
        int counts[26] = {};

        for (const auto& c: line) {
            counts[c - 'a']++;
        }
        
        int ch_counter = std::count(line.begin(), line.end(), ch_to_check);
        if (ch_counter <= max && ch_counter >= min) countpt1++;

        //int found = counts[ch_to_check - 'a'];
        //if (found <= max && found >= min) {
        //    countpt1++;
        //}

        // pt2

        //if ((line[min-1] != ch_to_check && line[max-1] == ch_to_check) ||
        //       (line[min-1] == ch_to_check && line[max-1] != ch_to_check)) 
        if ((line[min-1] == ch_to_check) ^ (line[max-1] == ch_to_check))
            countpt2++; 

    }
    cout << countpt1 << "\n" << countpt2;
}
