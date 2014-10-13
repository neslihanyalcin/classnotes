#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string>
#include <fstream>
#include "segment-graph.h"

using namespace std;

int vertices_count = 0; int edges_count = 0;

universe* segment_distances(string file, float threshold) {
  ifstream infile(file);  
  string line = "";
  int i=0; 
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

  universe *u = segment_graph(vertices_count, edges_count, edges, threshold);

  return u;

}

int main(int argc, char **argv) {

  universe *u = segment_distances("test.mtx", 1.0);

  cout << "sets " << u->num_sets() << endl << endl;
  cout << "vert " << vertices_count << endl;
  
  /*
  cout << "found " <<  u->find(0) << endl;
  cout << "found " <<  u->find(1) << endl;
  cout << "found " <<  u->find(2) << endl;
  cout << "found " <<  u->find(3) << endl;
  cout << "found " <<  u->find(4) << endl; 
  */
  cout << "point;cluster" << endl;
  for (int i=0;i<vertices_count;i++){
    cout << i << ";" << u->find(i) << endl;
  }
  
  return 0;
}

