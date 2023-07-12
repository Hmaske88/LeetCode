class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if(str1+str2==str2+str1)
        {
            // gcd -> greatest common divisor
            // we have to calculate the largest number which can divide the both numbers
            return str1.substr(0,gcd(str1.length(),str2.length()));
        }
        else
        {
            return "";
        }
    }
};
