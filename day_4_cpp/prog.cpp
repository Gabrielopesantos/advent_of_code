#include<bits/stdc++.h>

std::vector<std::string> hairs_lst = {"amb", "blue", "brn", "gry", "grn", 
                                        "hzl", "oth"};


    static inline std::vector<str_view> splitString(str_view view, char delim = '\n')
        {
                    std::vector<str_view> ret;

                            while(!view.empty())
                                        {
                                                        size_t ln = view.find(delim);

                                                                    if(ln != std::string_view::npos)
                                                                                    {
                                                                                                        ret.emplace_back(view.data(), ln);
                                                                                                                        view.remove_prefix(ln + 1);
                                                                                                                                    }
                                                                                else
                                                                                                {
                                                                                                                    break;
                                                                                                                                }
                                                                                        }

                                    // account for the case when there's no trailing newline, and we still have some stuff stuck in the view.
                                          if(!view.empty())
                                                      ret.emplace_back(view.data(), view.length());
                                    
                                                             return ret;
                                                                 }
                                   
static inline std::string readFile(const std::string& path)
        {
                    FILE* f = fopen(path.c_str(), "r");
                            if(!f) fprintf(stderr, "failed to open file '%s'\n", path.c_str()), abort();

                                    std::string input;
                                            {
                                                            fseek(f, 0, SEEK_END);

                                                                        long fsize = ftell(f);
                                                                                    fseek(f, 0, SEEK_SET);  //same as rewind(f);

                                                                                                char* s = new char[fsize + 1];
                                                                                                            fread(s, fsize, 1, f);
                                                                                                                        fclose(f);
                                                                                                                                    s[fsize] = 0;

                                                                                                                                                size_t n = fsize;
                                                                                                                                                            while(n > 0 && s[--n] == '\n')
                                                                                                                                                                                ;

                                                                                                                                                                        input = std::string(s, n + 1);
                                                                                                                                                                                    delete[] s;
                                                                                                                                                                                            }

                                                    return input;
                                                        }


    static inline std::string replace(std::string input, const std::string& thing, const std::string& with)
        {
                    while(true)
                                {
                                                if(auto it = input.find(thing); it != std::string::npos)
                                                                    input.replace(it, thing.size(), with);

                                                            else
                                                                                break;
                                                                    }

                            return input;
                                }


std::string drop_last(std::string s, int n) {
    // auto n = s.size();

    return (s.size() >= n ? s.substr(0, s.size() - n) : s);



}

static inline std::optional<int64_t> try_int(std::string s) {
    try { return std::stoll(std::string(s));}
    catch(...) {return { };}
}

struct Passport {

    std::string byr;
    std::string iyr;
    std::string eyr;
    std::string hgt;
    std::string hcl;
    std::string ecl;
    std::string pid;
    std::string cid;
    
    static bool checkNum(std::string str, int min, int max) {
        // converter para int
        auto x = try_int(str);
        

        if (!x) return false;



//        return min <= *x && *x <= max;
        return min <= x && x <= max;
    }

    bool present() const {
    
        return !byr.empty() && !iyr.empty() && !eyr.empty()
            && !hgt.empty() && !hcl.empty() && !ecl.empty()
            && !pid.empty();
    }

    bool valid() const {
        if (!present())
            return false;
        
        if(!checkNum(byr, 1920, 2002) || !checkNum(iyr, 2010, 2020)
                || !checkNum(eyr, 2020, 2030))
            return false;

        bool heightOk = false;
        if(hgt.find("cm") != -1)
            heightOk = checkNum(drop_last(hgt,2), 150, 193);

        if(hgt.find("in") != -1)
            heightOk = checkNum(drop_last(hgt,2), 59, 76);

        if (!heightOk)
            return false;
        if (hcl.size() != 7 || hcl[0] != '#' || (int) hcl.substr(1).
                find_first_not_of("0123456789abcdef") != -1)
            return false;

        if (count(hairs_lst.begin(), hairs_lst.end(), ecl) != 1)
                return false;
        if (pid.size() != 9 || !try_int(pid))
            return false;

        return true;
    }
};

int main() {

    auto fixed = replace(replace(replace(readFile("input.txt"), "\n\n", "|"),
                    "\n", " "), "|", "\n");
    auto lines = splitString(fixed, ' ');

    std::vector<Passport> passports;
    for (auto& line : lines) {
        std::cout << "Bo";  
    } 


}
