package org.web3j;

import org.web3j.crypto.Credentials;
import org.web3j.crypto.WalletUtils;
import org.web3j.generated.contracts.HelloWorld;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.http.HttpService;
import org.web3j.tx.gas.DefaultGasProvider;

import java.io.File;

/**
 * <p>This is the generated class for <code>web3j new helloworld</code></p>
 * <p>It deploys the Hello World contract in src/main/solidity/ and prints its address</p>
 * <p>For more information on how to run this project, please refer to our <a href="https://docs.web3j.io/quickstart/#deployment">documentation</a></p>
 */
public class Web3App {

   private static final String nodeUrl = System.getenv().getOrDefault("WEB3J_NODE_URL", "http://localhost:20002");
//   private static final String walletPassword = System.getenv().getOrDefault("WEB3J_WALLET_PASSWORD", "0xFE3B557E8Fb62b89F4916B721be55cEb828dBd73");
   private static final String walletPath = System.getenv().getOrDefault("WEB3J_WALLET_PATH", "/Volumes/aadi/workspace/goquorum/my_wallet/UTC--2022-01-19T14-48-00.366329000Z--c587c7c8752750c6f174d07de9bff9c35a05f631.json");

   public static void main(String[] args) throws Exception {
       String walletPassword = "pawword";
       String walletDirectory = "/Volumes/aadi/workspace/goquorum/my_wallet"; //add your own wallet directory path
       String walletName = WalletUtils.generateNewWalletFile(walletPassword, new File(walletDirectory));System.out.println(walletName);


       Credentials credentials = WalletUtils.loadCredentials(walletPassword, walletPath);
        Web3j web3j = Web3j.build(new HttpService(nodeUrl));
        System.out.println("Deploying HelloWorld contract ...");
        HelloWorld helloWorld = HelloWorld.deploy(web3j, credentials, new DefaultGasProvider(), "Hello Blockchain World!").send();
        System.out.println("Contract address: " + helloWorld.getContractAddress());
        System.out.println("Greeting method result: " + helloWorld.greeting().send());
       }
}

