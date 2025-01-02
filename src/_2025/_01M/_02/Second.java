package _2025._01M._02;

// https://www.acmicpc.net/problem/2908

import java.io.*;
import java.util.*;

public class Second {

    static BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main (String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        String a = st.nextToken();
        String b = st.nextToken();

        String aa = "";
        String bb = "";
        for (int i = 2; i >= 0; i--) {
            aa += a.charAt(i);
            bb += b.charAt(i);
        }

        int result = (Integer.parseInt(aa) > Integer.parseInt(bb) ) ? Integer.parseInt(aa) : Integer.parseInt(bb);
        System.out.println(result);
    }
}