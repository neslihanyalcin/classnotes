
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include "segment-graph.h"

/*
0 2 0 0
2 0 1 0
0 1 0 3
0 0 3 0
 */

int main(int argc, char **argv) {

  edge* s = new edge[6];
  s[0].w = 2; s[0].a = 0; s[0].b = 1;
  s[1].w = 2; s[1].a = 1; s[1].b = 0;
  s[2].w = 1; s[2].a = 1; s[2].b = 2;
  s[3].w = 1; s[3].a = 2; s[3].b = 1;
  s[4].w = 3; s[4].a = 2; s[4].b = 3;
  s[5].w = 3; s[5].a = 3; s[5].b = 2;

  universe *u = segment_graph(4, 6, s, 2);
  std::cout << "sets " << u->num_sets() << std::endl;
  
  return 0;
}

