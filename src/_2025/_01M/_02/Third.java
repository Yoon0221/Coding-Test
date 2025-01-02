package _2025._01M._02;

// https://www.acmicpc.net/problem/5622

import java.io.*;
import java.util.*;

public class Third {
    static BufferedReader br = new BufferedReader (new InputStreamReader (System.in));

    public static void main(String[] args) throws IOException {
        String s = br.readLine();

        List<Integer> list = new ArrayList<>();

        int now = 2;
        int next = 0;
        for (int i = 0; i < 15; i++) {
            list.add(now);
            next += 1;

            if (next == 3) {
                now += 1;
                next = 0;
            }
        }
        for (int i = 0; i < 4; i++) {
            list.add(7);
        }
        for (int i = 0; i < 3; i++) {
            list.add(8);
        }
        for (int i = 0; i < 4; i++) {
            list.add(9);
        }


        // 0 ~ 25
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            int now_int = list.get(s.charAt(i) -'0' -17) + 1;
            result += now_int;
        }

        System.out.println(result);

    }
}