package _2025._01M._10;

// https://www.acmicpc.net/problem/3003

import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter (System.out));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int[] real = {1,1,2,2,2,8};
        List<Integer> real_list = new ArrayList<>(real.);
        List<Integer> now_list = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            now_list.add(Integer.parseInt(st.nextToken()));
        }



    }
}