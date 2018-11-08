
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "scoreText.h"

#define TEMP 20
#define STEP 0.1
#define COUNT 10000

char *foursquareDecipher(char *key1,char *key2, char *in,char *out, int len);
float foursquareCrack(char *text,int len, char* maxKey1, char* maxKey2);
static char *shuffleKey(char *in);

int main(int argc, char *argv[])
{
    // THINGS TO ENSURE: CIPHER AND KEY MUST BE UPPERCASE, CONSISTING ONLY OF LETTERS A-Z, AND NO OTHERS. YOU CAN SPELL OUT NUMBERS IF YOU NEED TO.
    // NEITHER THE CIPHER OR THE KEY SHOULD HAVE THE LETTER 'J' IN IT. IT WILL CRASH IF YOU DO NOT DO THESE THINGS. THIS IS A PROOF OF CONCEPT ONLY.
    char cipher[]  = "JKYRMGHJ WDMDI YNZ GLZ HE KJLX KD RCYHTR YR WZGKYZI ZK NZA JNZYV HYZPYR SD CYR HIDMGHJ WDMDI HAK ZKYD PGDLFYH SZ YZDJJDXXZI JDA CHCLWIYZI PWKYHIHG JRA HA GDRSPRWB YZGRE XZGS HIDMCR GZS VJR ZK YRWB D JDAK YZ CYR YZDJLSYZI NZJ ZK HE KJLX PTHKRGKJ GLZ JPRNWR JR HXZIKLZ HAK HIYHLWSYD ZK YRWB R CHHY D CYR JDJDGI HAK ZK HJYZBJHG HAK HYDXGHKHC ZK YZZJ KCRKJAIDHG YD TYDKHHX HE WWDN JPZMYH JGZGHBXH HAKPWWLSHGRI CRHGK KJLX HN CYR HBZGLH YGHAKGZY YD HIYHLWSYD JKD SZ AKCRHGE HAK YHMDT HGDBXH HAK ZK KRHGAK XGHK GHTYZW R KYHJHGB PRX SWHJKD HLTRHW HAK CYRA GHAKZ HAK YZYZDJDM PGRYZDJYRBOH JRDJJLG YD YDHG ZK XDA YZ PWHG YRI HN VYDAK D ZJ HTRKYRMCR JDA ZK KZY JD RDJJLG CHWCDGEYL YR KRAK CHIYDMYZI HE ZK CHHY KZY WWDN HA CYR GRN GHAKGLS CDZMR ZK CYR YZDTHG HAK YD GHNZB SZ HIYRWRE R YDRKYDRX ZK YHHV PWGRWLIDKGRB JD VIGRXJDEHJLRI GLZ ZK JGZGHBXH HHGAK HAK SZ HLTRHW HAK HTRTYH ZK HWEDJJZB HE PRX KD JKATDWKZZS HAK SZ HGRWT HAK XZGS PRNR PRWB HAK KIHGDC ZK CYR JGZKIR HAK HIYHLWSYD ZK PGK ZK YZDKHGIJDC AKDN CHHIZGB ZK JL NZWWR PRX JDAK KYHCLGB KHP CYR CHTRTYH PWWRGZX HXDK HXRJ HAK KR HGDBXH HAK SZ JHIRS ZNK HAK CWGZN HAK ZK JHKRGKJYZXHC JJHGB HAK CYR KYHXRDWGRB YD CHKILCYZI HKLBJDC GDHAK PKDYLKGZBBZ YR JKYHJHGB DWHRGJDC CYR HYZKJCRWT YHHNKHE KYHXHHGTRJDC IDWELB HAK KRAK VYDAK D YZDKIHWSHG YZ KLE JXDR GLZ KLZER YZDJLSYZI ZK CRHW CWLZI JDAK KRAK HLGK JD KD CYR JIDKIRK GZ PTHKRGKJ PIDWZB YZ HHGTR ZK HWERYL HGR JGHCRHW WRIDKDWZB GLZ KRAK HKRYLKGZSYL GRHBBR PRX KD CRZGER CYR HXZA KR JLZWWRI CYR VRHN TYDGRHBBR VJDG HA YHAK YZDKIRYD JWHJYLZI HA SD HIYHGHSGHKYD YRDJJLG YXHCYZI ZK KWLIDSSDC HE WWDN KD YHAK YZDKIR JKGZBBLJ HA SD VGZS JYZKGZX AKDN CHIRS JD HA GHKJDYDX HXDGB HAK GZS KWLIDSSDC JTYDAK HVRX CYR YZDKYHMGHKYD GZS KGZBBLJ ZK CRHW CWLZI AIDAN YZDKIR GZS HKDKHBBR IDWELB R CHGGDKJ JRA KJRH HAK SZ YZDKJHLF HAK CYR JGZGGZA YRDGRTWLE KHWABXRB JHYZKJCRWT HXZA KRKRHGAK GHCYL HE WWDN RDCYD ZK JHKLZG TYDCRGK GLZ YHAK HWBZYDKYRKJYZI HVRK CYR KIR PHAK SD CYR JYRXZKKZ HAK HTRTYH ZK JVHHJ KD HJLIOH HAK JR JDAK HVRK WWDN RDJJLG KRAK VJDG R JD HGHAK HBZGLH SZ JHDGHWWHIYRAI HAK YD HTRGKLZ CHJLRI JRA JVGLK HAK PE YZDJJHGBBLJ WRKLGE JKD CYR RDGRTWLE YD TYDJDGBL WDGBR HAK";
    int len = strlen(cipher);
    char *out = malloc(sizeof(char)*(len+1));
    srand((unsigned)time(NULL)); // randomise the seed, so we get different results each time we run this program

    printf("Running foursquarecrack, this could take a few minutes...\n");

    char key1[] = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    char key2[] = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    int i=0;
    double score,maxscore=-99e99;
    // run until user kills it
    while(1){
        i++;
        score = foursquareCrack(cipher,len,key1,key2);
        if(score > maxscore){
            maxscore = score;
            printf("best score so far: %f, on iteration %d\n",score,i);
            printf("    Key: '%s','%s'\n",key1,key2);
            foursquareDecipher(key1,key2, cipher,out, len);
            printf("    plaintext: '%s'\n",out);
        }
    }
    free(out);
    return 0;
}

