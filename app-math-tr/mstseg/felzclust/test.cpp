
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string>
#include <fstream>
#include "segment-graph.h"

using namespace std;

universe* read() {
  ifstream infile("test.mtx");
  string line = "";
  int i=0; int vertices_count = 0; int edges_count = 0;
  edge* edges = NULL;
  while (getline(infile, line)) {
    if (line.find("%") != std::string::npos) continue;
    stringstream strstr(line);
    string word = "";
    int a; int b; float w;
    int j = 0;
    while (getline(strstr,word, ' ')) {
      if (j == 0) a = atoi(word.c_str());
      else if (j == 1) b = atoi(word.c_str());
      else if (j == 2) w = atof(word.c_str());
      j++;
    }    
    cout << a << " " << b << " " << w << endl;
    if (i == 0) {
      vertices_count = a;
      edges_count = (int)w;
      edges = new edge[edges_count];
      cout << "vertices " << vertices_count << " edges " << edges_count << endl;
    } else {
      edges[i-1].a = a;
      edges[i-1].b = b;
      edges[i-1].w = w;      
    }
    i++;
  }

  universe *u = segment_graph(vertices_count, edges_count, edges, 0.3);

  return u;

}

int main(int argc, char **argv) {

  universe *u = read();

  /*
  edge* s = new edge[8];
  s[0].w = 1/2; s[0].a = 0; s[0].b = 1;
  s[1].w = 1/2; s[1].a = 1; s[1].b = 0;
  s[2].w = 1; s[2].a = 1; s[2].b = 2;
  s[3].w = 1; s[3].a = 2; s[3].b = 1;
  s[4].w = 1/3; s[4].a = 2; s[4].b = 3;
  s[5].w = 1/3; s[5].a = 3; s[5].b = 2;
  s[6].w = 1/2; s[6].a = 0; s[6].b = 5;
  s[7].w = 1/2; s[7].a = 5; s[7].b = 0;
  
  universe *u = segment_graph(5, 6, s, 0.3);
  */

  cout << "sets " << u->num_sets() << endl << endl;
  cout << "found " <<  u->find(0) << endl;
  cout << "found " <<  u->find(1) << endl;
  cout << "found " <<  u->find(2) << endl;
  cout << "found " <<  u->find(3) << endl;
  cout << "found " <<  u->find(4) << endl;

  
  return 0;
}

