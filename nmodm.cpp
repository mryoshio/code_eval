#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

vector<int> split(string str, char delimiter) {
  vector<int> res;
  istringstream iss(str);
  string tmp;
  while (getline(iss, tmp, delimiter)) res.push_back(stoi(tmp));
  return res;
}

int main(int argc, char** argv) {
  ifstream file(argv[1]);
  string s;
  while (getline(file, s)) {
    vector<int> sep = split(s, ',');
    int ans = sep[0] / sep[1];
    cout << sep[0] - sep[1] * ans << endl;
    // cout << "--> " << ans << endl;
  }
  return 0;
}