void exchange2letters(char *key){
    int i = rand()%25;
    int j = rand()%25;
    char temp = key[i];
    key[i]= key[j];
    key[j] = temp;
}

// this is the bit that implements the simulated annealing algorithm
float foursquareCrack(char *text,int len, char* bestKey1, char* bestKey2){
    int i,j,count;
    float T;
    char temp, *deciphered = malloc(sizeof(char) * (len+1));
    char testKey1[26],testKey2[26];
    char maxKey1[26],maxKey2[26];
    double prob,dF,maxscore,score;
    double bestscore;
    strcpy(maxKey1,bestKey1);
    strcpy(maxKey2,bestKey2);
    foursquareDecipher(maxKey1,maxKey2,text,deciphered,len);
    maxscore = scoreTextQgram(deciphered,len);
    bestscore = maxscore;
    for(T = TEMP; T >= 0; T-=STEP){
        for(count = 0; count < COUNT; count++){
            strcpy(testKey1,maxKey1);
            strcpy(testKey2,maxKey2);
            if(count%2==0){
                exchange2letters(testKey1);
            }else{
                exchange2letters(testKey2);
            }
            foursquareDecipher(testKey1,testKey2,text,deciphered,len);
            score = scoreTextQgram(deciphered,len);
            dF = score - maxscore;
            if (dF >= 0){
                maxscore = score;
                strcpy(maxKey1,testKey1);
                strcpy(maxKey2,testKey2);
            }else if(T > 0){
                prob = exp(dF/T);
                if(prob > 1.0*rand()/RAND_MAX){
                    maxscore = score;
                    strcpy(maxKey1,testKey1);
                    strcpy(maxKey2,testKey2);
                }
            }
            // keep track of best score we have seen so far
            if(maxscore > bestscore){
                bestscore = maxscore;
                strcpy(bestKey1,maxKey1);
                strcpy(bestKey2,maxKey2);
            }
        }
    }
    free(deciphered);
    return bestscore;
}


char *foursquareDecipher(char *key1,char *key2, char *text, char *result, int len){
    int i;
    char a,b; /* the digram we are looking at */
    int a_ind,b_ind;
    int a_row,b_row;
    int a_col,b_col;
    char alph[] = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

    for (i = 0; i < len; i += 2){
        a = text[i];
        b = text[i+1];
        /*if (index(key,a) == NULL || index(key,b) == NULL) break;*/
        a_ind = (int)(strchr(key1,a) - key1);
        b_ind = (int)(strchr(key2,b) - key2);
        a_row = a_ind / 5;
        b_row = b_ind / 5;
        a_col = a_ind % 5;
        b_col = b_ind % 5;
        result[i] = alph[5*a_row + b_col];
        result[i+1] = alph[5*b_row + a_col];
    }
    result[i] = '\0';
    return result;
}

// do fisher yeates shuffle
static char *shuffleKey(char *in){
    int i,j;
    char temp;
    for (i = 24; i >= 1; i--){
        j = rand() % (i+1);
        temp = in[j];
        in[j] = in[i];
        in[i] = temp;
    }
    return in;
}
