//  Copyright 2013 Google Inc. All Rights Reserved.
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <malloc.h>
#define N 100
#define max_size 2000

//const long long max_size = 2000;         // max length of strings
//const long long N = 100;                  // number of closest words that will be shown
const long long max_w = 50;              // max length of vocabulary entries


typedef struct State {
  FILE *f;
  char st1[2000];
  char bestw[N][max_size];
  char file_name[max_size], st[100][max_size];
  float dist, len, bestd[N], vec[max_size];
  long long words, size, a, b, c, d, cn, bi[100];
  char ch;
  float *M;
  char *vocab;
} State;


State* construct(char *file, float *M, char *vocab, State* state) {
  FILE *f;
  char st1[max_size];
  char *bestw[N];
  char file_name[max_size], st[100][max_size];
  float dist, len, bestd[N], vec[max_size];
  long long words, size, a, b, c, d, cn, bi[100];
  char ch;
  //float *M;
  //char *vocab;
  printf("sizeof state: %d \n", sizeof(State));
  //State *state = malloc(sizeof(State));
  printf("%p\n",M);

  printf(file);

  // Handle CLI arguments
 // if (argc < 2) {
 //   printf("Usage: ./distance <FILE>\nwhere FILE contains word projections in the BINARY FORMAT\n");
 //   return state;
  //}
  //strcpy(file_name, argv[1]);
  strcpy(file_name, file);

  // Read in Word Vector Binary
  f = fopen(file_name, "rb");
  if (f == NULL) {
    printf("Input file not found\n");
    return state;
  }
  fscanf(f, "%lld", &words);
  fscanf(f, "%lld", &size);
  printf("words: %lld size:%lld,", words, size);
  //vocab = (char *)malloc((long long)words * max_w * sizeof(char));
  //for (a = 0; a < N; a++) bestw[a] = (char *)malloc(max_size * sizeof(char));
  //M = (float *)malloc((long long)words * (long long)size * sizeof(float));
  if (M == NULL) {
    printf("Cannot allocate memory: %lld MB    %lld  %lld\n", (long long)words * size * sizeof(float) / 1048576, words, size);
    return state;
  }

  // Compute ???
  for (b = 0; b < words; b++) {
    a = 0;
    while (1) {
      vocab[b * max_w + a] = fgetc(f);
      if (feof(f) || (vocab[b * max_w + a] == ' ')) break;
      if ((a < max_w) && (vocab[b * max_w + a] != '\n')) a++;
    }
    vocab[b * max_w + a] = 0;
    for (a = 0; a < size; a++) fread(&M[a + b * size], sizeof(float), 1, f);
    len = 0;
    for (a = 0; a < size; a++) len += M[a + b * size] * M[a + b * size];
    len = sqrt(len);
    for (a = 0; a < size; a++) M[a + b * size] /= len;
  }


  // Assign all needed values to State* state, to be passed up to Python handler
  // And given back to get_neighbors to get vector neighbors
  strcpy(state -> st1, st1);

  memcpy(state->bestw, bestw, N * sizeof(char*));
// for (a = 0; a < N; a++) {
//    state->bestw[a] = bestw[a];
//  }
  strcpy(state -> file_name, file_name);
  for (a = 0; a < N; a++) {
    strcpy(state->st[a], st[a]);
  }
  state -> dist = dist;
  state -> len = len;
  for (a = 0; a < N; a++) {
    state->bestd[a] = bestd[a];
  }
  for (a = 0; a < max_size; a++) {
    state->vec[a] = vec[a];
  }
  state->words = words;
  state->size = size;
  state->a = a;
  state->b = b;
  state->c = c;
  state->d = d;
  state->cn = cn;
  for (a = 0; a < 100; a++) {
    state->bi[a] = bi[a];
  }
  state->ch = ch;
  state->M = M;
  state->vocab = vocab;
  fclose(f); // AND now we're done with the original file.
  printf("state[%p]\n", state);
  return state;
}
char **get_neighbors(State *state, char *word, char **bestw) {
  printf("state[%p]\n", state);
  
  char st1[max_size];
  //char *bestw[N];
  char file_name[max_size], st[100][max_size];
  float dist, len, bestd[N], vec[max_size];
  long long words, size, a, b, c, d, cn, bi[100];
  float *M;
  char *vocab;
  printf(word);

  // Read back in the values to their original
  // Variable names, to make the program run like it wanted to originally.

  
  
  //strcpy(st1, state->st1);
  //memcpy(bestw, state->bestw, N * sizeof(char*));
  
//  for (a = 0; a < N; a++) {
//    bestw[a] = state->bestw[a];
//  }
 
  //strcpy(file_name, state->file_name);
  //for (a = 0; a < N; a++) {
  //  strcpy(st[a], state->st[a]);
  //}
  dist = state->dist;
  len = state->len;
  //for (a = 0; a < N; a++) {
  //  bestd[a] = state->bestd[a];
  //}
  //for (a = 0; a < max_size; a++) {
  //  vec[a] = state->vec[a];
  //}
  
  words = state->words;
  size = state->size;
  a = state->a;
  b = state->b;
  c = state->c;
  d = state->d;
  cn = state->cn;
  //for (a = 0; a < 100; a++) {
  //  bi[a] = state->bi[a];
  //}
  M = state->M;
  vocab = state->vocab;
  printf("M[%p]\n", M);

  // These don't need to be assigned in construct, so do 'em here.
  //vocab = (char *)malloc((long long)words * max_w * sizeof(char));
  for (a = 0; a < N; a++) bestw[a] = (char *)malloc(max_size * sizeof(char));

  // Main computation loop. Wait for input, and then print vectors or something?
  for (a = 0; a < N; a++) bestd[a] = 0;
  //for (a = 0; a < N; a++) bestw[a][0] = 0;
 // printf("Enter word or sentence (EXIT to break): ");
 // a = 0;
 // while (1) {
 //   st1[a] = fgetc(stdin);
 //   if ((st1[a] == '\n') || (a >= max_size - 1)) {
 //     st1[a] = 0;
 //     break;
 //   }
 //   a++;
 // }
  strcpy(st1, word);
  //if (!strcmp(st1, "EXIT")) break;
  cn = 0;
  b = 0;
  c = 0;

  // Another loop to do...
  while (1) {
    st[cn][b] = st1[c];
    b++;
    c++;
    st[cn][b] = 0;
    if (st1[c] == 0) break;
    if (st1[c] == ' ') {
      cn++;
      b = 0;
      c++;
    }
  }
  cn++;

  
  // Also another loop: 
  for (a = 0; a < cn; a++) {
    for (b = 0; b < words; b++) if (!strcmp(&vocab[b * max_w], st[a])) break;
    if (b == words) b = -1;
    bi[a] = b;
    //printf("\nWord: %s  Position in vocabulary: %lld\n", st[a], bi[a]);
    if (b == -1) {
      //printf("Out of dictionary word!\n");
      //break;
    }
    printf("%d",a);
  }
  
  // Now we're ready to print out our vectors 
  //if (b == -1) continue;
  printf("\n                                              Word       Cosine distance\n------------------------------------------------------------------------\n");
  for (a = 0; a < size; a++) vec[a] = 0;
  for (b = 0; b < cn; b++) {
    if (bi[b] == -1) continue;
    for (a = 0; a < size; a++){
      vec[a] += M[a + bi[b] * size];
      //printf("%f\n", M[0]);
      //printf("%f\n", vec[a]);
    }
  }
  len = 0;
  printf("%f\n", len);
  //printf("%f\n", vec[0]);
  for (a = 0; a < size; a++){ len += vec[a] * vec[a];}
  //printf("%f\n", len);
  len = sqrt(len);
  for (a = 0; a < size; a++) vec[a] /= len;
  for (a = 0; a < N; a++) bestd[a] = -1;
  for (a = 0; a < N; a++) bestw[a][0] = 0;
  
  for (c = 0; c < words; c++) {
    a = 0;
    for (b = 0; b < cn; b++) if (bi[b] == c) a = 1;
    if (a == 1) continue;
    dist = 0;
    for (a = 0; a < size; a++) dist += vec[a] * M[a + c * size];
    for (a = 0; a < N; a++) {
      if (dist > bestd[a]) {
        for (d = N - 1; d > a; d--) {
          bestd[d] = bestd[d - 1];
          strcpy(bestw[d], bestw[d - 1]);
        }
        bestd[a] = dist;
        strcpy(bestw[a], &vocab[c * max_w]);
        break;
      }
    }
  }
  // Print out the neighbors
  //for (a = 0; a < N; a++) printf("%50s\t\t%f\n", bestw[a], bestd[a]);
  fflush(stdout);
  return bestw;
}

State* dummy(char *file) {
  printf(file);
  return 0;
}

int main(int argc, char **argv) {
  char *file = "GoogleNews-vectors-negative300.bin";
  State* state = dummy(file);
  get_neighbors(state, "pizza", 0);
}
