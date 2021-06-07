#include <iostream>
#include <vector>
#include <string>

using namespace std;

std::string longBurp(int num) {
	std::string ret = "Bu";
	for ( int i = 0; i < num; i++ ) {
		ret += "r";
	}
	return ret + "p";
}


int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
    std::string r = longBurp(12);
    cout << r;
}

