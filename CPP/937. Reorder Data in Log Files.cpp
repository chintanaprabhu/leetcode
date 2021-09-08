class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) { 
        vector<string> dig;
        vector<pair<string, string> > let;
        vector<string> out;
        int i,j=0;
        for (i = 0; i < logs.size(); i++) {
            string second = logs[i].substr(logs[i].find(" ") + 1, logs[i].find(" "));
            if(isdigit(second[0]) == 0) {
                string firstWord = logs[i].substr(0, logs[i].find(" "));
                string rest = logs[i].substr(logs[i].find_first_of(" \t")+1);
                let.push_back(make_pair(firstWord, rest));
            }
                    
            else 
                dig.push_back(logs[i]);
        }
        for(i = 0; i < let.size()-1; i++) {
            for (j = i+1; j < let.size(); j++) {
                if((let[i].second == let[j].second) && (let[j].first < let[i].first)) 
                    swap(let[i], let[j]);
            
                else if (let[i].second > let[j].second)
                    swap(let[i], let[j]);
            }
        }
        for( i = 0; i < let.size(); i++) {
            string concat = let[i].first;
            concat += " ";
            concat += let[i].second;
            out.push_back(concat);
            concat = "";
        }
        out.insert(end(out), begin(dig), end(dig));
        return out;
    }
};
