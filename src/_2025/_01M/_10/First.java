package _2025._01M._10;

// https://xn--acmicpc-eh94a.net/problem/11718

import java.io.*;
import java.util.*;

public class First {
    static BufferedReader br = new BufferedReader (new InputStreamReader (System.in)) ;
    static BufferedWriter bw = new BufferedWriter (new OutputStreamWriter (System.out));

    public static void main(String[] args) throws IOException {
        while(true) {
            String temp =br.readLine() ;
            if (temp == null || temp.isEmpty())
                break;
            else {
                bw.write(temp + "\n");
            }
        }
        bw.flush();
        bw.close();

    }
}