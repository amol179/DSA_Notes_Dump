/*
ID: amolgur1
LANG: C
TASK: msquare
*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int dist[40320];
int queue[40325][8];
int qhead, qtail;

int encode(int *board) {
    static int mult[8] = {1, 8, 56, 336, 1680, 6720, 20160, 40320};
    int look[8] = {0, 1, 2, 3, 4, 5, 6, 7};
    int rlook[8] = {0, 1, 2, 3, 4, 5, 6, 7};
    int rv = 0, t;

    for (int lv = 0; lv < 8; lv++) {
        t = look[board[lv]];
        assert(t < 8 - lv);
        rv += t * mult[lv];
        look[rlook[7 - lv]] = t;
        rlook[t] = rlook[7 - lv];
    }
    return rv;
}

int tforms[3][8] = {
    {8, 7, 6, 5, 4, 3, 2, 1},
    {4, 1, 2, 3, 6, 7, 8, 5},
    {1, 7, 2, 4, 5, 3, 6, 8}
};

void do_trans(int *inboard, int *outboard, int t) {
    for (int lv = 0; lv < 8; lv++)
        outboard[lv] = inboard[tforms[t][lv] - 1];
}

void do_rtrans(int *inboard, int *outboard, int t) {
    for (int lv = 0; lv < 8; lv++)
        outboard[tforms[t][lv] - 1] = inboard[lv];
}

void do_dist(int *board) {
    qhead = 0;
    qtail = 1;
    for (int lv = 0; lv < 8; lv++)
        queue[0][lv] = board[lv];
    dist[encode(queue[0])] = 1;

    while (qhead < qtail) {
        int t1 = encode(queue[qhead]);
        int d = dist[t1];

        for (int lv = 0; lv < 3; lv++) {
            do_rtrans(queue[qhead], queue[qtail], lv);
            int t = encode(queue[qtail]);
            if (dist[t] == 0) {
                dist[t] = d + 1;
                qtail++;
            }
        }
        qhead++;
    }
}

void walk(FILE *fout) {
    int cboard[8], newboard[8];
    for (int lv = 0; lv < 8; lv++)
        cboard[lv] = lv;

    int d = dist[encode(cboard)];
    while (d > 1) {
        for (int lv = 0; lv < 3; lv++) {
            do_trans(cboard, newboard, lv);
            if (dist[encode(newboard)] == d - 1) {
                fprintf(fout, "%c", lv + 'A');
                for (int lv2 = 0; lv2 < 8; lv2++)
                    cboard[lv2] = newboard[lv2];
                break;
            }
        }
        d--;
    }
    fprintf(fout, "\n");
}

int main() {
    FILE *fin = fopen("msquare.in", "r");
    FILE *fout = fopen("msquare.out", "w");
    if (!fin || !fout) {
        perror("File open error");
        exit(1);
    }

    int board[8];
    for (int lv = 0; lv < 8; lv++) {
        fscanf(fin, "%d", &board[lv]);
        board[lv]--;
    }

    do_dist(board);
    for (int lv = 0; lv < 8; lv++)
        board[lv] = lv;

    fprintf(fout, "%d\n", dist[encode(board)] - 1);
    walk(fout);

    fclose(fin);
    fclose(fout);
    return 0;
}