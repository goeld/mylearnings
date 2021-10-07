package kafka.learning.producer;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;

import java.util.Properties;

public class ProducerDemoWithCallBacks {

    public static void main(String[] args) {

        Properties props = new Properties();
        String bootstrapServers = "127.0.0.1:9092";
        String topicName = "first_topic";

        // Create Producer Config
        props.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        props.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        props.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        // Create Kafka Producer
        KafkaProducer<String, String> producer = new KafkaProducer<String, String>(props);

        // Send Data
        for (int i = 0; i < 10; i++) {

            String data = "Hello World again = " + i  ;
            ProducerRecord<String, String> producerRecord = new ProducerRecord<>(topicName, data);
            producer.send(producerRecord, new Callback() {
                @Override
                public void onCompletion(RecordMetadata metadata, Exception exception) {
                    if (exception == null) {
                        System.out.println("Offset" + metadata.offset());
                        System.out.println("Partition" + metadata.partition());
                        System.out.println("Partition" + metadata.timestamp());
                    } else {
                        exception.printStackTrace();
                    }
                }
            });
        }
        producer.close();

    }
}
