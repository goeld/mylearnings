package kafka.learning.producer;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class ProducerDemo {

    public static void main(String[] args) {
        System.out.println("Hello World");
        String bootStrapServers = "127.0.0.1:9092";

        // Kafka Producer properties
        Properties props = new Properties();
        props.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootStrapServers);
        props.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());


        // Creatre Producer
        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(props);


        // Send data
        ProducerRecord<String, String> record = new ProducerRecord<>("first_topic", "hello_world_from_java");

        producer.send(record);
        producer.flush();
        producer.close();
    }
}
