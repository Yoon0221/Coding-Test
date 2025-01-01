package _2025._01M._02;

// https://www.acmicpc.net/problem/1152

import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        String s = br.readLine();

        s = s.trim();

        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ')
                result += 1;
        }

        System.out.println(result+1);
    }
}