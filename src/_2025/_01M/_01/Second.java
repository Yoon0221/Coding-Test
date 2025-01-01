package _2025._01M._01;

// https://www.acmicpc.net/problem/10809

import java.io.*;
import java.util.*;

public class Second {
    static BufferedReader br = new BufferedReader(new InputStreamReader (System.in));
    static StringTokenizer st;

    public static void main (String[] args) throws IOException {

        String s = br.readLine();

        // 0 ~ 25
        int[] nums = new int[26];

        for (int i = 0; i < 26; i++) {
            nums[i] = -1;
        }

        for (int i = 0; i < s.length(); i++) {
            int now = s.charAt(i)-'0'-49;
            if (nums[now] == -1)
                nums[now] = i;
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(nums[i] + " ");
        }

    }
}