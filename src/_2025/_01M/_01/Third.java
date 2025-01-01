package _2025._01M._01;

// https://www.acmicpc.net/problem/2675

import java.io.*;
import java.util.*;

public class Third {

    static BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
    static StringTokenizer st;
    static BufferedWriter bw = new BufferedWriter (new OutputStreamWriter (System.out));

    public static void main (String[] ars)throws IOException {
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            String s = st.nextToken();

            String now_s = "";
            for (int j = 0; j < s.length(); j++) {
                for (int k = 0; k < r; k++) {
                    now_s = now_s + s.charAt(j);
                }
            }

            bw.write(now_s);
            bw.write("\n");
        }

        bw.flush();
        bw.close();

    }

}