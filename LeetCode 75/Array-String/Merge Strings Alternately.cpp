class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string str;
        int x=0;
        while(word1.length()>x || word2.length()>x)
        {
            if(word1.length()>x)
            {
                str+=word1[x];
            }
            if(word2.length()>x)
            {
                str+=word2[x];
            }
            x++;
        }
        return str;
    }

};
