package com.learning;

public class ThreadCreationRunnableInterface {

    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(() -> {
            System.out.println("Current Thread name : " + Thread.currentThread().getName());
            System.out.println("Inside Current thread prioroty : " + Thread.currentThread().getPriority());
            throw new RuntimeException("Uncaught Exception");
        });

        thread.setName("My first thread");
        thread.setPriority(Thread.MAX_PRIORITY);
        thread.setUncaughtExceptionHandler( new Thread.UncaughtExceptionHandler() {

            @Override
            public void uncaughtException(Thread t, Throwable e) {
                System.out.println("A critical error has happened");
                e.printStackTrace();
            }
        });

        System.out.println("Current thread name is " + Thread.currentThread().getName());
        thread.start();
//        Thread.sleep(1000);
        System.out.println("Current thread name is " + Thread.currentThread().getName());
    }
}
