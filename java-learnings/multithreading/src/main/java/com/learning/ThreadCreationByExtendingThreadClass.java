package com.learning;

public class ThreadCreationByExtendingThreadClass {

    public static void main(String[] args) {
        Thread thread = new MyThread();
        thread.start();

    }

    private static class MyThread extends Thread {

        @Override
        public void run() {
            System.out.println(" Running thread name  " + Thread.currentThread().getName());
        }
    }
}
