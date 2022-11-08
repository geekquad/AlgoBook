int rabin_karp(char* txt, char* pat){
    int n = strlen(txt);
    int m = strlen(pat);
    int pat_hash = 0;
    int txt_hash = 0;

    for (int k = 0; k < m ; k++){
        pat_hash += pat[k];
        txt_hash += txt[k];
    }
    
    for (int i = 0; i <= n - m; i++) {
        if(pat_hash == txt_hash){
            for(int j = 0; j < m; j++){
                if(pat[j] != txt[i+j]){
                    break;
                }
            }
            if(j == m){
                return i;
            }
        }
        txt_hash = txt_hash - txt[i] + txt[i+m];
    }
    return -1;
}