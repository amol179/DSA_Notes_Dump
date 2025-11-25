/*
ID: amolgur1
LANG: C
TASK: camelot
*/

#include <stdio.h>
#include <string.h>

#define MAXR 30
#define MAXC 26
#define MAXK 900
#define INF 1000000

int R, C;
int king_r, king_c;
int knight_r[MAXK], knight_c[MAXK], knight_count;

int drk[8] = {-1,-1,-1,0,0,1,1,1};
int dck[8] = {-1,0,1,-1,1,-1,0,1};

int drn[8] = {-2,-2,-1,-1,1,1,2,2};
int dcn[8] = {-1,1,-2,2,-2,2,-1,1};

int king_dist[MAXR][MAXC];
int knight_dist[MAXK][MAXR][MAXC];
int knight_move[MAXR][MAXC][MAXR][MAXC];
int queue_r[10000], queue_c[10000];

void bfs(int sr, int sc, int dist[MAXR][MAXC], int dr[], int dc[], int len) {
    memset(dist, -1, sizeof(int) * MAXR * MAXC);
    int front = 0, back = 0;
    queue_r[back] = sr;
    queue_c[back++] = sc;
    dist[sr][sc] = 0;
    while (front < back) {
        int r = queue_r[front], c = queue_c[front++];
        for (int i = 0; i < len; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr >= 0 && nr < R && nc >= 0 && nc < C && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                queue_r[back] = nr;
                queue_c[back++] = nc;
            }
        }
    }
}

void precompute_knight_moves() {
    int dist[MAXR][MAXC];
    for (int sr = 0; sr < R; sr++) {
        for (int sc = 0; sc < C; sc++) {
            bfs(sr, sc, dist, drn, dcn, 8);
            for (int r = 0; r < R; r++)
                for (int c = 0; c < C; c++)
                    knight_move[sr][sc][r][c] = dist[r][c];
        }
    }
}

int main() {
    FILE *fin = fopen("camelot.in", "r");
    FILE *fout = fopen("camelot.out", "w");

    fscanf(fin, "%d %d", &R, &C);
    char col;
    int row;
    fscanf(fin, " %c %d", &col, &row);
    king_r = row - 1;
    king_c = col - 'A';

    knight_count = 0;
    while (fscanf(fin, " %c %d", &col, &row) == 2) {
        knight_r[knight_count] = row - 1;
        knight_c[knight_count] = col - 'A';
        knight_count++;
    }

    bfs(king_r, king_c, king_dist, drk, dck, 8);
    for (int i = 0; i < knight_count; i++) {
        bfs(knight_r[i], knight_c[i], knight_dist[i], drn, dcn, 8);
    }
    precompute_knight_moves();

    int min_total = INF;

    for (int gr = 0; gr < R; gr++) {
        for (int gc = 0; gc < C; gc++) {
            int total = 0;
            int valid = 1;
            for (int i = 0; i < knight_count; i++) {
                int d = knight_dist[i][gr][gc];
                if (d == -1) {
                    valid = 0;
                    break;
                }
                total += d;
            }
            if (!valid) continue;

            int best = total + king_dist[gr][gc];

            for (int i = 0; i < knight_count; i++) {
                for (int dr = -3; dr <= 3; dr++) {
                    for (int dc = -3; dc <= 3; dc++) {
                        int pr = king_r + dr;
                        int pc = king_c + dc;
                        if (pr < 0 || pr >= R || pc < 0 || pc >= C) continue;
                        if (knight_dist[i][pr][pc] == -1 || king_dist[pr][pc] == -1) continue;
                        int cd = knight_move[pr][pc][gr][gc];
                        if (cd == -1) continue;
                        int cost = total - knight_dist[i][gr][gc]
                                 + knight_dist[i][pr][pc]
                                 + king_dist[pr][pc]
                                 + cd;
                        if (cost < best) best = cost;
                    }
                }
            }

            if (best < min_total) min_total = best;
        }
    }

    fprintf(fout, "%d\n", min_total);
    fclose(fin);
    fclose(fout);
    return 0;
}