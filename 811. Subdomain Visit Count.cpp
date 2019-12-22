class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        map <string, int> subdomain;
        map<string, int>::iterator it;
        vector<string> list;
        string word = "";
        for (string& s : cpdomains) {
            int i = 0;
            string num = "";
            while (!isspace(s[i])) {
                num += s[i];
                i++;
            }
            it = subdomain.find(s.substr(i+1, s.size()));
            if(it == subdomain.end()) 
                subdomain[s.substr(i+1, s.size())] = stoi(num);
            else 
                subdomain[s.substr(i+1, s.size())] += stoi(num);  
            
            for (int j = i; j < s.size(); j++) {
                if(s[j] == '.' || j == s.size()) {
                 it = subdomain.find(s.substr(j+1, s.size()));
                 if(it == subdomain.end()) 
                     subdomain[s.substr(j+1, s.size())] = stoi(num);
                 else 
                     subdomain[s.substr(j+1, s.size())] += stoi(num);  
                }
           } 
        }
        for (it = subdomain.begin(); it != subdomain.end(); it++) {
            string sub = "";
            sub += to_string(it->second);
            sub += " ";
            sub += it->first;
            list.push_back(sub);
        }    
        return list;
    }
};
