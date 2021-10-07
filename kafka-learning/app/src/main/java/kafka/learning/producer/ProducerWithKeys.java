package kafka.learning.producer;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;
import org.checkerframework.checker.units.qual.C;

import java.util.Properties;
import java.util.concurrent.ExecutionException;

public class ProducerWithKeys {


    public static void main(String[] args) throws ExecutionException, InterruptedException {
        Properties p = new Properties();
        String bootstrapServer = "localhost:9092";
        p.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        p.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        p.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServer);

        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(p);
        String topicName = "first_topic";

        for (int i = 0; i < 10; i++) {
            String data = "Hello world = " + i ;
            String key = "id_" + i%4;
            ProducerRecord<String,String> pr = new ProducerRecord<>(topicName, key, data);

            producer.send(pr, new Callback() {
                @Override
                public void onCompletion(RecordMetadata metadata, Exception exception) {
                    if(exception == null){
                        System.out.println("key : " + key + ",  partition : " + metadata.partition());
                    }
                }
            }).get() ;

        }

    }
}
