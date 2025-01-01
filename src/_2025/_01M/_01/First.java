package _2025._01M._01;

// https://www.acmicpc.net/problem/11720

import java.io.*;
import java.util.*;

public class First {

    static BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
    static StringTokenizer st;

    public static void main (String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        int sum = 0;
        String s = br.readLine();
        for (int i = 0; i < n; i++) {
            int now = s.charAt(i) - '0';
            sum += now;
        }

        System.out.println(sum);
    }

}