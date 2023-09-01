// C++14 program to build a suffix array in O(nlogn) time;
#define trav(a, x) for (auto &a : x)
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

vector<string> split(string s);

vi pi(const string &s) {
  vi p(sz(s));
  rep(i, 1, sz(s)) {
    int g = p[i - 1];
    while (g && s[i] != s[g])
      g = p[g - 1];
    p[i] = g + (s[i] == s[g]);
  }
  return p;
}

vi match(const string &s, const string &pat) {
  vi p = pi(pat + '\0' + s), res;
  rep(i, sz(p) - sz(s), sz(p)) if (p[i] == sz(pat))
      res.push_back(i - 2 * sz(pat));
  return res;
}