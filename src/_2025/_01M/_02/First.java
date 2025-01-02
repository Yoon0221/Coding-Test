package _2025._01M._02;

// https://www.acmicpc.net/problem/1152

import java.io.*;
import java.util.*;

public class First {

    static BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
    static StringTokenizer st;

    public static void main(String[] args)throws IOException {

        String s = br.readLine();
        s = s.trim();

        if (s.isEmpty()) {
            System.out.println(0);
        } else {
            int sum = 1;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == ' ')
                    sum += 1;
            }

            System.out.println(sum);
        }

    }
}